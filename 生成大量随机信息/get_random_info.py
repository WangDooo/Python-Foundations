import random
import string
import codecs

StringBase = '美国，对，中国，600亿，美元，商品，加征，关税，而，中国，的，反击，是，30亿，美元，中国的回击，偏软，了吗？高铁，装备，信息，技术，新能源，机器人，为什么，美，国专盯，中国的，高科技，过去，美国，针对中，国，启动的，301调查，已有5次，而，每一次，都以，协商，谈判，收场，那么，这一次，呢'
StringBase = ''.join(StringBase.split('，'))
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

print(getEmail())
print(getTelNo())
print(StringBase)
print(getNameOrAddress(0))