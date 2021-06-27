from flask import Flask, jsonify, request


import datetime
from random import choice, randrange, getrandbits
from datetime import timedelta, date
from random import shuffle
from dateutil.relativedelta import relativedelta
import os
from radar import random_datetime

FEMALE = True
MALE = False

app = Flask(__name__)

@app.route("/")
def dummy_api():
    person = {}
    age_max=99
    age_min=1
    gender=MALE

    count=int(request.args.get("att"))
    gender2=str(request.args.get("uuid"))
    gender2=gender2.upper()
    if gender2=="FEMALE":
        gender=FEMALE


    return jsonify(human_list)


if __name__ == "__main__":
    app.run()