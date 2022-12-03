# Author: Serhii
# HW3 task 3.1

status = input ('Hey, are you ready? (yes/no):  ')
if status == 'yes':
	print ("Lets go!!!")
elif status == 'no':
	print ("You must be always ready ;)")

print("=======  Writing Zen of Python into String  =======\n")

Py_Zen ="""                Beautiful is better than ugly.
                Explicit is better than implicit.
                Simple is better than complex.
                Complex is better than complicated.
                Flat is better than nested.
                Sparse is better than dense.
                Readability counts.
                Now is better than never.
                Although never is often better than *right* now.
                If the implementation is hard to explain, it's a bad idea.
                If the implementation is easy to explain, it may be a good idea.
                Namespaces are one honking great idea -- let's do more of those!\n"""

print("Word 'better' in Zen of Python appears:", Py_Zen.count('better'), "times")
print("Word 'never' in Zen of Python appears:", Py_Zen.count('never'), "times")
print("Word 'is' in Zen of Python appears:", Py_Zen.count('is'), "times\n")

print("=======  Editing Zen of Python into Upper  =======\n")

print(Py_Zen.upper())

print("=======  Replacing 'i' symbol in Zen of Python  =======\n")

print(Py_Zen.replace('i', '&'))