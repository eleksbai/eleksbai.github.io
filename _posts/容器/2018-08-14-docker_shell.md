---
layout: default
title: 容器命令大全
date:   2018-08-14 16:16:01 
categories: docker
---
# docker 和 docker-compose 安装
docker 安装

[docker安装官网文档](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
~~~
暂略
~~~

docker-compose 安装
~~~
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
~~~

# 容器基本命令

### 进入现有容器

代码示例

[参考链接](https://stackoverflow.com/questions/30172605/how-to-get-into-a-docker-container)

~~~sh
# 打开一个现在正在运行的容器
sudo docker exec -t -i container_name /bin/bash 

# 创建一个现有容器并链接
sudo docker run --name t1 -it --entrypoint /bin/bash  python #python为镜像名

# Alpine 是专为容器设计的轻量镜像
# 以Alpine为基础构建的镜像中没有bash
sudo docker run --rm -it --entrypoint sh python
~~~


### docker-compose 命令

docker-compose 相关命令需要在含有docker-compose.yaml文件的路径下运行
~~~
# 项目创建及更新 -d 后台运行
sudo docker-compose up -d

# 项目重新构建镜像
sudo docker-compose up --build

# 运行一次性命令 查看web服务的环境变量
sudo docker-compose run web env

# 停止服务
sudo docker-compose stop

# 删除服务及数据卷
sudo docker-compose down --volumes

# 如果容器已存在则不会重新创建
sudo docker-compose up -d --no-recreate
~~~

# 应用篇 

### 使用 docker-compose 进行容器部署

本地环境快速部署 mysql redis rabbitmq

docker-compose.yaml 
注 3.2才支持使用volumes表达mount bind
~~~yaml
version: '3.2'
services:
  redis:
    image: "redis"
    restart: always
    ports:
    - "6379:6379"
    volumes:
      - type: bind
        source: /home/ubuntu/redis-data
        target: /data
    environment:
    - HELLO=hyman
    command: redis-server --appendonly yes

  mysql:
    image: "mysql:5.7"
    restart: always
    ports:
    - "3306:3306"
    environment:
    - MYSQL_ROOT_PASSWORD=123456

  rabbitmq:
    image: "rabbitmq:3-management"
    restart: always
    ports:
    - "5672:5672"
    - "15672:15672"
~~~

### redis容器应用

代码示例
~~~
# 更换绑定方式（成功） 用iptables 外网访问保证安全
docker run -p 6379:6379 --name myredis --restart always --mount type=bind,src=/home/ubuntu/redis-data,dst=/data -d redis redis-server --appendonly yes 

~~~

### mysql容器应用

代码示例
~~~
sudo docker run --restart always --name my-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7

~~~
