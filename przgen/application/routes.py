from application import app
import random, requests
from flask import request, Response, jsonify

@app.route('/home', methods =['GET','Post'] )
def prize():

    reqnum= requests.get('http://numgen:8000/num')# request to num gen
    n = str(reqnum.text)
    reqtext= requests.get('http://txtgen:8000/text') # request to sring gen
    s = str(reqtext.text)
    stakes = random.randint(1,100)
    prize = 0
    if s[0] == 'a':
        if stakes in range(1,26):
            prize = 100
        elif stakes in range(26,101):
            prize = 50
        else:
            prize = random.randint(1,50)
    else:
        prize = random.randint(1,50)
    return jsonify({"code":s+n,"prize":prize})

