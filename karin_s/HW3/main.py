
# вивести текст Zen of Python у верхньому регістрі

zen = '''1.Beautiful is better than ugly.
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
15.Now is better than never.'''

big_letters = (f"{zen.upper()}")
print (big_letters)


#кількість входжень слів (better, never, is)

count_better = zen.count("better")
print (count_better)

count_never = zen.count("never")
print (count_never)

count_is = zen.count("is")
print (count_is )

#замінити всі входження символу “і” на “&”

change_i = zen.replace('i','&')
print (change_i)
