import os
from flask import Flask, jsonify
from db_controller import DbController
from clv_prediction import CLVPrediction

app = Flask(__name__)


@app.route("/")
def read_model():
    return 'GET: /v1/clv/{customer_id}' \
           ' <br> ' \
           '/v1/total'


@app.route("/v1/total")
def read_total():
    response = {}
    try:
        db_object = DbController()
        query = "SELECT COUNT(*) as total FROM tbl_clv_prediction"
        data = db_object.execute_select(query)
        response["data"] = data[0]
    except Exception as e:
        response['error'] = '%s' % e

    return jsonify(response)


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
    port = os.getenv('PORT', 5000)
    host = os.getenv('HOST', '0.0.0.0')
    app.run(debug=False, host=host, port=int(port))
