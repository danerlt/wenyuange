#! /bin/bash

# 当前文件所在的目录
current_path=$(
  cd "$(dirname "$0")"
  pwd
)
echo "current pah is $current_path"
src_path=$(dirname "$current_path")
echo "src_path is $src_path"
root_path=$(dirname "$src_path")
echo "root_path is $root_path"

# 配置项
# MySQL 容器名
container_name="wenyuange_mysql"
# db对应的目录
db_path="$root_path/data/db"
# MySQL 挂载的目录
mysql_mount_path="$db_path/mysql"
# MySQL root密码
mysql_pass="123456"
# MySQL 容器映射到本地的端口
mysql_port="30306"

echo "mysql_mount_path is $mysql_mount_path"
if [ ! -d "$mysql_mount_path" ]; then
  mkdir -p "$mysql_mount_path"
fi

if docker inspect ${container_name} --format "{{.Name}}" | grep "/${container_name}"; then
  echo "docker container $container_name exist, can't create!!!"
  exit 1
else
  echo "docker container $container_name don't exist"
  ret=$(
    docker run -d \
      --name wenyuan_mysql \
      --privileged=true \
      --restart=always \
      -p $mysql_port:3306 \
      -v "$mysql_mount_path":/var/lib/mysql \
      -e MYSQL_ROOT_PASSWORD=$mysql_pass \
      mysql:8.0 \
      --lower_case_table_names=1 \
      --character-set-server=utf8mb4 \
      --collation-server=utf8mb4_unicode_ci \
      --skip-character-set-client-handshake \
      2 >/dev/null
  )
  if [ "$ret" == "0" ]; then
    echo "start container $container_name success"
  else
    echo "start container $container_name filure, return code is $ret"
  fi
fi
