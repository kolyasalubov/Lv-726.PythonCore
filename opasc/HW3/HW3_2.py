originalNumber = input("Enter 4-th number:")

originalList = list(originalNumber)

mulsum = int(originalList[0]) * int(originalList[1]) * int(originalList[2]) * int(originalList[3])

originalList.reverse()
oriRevers = ''.join(originalList)

originalList.sort()
oriSort = ''.join(originalList)

print(f"Your number: {originalNumber}",
      f"Dobudok: {mulsum}",
      f"Revers number: {oriRevers}",
      f"Sort number: {oriSort}",
      sep='\n')