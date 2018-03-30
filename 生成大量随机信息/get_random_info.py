import random
import string
import codecs  # 做中文utf8编码处理

StringBase = "中石化表示，公司注重发展质量和效益，持续优化原料、产品结构，增产市场需求旺盛的高附加值产品，炼油和化工业绩双创历史新高。炼油板块经营收益为650亿元，同比增长15.5%；化工板块实现经营收益为270亿元，同比增长30.8%"
# StringBase = ''.join(StringBase.split('，'))
def getEmail():
	suffix = ['.com','.org','.net','.cn']
	# string.ascii_letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
	# string.digits = 0123456789
	characters = string.ascii_letters + string.digits + ' '
	# random.randint(a,b) 取a~b中的随机数
	# random.choice() 选一个
	username = ''.join((random.choice(characters) for i in range(random.randint(6,12))))
	domain = ''.join((random.choice(characters) for i in range(random.randint(3,6))))
	return username+'@'+domain+random.choice(suffix)

def getTelNo():
	return '1'+''.join((str(random.randint(0,9)) for i in range(10)))

def getNameOrAddress(flag):
	'''flag=1 返回随机姓名 flag=0 返回随机地址'''
	result = ''
	if flag == 1:
		rangestart, rangeend = 2, 5 # 姓名在2~4个汉字
	elif flag == 0:
		rangestart, rangeend = 10, 31 # 地址在10~30个汉字
	else:
		print('flag must be 1 or 0')
		return ''
	for i in range(rangestart,rangeend):
		result += random.choice(StringBase)
	return result

def getSex():
	return random.choice(('男','女'))

def getAge():
	return str(random.randint(18,100))

def main(filename):
	with codecs.open(filename,'w','utf-8') as fp:
		fp.write('Name, Sex, Age, TelNo, Address, Email\n')
		# 随机生成200人信息
		for i in range(200):
			name = getNameOrAddress(1)
			sex = getSex()
			age = getAge()
			tel = getTelNo()
			address = getNameOrAddress(0)
			email = getEmail()
			line = name+','+sex+','+age+','+tel+','+address+','+email+'\n'
			fp.write(line)

if __name__ == '__main__':
	filename = 'random_info.txt'
	main(filename)
