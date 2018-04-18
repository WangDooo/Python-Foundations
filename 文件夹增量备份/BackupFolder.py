import os
import filecmp
import shutil
import sys

def autoBackup(scrDir, dstDir):
	
	pass

def usage():
	print('scrDir and dstDir must be existing absolute path of certain directory')
	sys.exit(0)

if __name__ == '__main__':
	scrDir = 'D:\Coding\GitHub\Python-Foundations\文件夹增量备份\main'
	dstDir = 'D:\Coding\GitHub\Python-Foundations\文件夹增量备份\backup'
	autoBackup(scrDir,dstDir)