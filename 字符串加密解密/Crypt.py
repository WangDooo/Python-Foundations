def crypt(source, key):
	from itertools import cycle
	result = ''
	temp = cycle(key) # cycle('abc') 重复序列的元素，既a, b, c, a, b, c ...
	for ch in source:
		result = result + chr(ord(ch) ^ ord(next(temp))) # ord('a')=97 chr(97)='a' next() 返回迭代器的下一个项目
		# ^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
	return result

source = 'WangDoo asd utututut'
key = '1'
print('Before :'+source)
encrypted = crypt(source, key)
print('After :'+encrypted)
decrypted = crypt(encrypted,key)
print('还原 :'+decrypted)	