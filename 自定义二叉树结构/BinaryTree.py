class BinaryTree:
	def __init__(self,value):
		self._left = None
		self._right = None
		self._data = value

	def insertLeftChild(self,value): # 创建左子树
