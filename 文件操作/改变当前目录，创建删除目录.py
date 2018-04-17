import os
os.getcwd() # 返回当前工作目录 
os.mkdir(os.getcwd()+'\\temp') # 创建目录
os.chdir(os.getcwd()+'\\temp') # 改变当前目录
os.getcwd()
os.mkdir(os.getcwd()+'\\test')
path = "/tmp/home/monthly/daily"
os.makedirs(os.getcwd()+path)
print(os.listdir('.'))
os.rmdir('test') # 删除目录