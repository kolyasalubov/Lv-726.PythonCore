python_philosofy = '''The Zen of Python, by Tim Peters
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
20.Beautiful is better than ugly.
21.Explicit is better than implicit.
22.Simple is better than complex.
23.Complex is better than complicated.
24.Flat is better than nested.
25.Sparse is better than dense.
26.Readability counts.
27.Special cases aren't special enough to break the rules.
28.Although practicality beats purity.
29.Errors should never pass silently.
30.Unless explicitly silenced.
31.In the face of ambiguity, refuse the temptation to guess.
32.There should be one-- and preferably only one --obvious way to do it.
33.Although that way may not be obvious at first unless you're Dutch.
34.Now is better than never.
35.Although never is often better than *right* now.
36.If the implementation is hard to explain, it's a bad idea.
37.If the implementation is easy to explain, it may be a good idea.
38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
39.Explicit is better than implicit.
40.Simple is better than complex.
41.Complex is better than complicated.
42.Flat is better than nested.
43.Sparse is better than dense.
44.Readability counts.
45.Special cases aren't special enough to break the rules.
46.Although practicality beats purity.
47.Errors should never pass silently.
48.Unless explicitly silenced.
49.In the face of ambiguity, refuse the temptation to guess.
50.There should be one-- and preferably only one --obvious way to do it.
51.Although that way may not be obvious at first unless you're Dutch.
52.Now is better than never.
53.Although never is often better than *right* now.
54.If the implementation is hard to explain, it's a bad idea.
55.If the implementation is easy to explain, it may be a good idea.
56.Namespaces are one honking great idea -- let's do more of those!'''

# counting number of occurence of word: 'better' in python philosofy
print ('Number of occurence of "better" in python philosofy:', python_philosofy.find('better'))

# counting number of occurence of word: 'never' in python philosofy
print ('Number of occurence of "never" in python philosofy:', python_philosofy.count('never'))

# counting number of occurence of word: 'is' in python philosofy
print ('Number of occurence of "is" in python philosofy:', python_philosofy.count('is'))



# outputing python philosofy in uppercase
print('Python philosofy in UPPERCASE: \n', python_philosofy.upper())



# replacing char 'i' to '&' in python philosofy
print(python_philosofy.replace('i', '&'))



# input four-digits number
some_number = input('Input some four-digits number = ')



# find the product of the digits of this number.
multi_number = 1
for element in some_number:
    multi_number *= int(element)

print('The product of the digits of this number = ', multi_number)



# output the number in reverse order
print('Number in reverse order = ', some_number[::-1])



# output sorted number
sorted_some_number = sorted(some_number)
print('Sorted number =', ''.join(sorted_some_number))



# exchange of variable values
some_value1 = 555
print('1-st variable = ', some_value1)
some_value2 = "data"
print('2-d variable = ', some_value2)

some_value1, some_value2 = some_value2, some_value1

print(f'After swaping 1-st variable = {some_value1}, and 2-d variable = {some_value2}')
