FROM python:3.6-alpine
WORKDIR /app
COPY . /app
ENV NAME World
ENV TZ Asia/Shanghai
RUN apk add --no-cache tzdata

# Run app.py when the container launches
CMD ["python", "app.py"]