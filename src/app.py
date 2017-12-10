from flask import Flask
import dill as pickle
import os  
import numpy as np

app = Flask(__name__)



@app.route("/")
def read_model():
	try:
		with open("resource/model.dill", 'rb') as file:
			model = pickle.load(file)
	except Exception as e:
		raise e

	return "hey"

@app.route("/v1/data")
def read_dataset():
	try:
		data = np.genfromtxt('resource/orders.csv', delimiter=',')
	except Exception as e:
		raise e
	
	return data



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)