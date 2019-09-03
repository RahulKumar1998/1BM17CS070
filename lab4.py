import sys
class Student:
	def __init__(self):
		self.studentId=None
		self.age=None
		self.marks=None
	def validate_marks(self):
		if self.marks in range(0,101):
			return True
		else:
			return False
	def validate_age(self):
		if self.age>20:
			return True
		else:
			return False
	def setter(self):
		self.studentId=(input("Enter the id:"))
		self.age=int(input("Enter the age:"))
		self.marks=int(input("Enter the marks:"))
	def getter(self):
		print("Student Id:",self.studentId)
		print("Student Age:",self.age)
		print("Student marks:",self.marks)
	def check_qualification(self):
		if self.validate_marks() and self.validate_age():
			if self.marks>64:
				return True
			else:
				return False
		else:
			return False
s1=Student()
s1.setter()
if s1.check_qualification():
	s1.getter()
	print("Student's admission approved! :)")
else:
	s1.getter()
	print("Student's admission disapproved :(")
