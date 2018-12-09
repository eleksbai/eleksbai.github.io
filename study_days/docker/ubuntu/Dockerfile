FROM ubuntu

RUN apt update && apt install -y tzdata
ENV TZ Asia/Shanghai
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /app
COPY . /app

ENV NAME World

# Run app.py when the container launches
