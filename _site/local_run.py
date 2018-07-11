import subprocess, os


# 启动本地服务
print(os.getcwd(), 'http://local:4000')
subprocess.run(['bundle', 'exec', 'jekyll', 'server'])
