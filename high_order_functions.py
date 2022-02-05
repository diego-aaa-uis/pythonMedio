#Filter, map y reduce
# Funcion que recibe como parámetro a otra función

#filter
from functools import reduce
my_list = [1, 4, 5, 6, 9, 13, 19, 21]

"""odd = [i for i in my_list if i%2!=0]

print(odd)"""

odd = list(filter(lambda x : x%2 !=0, my_list))
print(odd)

my_list2= [1,2,3,4,5]

square = list(map(lambda x: x**2,my_list2))
print(square)

#REDUCE

my_list3 = [2,2,2,2,2]
reduceList = reduce(lambda a,b: a*b ,my_list3)

print(reduceList)