from flask import Flask, jsonify, request
import uuid

import datetime
from random import choice, randrange, getrandbits, shuffle
from datetime import timedelta, date

app = Flask(__name__)

@app.route("/")
def dummy_api():
    person = {}


    #code = str(request.args.get("code"))
    code="new_game"
    code= code.lower()
    if code=="new_game":
        game_uuid = uuid.uuid4()
        game_uuid = str(game_uuid)
        game_uuid = game_uuid[:8]
        return game_uuid
    else:
        return "ahoj michale."

    return jsonify(human_list)


if __name__ == "__main__":
    app.run()