from flask import Flask, jsonify, request
import uuid

import datetime
from random import choice, randrange, getrandbits, shuffle
from datetime import timedelta, date

app = Flask(__name__)


@app.route("/")
def dummy_api():
    person = {}

    class GameZone:
        def __init__(self):
            self.uuid = "00000000"
            self.secret_code = [0 , 0, 0, 0, 0]
            self.current_att=0
            self.attempts=[]
            self.attempt={{"no": 0, "inserted_code": "00000000", "black_s"=0, "white_s"=0}}
            self.game_over = False
            self.code_hacked = False
            self.all_colors_quessed = False

        def random_code_generator(self):
            for digit_index in range(len(self.secret_code)):
                self.secret_code[digit_index]=randrange(1,8)
                #print (self.secret_code)
    #         a nakonec to jeste zamicham. (:-)
            shuffle(self.secret_code)
            #print(self.secret_code)

        def print_random_code(self):
            list_rand_code = [str(digit) for digit in self.secret_code]
            string_rand_code=" "
            string_rand_code = string_rand_code.join(list_rand_code)
            #print(string_rand_code)
            return string_rand_code


        def insert_uuid(self, game_uuid):
            self.uuid = game_uuid

    code = str(request.args.get("code"))
    #code="new_game"
    code= code.lower()
    if code=="new_game":
        game_uuid = uuid.uuid4()
        game_uuid = str(game_uuid)
        game_uuid = game_uuid[:8]
        my_game=GameZone()
        my_game.insert_uuid(game_uuid)
        my_game.random_code_generator()
        secret_code=my_game.print_random_code()
        print(secret_code, type(secret_code))
        return secret_code
    else:
        return "ahoj michale."



if __name__ == "__main__":
    app.run()