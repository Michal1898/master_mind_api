from flask import Flask, jsonify, request
import uuid

import datetime
from random import choice, randrange, getrandbits, shuffle
from datetime import timedelta, date

from copy import copy

app = Flask(__name__)

game_active=[]


class GameZone:
    def __init__(self):
        self.DIGIT_NO = 5
        self.ATTEMPTS_NO = 10
        self.uuid = "00000000"
        self.secret_code = ["0", "0", "0", "0", "0"]
        self.current_att = 0
        self.attempts = []
        self.single_attempt = {"att_no": 0, "guessed_code": ["0", "0", "0", "0", "0"], "black_s": 0, "white_s": 0}
        self.game_over = False
        self.code_hacked = False
        self.all_colors_quessed = False

    def random_code_generator(self):
        for digit_index in range(len(self.secret_code)):
            self.secret_code[digit_index] = randrange(1, 8)
            # print (self.secret_code)
        #         a nakonec to jeste zamicham. (:-)
        shuffle(self.secret_code)
        self.secret_code = [str(digit) for digit in self.secret_code]
        # print(self.secret_code)

    def print_random_code(self):
        # list_rand_code = [str(digit) for digit in self.secret_code]
        list_rand_code = self.secret_code
        string_rand_code = " "
        string_rand_code = string_rand_code.join(list_rand_code)
        # print(string_rand_code)
        return string_rand_code

    def insert_uuid(self, game_uuid):
        self.uuid = game_uuid

    def evaluate_attempt(self, att_no, inserted_code):
        self.single_attempt.update({"att_no": att_no})
        inserted_code = list(inserted_code)
        self.single_attempt.update({"guessed_code": inserted_code})

        secret_code = copy(self.secret_code)
        print(f"Tajny kod:{secret_code},Vlozeny kod :{inserted_code}")
        black = 0
        white = 0
        digits_rest = self.DIGIT_NO
        new_iteration = True
        while (new_iteration):
            new_iteration = False
            for pointer in range(0, digits_rest):
                if secret_code[pointer] == inserted_code[pointer]:
                    black += 1
                    del (secret_code[pointer])
                    del (inserted_code[pointer])
                    digits_rest = len(inserted_code)
                    new_iteration = True
                    break;
        # print(black)
        new_iteration = True

        while (new_iteration):
            new_iteration = False
            for pointer in range(0, digits_rest):
                if new_iteration:
                    break
                for pointer2 in range(0, digits_rest):
                    if secret_code[pointer] == inserted_code[pointer2]:
                        white += 1
                        del (secret_code[pointer])
                        del (inserted_code[pointer2])

                        digits_rest = len(inserted_code)
                        new_iteration = True
                        break
        self.single_attempt.update({"black_s": black})
        self.single_attempt.update({"white_s": white})
        print(f"jednotlivy pokus:{self.single_attempt}")

@app.route("/")
def dummy_api():




    game_code = str(request.args.get("uuid"))
    game_code= game_code.lower()
    if game_code=="new_game":
        game_uuid = uuid.uuid4()
        game_uuid = str(game_uuid)
        game_uuid = game_uuid[:8]
        my_game=GameZone()
        # only for tests
        #my_game.evaluate_attempt(0,"53421")
        my_game.insert_uuid(game_uuid)
        my_game.random_code_generator()
        secret_code=my_game.print_random_code()
        game_active.append(my_game)
        return my_game.uuid
    else:
        print(game_active)
        game_activated = False
        for game in game_active :
            # print(game.uuid , game_code)
            if game.uuid == game_code:
                active_game = game
                game_activated = True
        if game_activated:
            att = int(request.args.get("att"))
            inserted_code = str(request.args.get("c"))

            active_game.evaluate_attempt(game.current_att,inserted_code)
            print (active_game.uuid, active_game.single_attempt)

            return "hra nalezena"

        else:
            return "neplatny kod!"
        #
        #return "ahoj michale."



if __name__ == "__main__":
    app.run()