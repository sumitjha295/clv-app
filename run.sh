#!/bin/bash
API_DIR=/home/ls-app/app/
app=$1
num_rows=$2


if [ "$app" = "app" ]
then
    re='^[0-9]+$'
    if ! [[ $num_rows =~ $re ]] ; then
       num_rows=-1
    fi
    chown -R mysql:mysql /var/lib/mysql /var/run/mysqld && service mysql start
    echo "Please waiting predicting for $num_rows."
    #echo NUM_ROWS="$num_rows" python3 "$API_DIR"api/offline_predict.py
    NUM_ROWS="$num_rows" python3 "$API_DIR"api/offline_predict.py
    echo "Starting server"
    python3 "$API_DIR"api/clv_server.py
fi
