#знайти добуток цифр заданого числа

a = input("Enter 4th number:")
b = int(a[0])
c = int(a[1])
d = int(a[2])
f = int(a[3])

print (b*c*d*f)

#записати число в реверсному порядку

a = input("Enter your number:")
b = list(reversed(a))
b = ''.join(b)
print (b)


#посортувати цифри, що входять в дане число

a = input("Enter your number:")
b = list(a)
c = b.sort()
d = ''.join(b)
print (d)



