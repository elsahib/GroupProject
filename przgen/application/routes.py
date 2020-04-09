from application import app
import random, requests
from flask import request, Response, jsonify

@app.route('/home', methods =['GET','Post'] )
def prize():

    reqnum= requests.get('http://localhost:5002/num')# request to num gen
    n = str(reqnum.text)
    reqtext= requests.get('http://localhost:5001/text') # request to sring gen
    s = str(reqtext.text)
    stakes = random.randint(1,100)
    prize = 0
    if s[0] == 'a':
        if stakes in range(1,76):
            prize = 100
    else:
        prize = 50
    return jsonify({"code":s+n,"prize":prize})
    #return Response('your code ' + s + str(n) +  ' Won you ' + str(prize) + '£', mimetype='text/plain')

