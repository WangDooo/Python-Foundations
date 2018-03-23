class muQueue():		
	# 构造函数，默认队列大小为10 
	def __init__(self,size=10):
		self._content = []
		self._size = size
		self._current = 0

	def setSize(self,size):
		if size < self._current:
			# 如果缩小队列，应删除后面的元素
			for i in range(size,self._current)[::-1]: #[::-1]的含义是将元组或列表的内容翻转
				del self._content[i]
			self._current = size