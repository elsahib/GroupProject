from application import app
import random, requests
from flask import request, Response, jsonify
from requests.exceptions import ConnectionError

@app.route('/home', methods =['GET','Post'] )
def prize():
    try:    
        reqnum= requests.get('http://numgen:8000/num') # request to num gen
        n = str(reqnum.text)
        reqtext= requests.get('http://txtgen:8000/text')  # request to sring gen
        s = str(reqtext.text)
    except ConnectionError:
        s = 'zzz'
        n = '000000'

    stakes = random.randint(1,100)
    prize = 0
    if s[0] == 'A':
        if stakes in range(1,26):
            prize = 200
        elif stakes in range(26,101):
            prize = 100
        else:
            prize = random.randint(50,100)
    elif s+n == 'zzz000000':
        prize = 0
    else:
        prize = random.randint(50,100)
    return jsonify({"code":s+n,"prize":prize})

