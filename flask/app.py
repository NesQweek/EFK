from flask import Flask, Response

app = Flask(__name__)

@app.route('/one')
def one():
    return Response('one', status=201)

@app.route('/two')
def two():
    return Response('two', status=202)

@app.route('/three')
def three():
    return Response('three', status=203)

@app.route('/four')
def four():
    return Response('four', status=204)

@app.route('/five')
def five():
    return Response('five', status=205)

@app.route('/error')
def error():
    return Response('error', status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
