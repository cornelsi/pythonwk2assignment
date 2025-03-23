#question 1. Create an empty list called my_list
my_list=[]

#question 2.Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# print(my_list)

#question 3.Insert the value 15 at the second position in the list.
my_list.insert(1,15)
# print(my_list)

#question 4. Extend my_list with another list: [50, 60, 70]
anotherlist=[50,60,70]
my_list.extend(anotherlist)
# print(my_list)

#question 5. Remove the last element from my_list.
del my_list [-1]
#print(my_list)

#question 6. Sort my_list in ascending order.
my_list.sort()
# print(my_list)

#question 6. Find and print the index of the value 30 in my_list
if 30 in my_list:
   print(my_list.index(30))

