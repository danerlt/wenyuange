#! /bin/bash

pwd=$(PWD)
script_path=$(dirname "$pwd")
data_path="$script_path/data"
mysql_data_path="$data_path/mysql"

docker run  -d  \
--name wenyuan_mysql \
--privileged=true \
--restart=always \
-p 30306:3306 \
-v "$mysql_data_path":/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=123456 \
mysql:8.0 \
--lower_case_table_names=1

