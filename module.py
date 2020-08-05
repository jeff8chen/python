#math, random, statistics
import math, random
import statistics as stat
alist =[1,2,3,4,5,6,7,8,9]
x =6.6
print(f"{x} ceiling={math.ceil(x)}")
print(f"{x} floor={math.floor(x)}")
x=12
y=32
print(f"gcd({x},{y}) ={math.gcd(x,y)}")
print(f"fmod({y},{x})={math.fmod(y,x)}")

print(f"1 to 100 random number = {round(random.random()*100)}")
print(f"another way to create random number = {random.randint(1,100)} ")
print(f"select a value from a list: {random.choice(alist)}")
print(f"a list before shuffle:")
print(alist)
random.shuffle(alist)
print(f"the list after shuffle:")
print(alist)
random.shuffle(alist)
print(f"the list after another shuffle:")
print(alist)

print("a few stats about the list:")
print(f"mean={stat.mean(alist)}, median={stat.median(alist)}, median_low={stat.median_low(alist)}")
print(f"stdev={stat.stdev(alist)}, variance={stat.variance(alist)}")

from datetime import timedelta, date, time, datetime
print("\nstarting theh module datetime...")
dt = timedelta(days=50, seconds=20, microseconds=10, milliseconds =100, minutes=10, hours=0, weeks=0)
print(dt) #50 days, 0:10:20.100010
dt =timedelta(microseconds=-1)
print(f"days={dt.days}, seconds={dt.seconds}, microseconds={dt.microseconds}")

dt = date(2020, 1, 23)
print(f"the designated date is {dt}")
dt = date.today()
print(f"today is {dt}")
dt = dt - timedelta(days=3)
print(f"three days ago is {dt}")
print(f"iso format is {dt.isoformat()}")
print(f"mm/dd/yy format is {dt.strftime('%m/%d/%y')}")
print(f"mm/dd/yyyy format is {dt.strftime('%m/%d/%Y')}")





# the module file to handle the business logical.
#import io
