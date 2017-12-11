from flask import Flask, jsonify
from clv_prediction import CLVPrediction
import json

app = Flask(__name__)


@app.route("/")
def read_model():
    return 'GET: /v1/clv/{customer_id}'


@app.route("/v1/clv/<customer_id>")
def read_customer_clv(customer_id):
    response = {}
    try:
        clv = CLVPrediction.find_by_customer_id(customer_id)
        if len(clv) > 0:
            response['data'] = clv[0]
        else:
            response['error'] = 'invalid customer id %s' % customer_id
    except Exception as e:
        response['error'] = '%s' % e

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)