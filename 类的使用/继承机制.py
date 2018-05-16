# 设计Person类 为父类， 派生Teacher类

class Person(object): # 必须以object为基类
	def __init__(self, name='', age=20, sex='man'):
		self.setName(name)
		self.setAge(age)
		self.setSex(sex)

	def setName(self, name):
		if not isinstance(name, str):
			print("Name must be string!")
			return
		self.__name = name

	def setAge(self, age):
		if not isinstance(age, int):
			print("Age must be integer!")
			return
		self.__age = age

	def setSex(self, sex):
		if sex != 'man' and sex != 'woman':
			print("Sex must be 'man' or 'woman'")
			return
		self.__sex = sex

	def show(self):
		print('Name:', self.__name)
		print('Age:', self.__age)
		print('Sex:', self.__sex)

class Teacher(Person): # 子类
	def __init__(self, name='', age=30, sex='man', department='Computer'):
		super(Teacher, self).__init__(name, age, sex)
		# Person.__init__(self, name, age, sex)
		self.setDepartment(department)

	def setDepartment(self, department):
		if not isinstance(department, str):
			print('Department must be a string!')
			return
		self.__department = department

	def show(self):
		Person.show(self)
		# super(Teacher, self).show()
		print('Department:', self.__department)

if __name__ == '__main__':
	zhangsan = Person('Zhang San', 19, 'man')
	zhangsan.show()
	lisi = Teacher('李四', 32, 'woman', 'Civil')
	lisi.show()
	lisi.setAge(55)
	lisi.show()
