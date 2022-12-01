#поміняти між собою значення двох змінних,не використовуючи третьої

a = input("Enter your 1st word:")
b = input("Enter your 2nd word:")
a,b= b,a
print ("So we've changed the order and now:\n 1st is", a, "; 2nd is",b)
