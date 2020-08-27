from flask import Flask, jsonify
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

@app.route ('/covid')
def tracker():
      data = dict(
            newcses=145,
            total=954,
            recvrd=625,
            actvcses=160,
            totald=24)
      return jsonify(data)
