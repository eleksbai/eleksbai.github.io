时区设置
ENV TZ=Asia/Shanghai

ubuntu

aphine 

docker build -t t-u /home/hyman/eleksbai.github.io/study_days/docker/ubuntu
docker build -t t-a /home/hyman/eleksbai.github.io/study_days/docker/alpine

docker run --entrypoint /bin/sh -it t-a
docker run --entrypoint /bin/bash -it t-s

# tzdata 设置时区
dpkg-reconfigure tzdata