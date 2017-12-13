# Customer​ ​Lifetime​ ​Value​ ​Project

Determine Customer​ ​lifetime​ ​value​ ​(CLV)​ ​--​ ​discounted​ ​value​ ​of​ ​future​ ​revenue​ ​generated​ ​by​ ​a
customer,​ ​is​ ​particularly​ ​important​ ​in​ ​online​ ​fashion​ ​retail,​ ​since​ ​CLV​ ​helps​ ​us​ ​make
important​ ​business​ ​decisions​ ​about​ ​sales,​ ​marketing,​ ​product​ ​development,​ ​and
customer​ ​support.​ ​Now,​ ​you​ ​are​ ​collaborating​ ​with​ ​Lesara​ ​data​ ​scientists​ ​to​ ​work​ ​on​ ​a
project,​ ​which​ ​predicts​ ​the​ ​CLV​ ​of​ ​each​ ​customer​ ​based​ ​on​ ​his/her​ ​historical​ ​orders.

## Project Setup

Manually set up MySQL database:
If you have MySQL server available, then please create database and user using below instrunctions.
```shell
CREATE USER 'ls_user'@'localhost' IDENTIFIED BY 'ls_password';
GRANT ALL PRIVILEGES ON * . * TO 'ls_user'@'localhost';
FLUSH PRIVILEGES

CREATE TABLE IF NOT EXISTS ls_db.tbl_clv_prediction (
  id INT(11) NOT NULL AUTO_INCREMENT,
  customer_id VARCHAR(45) DEFAULT NULL,
  max_number_item INT(11) NOT NULL DEFAULT 0,
  max_revenue FLOAT NOT NULL DEFAULT 0,
  total_revenue FLOAT NOT NULL DEFAULT 0,
  total_orders INT(11) NOT NULL DEFAULT 0,
  days_since_last_order INT(11) NOT NULL DEFAULT 0,
  longest_interval INT(11) NOT NULL DEFAULT 0,
  predicted_clv FLOAT NOT NULL DEFAULT 0,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

```
Or use preconfigured docker image:
Go to app folder
build
```shell
docker build -f  Dockerfile .
```
predict and run RESTful service
```shell
docker run -it <image_id>  app <num_rows>
docker run -it -p 5000:5000 88955f78d824  app 1000
```

## Getting Started

Install the project's development environment and runtime requirements:

```shell
pip3 install -r requirements.txt
```

## Configuration

If you have a different database configuration, then please edit config/config.yaml file.

## Run Applications

To start the offine predition, go to the app folder:

```shell
NUM_ROWS=1000 python3.6 api/offine_predict.py
```   
This program predicts using the model and saves in MySQL database and also exports to csv in output folder.

To check the predicted results through RESTful, please run clv_server.py

```shell
PORT=5000 python3 api/clv_server.py
```

Once the API is up, you can test the endpoints by:

```shell
curl -X GET 127.0.0.1:5000/v1/clv/<customer_id>
```


## Unittest

To run unittest, go to the `tests` folder and run
```shell
python3.6 -m unittest discover -p 'test_*.py'
```  

Currently test cases are hard coded.
