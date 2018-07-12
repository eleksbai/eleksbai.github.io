import subprocess, os


# 启动本地服务
# chcp 65001
# bundle exec jekyll server
print(os.getcwd(), 'http://127.0.0.1:4000/')
subprocess.run(['bundle', 'exec', 'jekyll', 'server'])
