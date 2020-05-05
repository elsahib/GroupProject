from application import app
from flask import request, Response
import string, random


@app.route('/num', methods =['GET'] )
def num():
    result = ''.join(random.choices(string.digits, k = 6))

    return Response(result, mimetype='text/plain')
