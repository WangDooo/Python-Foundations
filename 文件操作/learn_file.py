#========二进制文件操作案例精选========================================================
# 二进制文件
# Python常用的序列化模块 struct pickle json marshal shelve
#----------------------------------------------------------------

#----------------------------------------------------------------


#========pickle模块========================================================
# 进行对象序列化和二进制文件读写
#----------------------------------------------------------------
# import pickle

# f = open('sample_pickle.dat','wb')
# n = 7
# i = 123123123412
# a = 99.123
# s = '是打发阿达瓦亲'
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# tu = (-123,1,1)
# coll = {1,2,3,5}
# dic = {'a':'apple','b':'banana','c':'ccacasc'}
# try:
# 	pickle.dump(n,f)
# 	pickle.dump(i,f)
# 	pickle.dump(a,f)
# 	pickle.dump(s,f)
# 	pickle.dump(lst,f)
# 	pickle.dump(tu,f)
# 	pickle.dump(coll,f)
# 	pickle.dump(dic,f)
# except:
# 	print('写文件异常')
# finally:
# 	f.close()

# import pickle

# f = open('sample_pickle.dat','rb')
# n = pickle.load(f) # 读出文件的数据个数
# i = 0
# while i < n:
# 	x = pickle.load(f)
# 	print(x)
# 	i += 1
# f.close()

#----------------------------------------------------------------


#=========struct模块=======================================================
# 对二进制文件进行读写
#----------------------------------------------------------------
# import struct

# n = 123123123
# x =123.12312
# b = True
# s = 'a1@ sd大师的范范'
# sn = struct.pack('if? ',n,x,b)
# f = open('sample_struct.dat','wb')
# f.write(sn)
# f.write(s.encode())
# f.close()

# import struct

# f = open('sample_struct.dat','rb')
# sn = f.read(9)
# tu = struct.unpack('if? ',sn)
# print(tu)
# n,x,b1 = tu
# print('n=',n,'x=',x,'b1=',b1)
# s = f.read(9)
# s = s.decode()
# print('s=',s)

#----------------------------------------------------------------


#=========文件级操作=======================================================
# 处理文件路径 os.path
# 使用命令行读取文件内容 fileinput模块
# 创建临时文件和文件夹 tempfile模块
# 处理文件系统路径 pathlib模块
#----------------------------------------------------------------

#----------------------------------------------------------------



#=======os与os.path模块=========================================================
# os模块
# remove(path) 删除指定文件
# rename(src,dst)
# listdir(path) 返回path目录下的文件和目录列表
# os.path模块
#----------------------------------------------------------------
# import os
# import os.path

# print(os.path.exists('test1.txt'))
# # os.rename('test1.txt','rename.txt')
# os.rename('test1.txt','./filetxt/rename.txt') # os.rename()可以实现文件的改名和移动
#----------------------------------------------------------------


#=========目录操作=======================================================
# mkdir(path) 创建目录
# makedirs(path1/path2...)
# rmdir(path) 删除目录
# removedirs(path1/path2...)
# listdir(path) ls
# getcwd() 返回当前工作目录
# get_exec_path() 返回可执行文件的搜索路径
# chdir(path) cd
# walk(top,topdown=True,onerror=None) 遍历目录树,该方法返回一个元组,包含三个元素：
# 所有路径名、所有目录列表、文件列表
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------