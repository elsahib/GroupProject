from application import app
from flask import request, Response
import string, random


@app.route('/text', methods =['GET'] )
def text():
    result= ''.join(random.choices(string.ascii_lowercase, k=3))
    

    return Response(result, mimetype='text/plain')