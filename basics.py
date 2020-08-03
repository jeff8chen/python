import datetime


#Hello World.
message="Hello Python World!!"
print(message)


#numbers: int(), float(), complex()
my_number =2+3**3
print(f"simple number: {my_number}")
my_number = 140_000_000_000_000
print(f"giant number: {my_number:,}")
my_number = 0.2*0.1
print(f"decimal tail: {my_number}")


#special characters
message ="It is Python's strength."
print(message)

message = 'It is Python\'n strength.\n\t1) simple, \n\t2) flexible, \n\t3) open source.'
print(message)

# string functions, str():
first_name = "john"
last_name = "smith"
print(f"{first_name} {last_name}")
print(f"{first_name.title()} {last_name.title()}")
print(f"{first_name.upper()} {last_name.upper()}")

#string format function
print('{0}{1}{0}'.format('abra', 'cad'))
print('geolocation: {lat}, {long}'.format(lat='37.24', long='-115.88'))
print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('ceter aligned'))
print('int:{0:d}, hex:{0:#x}, oct:{0:#o}, binary:{0:#b}'.format(42))
print('{:,}'.format(987612345))
print('{:.2%}'.format(19/22))
d =datetime.datetime(2020,7,4,12, 15, 50)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))


#list []
alist =[3,10,"a", "b", [1,2]]
print(f"alist size: {len(alist)}")
print(f"item2:{alist[1]}")
alist.append('xyz')
new_element =alist.pop()
print(f"new element:{new_element}")

#list comprehesnion
alist =[value*2 for value in range(1,30) if value%2==0]
temp_str=""
for a in alist:
    if temp_str =="":
        temp_str=str(a)
    else:
        temp_str = temp_str + ", " + str(a)
print("list comprehesion: " + temp_str)
list_copy= alist[:]
print(list_copy)


#string, list operators:
print("la"*5 + "robin")

colors =['red', 'blue', 'green', 'orange', 'purple']
print(colors[0:3])
print(colors[::2])
print(colors[-3:-1])

my_str="the brown fox jumped over the lazy dog";
print(my_str[0:6])
print(my_str[::3])
print(my_str[-9:-1:2])

', '.join(colors)
'a b c'.split(' ')


#range and tuple:
d=range(1,8)
for r in d:
    print(r)

d=(9,8,7,6,5)
for r in d:
    print(r)


#dictionary:
#to store different types of inforamtion about one alien object:
alien = {'name':'alpha delta', 'height':5.6, (1,2):[[2,3],[3,4]], 'maker':{'name':'alian builder Inc.', 'built year':20202}}

#to store one type of information about different objects:
favourite_lang ={
    'jen':'python',
    'sarah':'c',
    'edward':'java',
    'phil':'python'
    }

for key in favourite_lang.keys():
    print(key)
for value in favourite_lang.values():
    print(value)
for k, v in favourite_lang.items():
   print(f"{k}:{v},")


 #functions
 #built in function examples:
print(f"my_str length: {len(my_str)}")
print(f"max value in the tuple d: {max(d)}")
print(f"sorted string:{''.join(reversed(sorted('abracadabra')))}")

#custom function examples:
def incremental(end=5, start=0):
    total=0
    while start<end:
        total = total +1
        start = start + 1
    return total

start1=3
end1=6
result = incremental(end1, start1)
print(result)
result = incremental(end1)
print(result)
result = incremental()
print(result)

def update_dict(one_dict):
    '''update the dictionary content'''
    '''similarly, function can update a list'''
    for k in one_dict.keys():
        one_dict[k] = one_dict[k] + 1

my_dict ={1:1, 2:2, 3:3}
print(my_dict)
update_dict(my_dict)
print(my_dict)

def make_pizza(size, *topping):
    '''take arbitrary number of arguments of toppings
    return it as tuple'''
    print(f"pizza size = {size}")
    print(topping)

make_pizza(12, "pepperoni", "ham")

def build_profile(**user_profile):
    '''take random number of keyword argument and value pair
    return it as an dictionary'''
    return user_profile

my_profile = build_profile(firstname="john", lastname="Smith", location="Philadelphia", state="PA")
print(my_profile)
