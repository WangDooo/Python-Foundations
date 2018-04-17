import os 

def visitDir2(path):
	if not os.path.isdir(path):
		print('Error:'.path,'is not a directory or does not exist.')
		return
	list_dirs = os.walk(path)
	for root, dirs, files in list_dirs: # 遍历该元组的目录和文件
		for d in dirs:
			print(os.path.join(root,d))
		for f in files:
			print(os.path.join(root,f))

path='D:\Coding\GitHub\Python-Foundations\文件操作'
visitDir2(path)
