import os
import filecmp
import shutil
import sys

def autoBackup(scrDir, dstDir):
	if ((not os.path.isdir(scrDir)) or (not os.path.isdir(dstDir)) or (os.path.abspath(scrDir)!=scrDir) or (os.path.abspath(dstDir)!=dstDir)):
		usage()
	for item in os.listdir(scrDir):
		scrItem = os.path.join(scrDir, item)
		dstItem = scrItem.replace(scrDir, dstDir)
		if os.path.isdir(scrItem):
			# 创建新增的文件夹，保证目标文件夹的结构与原始文件夹一致
			if not os.path.exists(dstItem):
				os.makedirs(dstItem)
				print('make directory'+dstItem)
			autoBackup(scrItem, dstItem)
		elif os.path.isfile(scrItem):
			# 只复制新增或修改过的文件
			# filecmp.cmp(f1, f2, shallow=True) 比较文件f1和文件f2，当两个文件相同时返回True，否则返回False。 使用shallow参数可以快速地比较文件是否有修改过
			if ((not os.path.exists(dstItem)) or (not filecmp.cmp(scrItem, dstItem, shallow=False))):
				shutil.copyfile(scrItem,dstItem)
				print('file:'+scrItem+'==>'+dstItem)


	pass

def usage():
	print('scrDir and dstDir must be existing absolute path of certain directory')
	sys.exit(0)

if __name__ == '__main__':
	scrDir = 'D:\\Coding\\GitHub\\Python-Foundations\\文件夹增量备份\\main'
	dstDir = 'D:\\Coding\\GitHub\\Python-Foundations\\文件夹增量备份\\backup'
	autoBackup(scrDir,dstDir)
