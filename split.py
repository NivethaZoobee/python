import copy
import random

ph='91-9962512345'
list=ph.split("-",2)
print(list[1])

a=ph[:2]+'-'+ph[2:]
print(a)

b=ph.replace("-","")
print(b)

ph1="1800 123 4567"
c=ph1.replace(" ","")
print(c)

st="hello world"
li=st.split(" ")
print("".join(li))

ip="10.2753.24.1"
s=ip.split(".")
print(s)
k=0
for i in s:
    if int(i) not in range(0,256):
        k=1
        print("invalid ip address")
        break
if k==0:
    print("valid ip address")
    
lst1=[5,11,12,6,7]
lst1.sort()
print(lst1)

print(lst1.pop())
print(lst1.pop(2))
print(lst1)
lst1.remove(5)
print(lst1)
lst1=[10,20,30]
lst2=[40,50,60]
print(lst1+lst2)
print(lst1[-1])
print(lst1*3)
print(30 in lst1)
print(30 not in lst1)
for num in lst1:
    print(num,end=" ")

lst3=lst1[:]
print(lst3)

#lst4=list("lst1")
#print(lst4)

lst5=copy.copy(lst1)
print(lst5)

for num in lst1:
    print(num**2)
res=[num**3 for num in lst1]
print(res)

lst1=[1,2,3]
print(lst1)
lst7=[elem for elem in lst1]#copy
print(lst7)

lst8=[[1,2],3,4]# nested list
print(lst8[0])
print(lst8[0][0])
print(lst8[0][1])
lst8[0][0]=100#value can be changed#shallow copy
print(lst8)
lst9=copy.deepcopy(lst8)#deep copy
print(lst9)

tup=(1,2,False,'abc')
print(type(tup))
print(tup.count(1))
print(tup.count('1'))
print(tup[1:])
for elem in tup:
    print(elem)
    print(tup)
#tup2()#empty tuple
#tup3(10,)#tuple with single element
#indexing and slicing in tuple
colors=('white','red','green')
print('white' in colors)

#dictionaries
emp={
    "name":"nivetha",   #creating a dictionary
    'age':'25',
    'salary':'20000'
    }
print(emp)
print(emp.get("name"))  #printing specific element
emp['age']=24           # changing the value
print(emp)
for key in emp.keys():
    print(emp[key])

for key,value in emp.items():
    print(key,value)

#Set

colors={'pink','yellow','green'}
print(colors)

#type conversions

print(int('10'))
#### ord,chr(char to int)(int to char)
#### hex,oct(int to hex)(int to oct)
#### tuple(),list(),set(),dict()
#eg:tuple(['a','b'])
#list(('a','b'))
#set(['a','b','a'])
#dict((('id',10001),('name','nivetha')))

#if-else

num=int(input("enter the no"))
if num %2==0:
    print("even".format(num))
else:
    print("odd")
    
#if-elif-else

num=int(input("enter the no"))
if num<10:
    print("<10")
elif num>10:
    print(">10")
else:
    print("=10")

#Shorthand if,if-else and multiple else statements

if(7>5):print("7>5")
print(7)if 7>5 else print(5)
print(7) if 7>5 else print(5) if(4==4) else print(4)
 #logical and & or statements
a=int(input("enter the num"))
b=int(input("enter the num"))
c=int(input("enter the num"))
d=int(input("enter the num"))
if a>b and c==d:
    print("logical")
#looping

for i in range(10):
    print()
    for j in range(i):
        print(j,end='')
for i in range(10):
    print()
    for j in range(i):
        print('*',end='')

#for-else
for val in range(5):
    print(val)
else:
    print("for loop exhausted without any break")
#while[tables]
i=1
j=9
num=int(input("enter a num"))
while(i<=j):
    print("{}*{}={}".format(num,i,num*i))
    i=i+1
    
num=int(input("enter a num"))
for i in range(1,10):
     print("{}*{}={}".format(num,i,num*i))

    
#pass
for val in range(5):
    if(val==3):
        pass
    print(val)

lst1=[10,['user1','user2'],10.25,('test1','test2'),True]
print(lst1)

for i in range(5,0,-1):
    print()
    for j in range(i):
        print('*',end='')


for i in range(1,6):
    print()
    for j in range(i):
        print(   '*',end='')
print()       
print()

size = 10
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
        
    
for i in range(1,7):
    str1='* '*i
    print(str1.center(14))

movies=["A","B","C"]
years=[1975,1979,1980]
lst=[]
for i in movies:
    for j in years:
        if movies.index(i)==years.index(j):
            lst.append(i+str(j))
print(lst)           
        

cp=650
dis=cp*0.4
n=25
cost1=(cp-dis)+30
cost2=((cp-dis)+15)*24
cost=cost1+cost2
print(cost) 

name=input("Hello! Enter yout name")
print("well {}, I am thinking a number between 1 to 10".format(name))
num=random.randint(1,10)
for i in range(1,6):
    print("take a guess")
    gue=int(input())
    if gue<num:
        print("too low")
        continue
    elif gue>num:
        print("too high")
        continue
    else:
        print("equal")
        break
else:
    print("the number is {}".format(num))

def leaf(year):
    if (year % 4) == 0:  
       if (year % 100) == 0:  
           if (year % 400) == 0:  
               print("{0} is a leap year".format(year))  
           else:  
               print("{0} is not a leap year".format(year))
       else:
            print("{0} is a leap year".format(year))  
    else:
        print("{0} is not a leap year".format(year))  

year=int(input())
leaf(year)
