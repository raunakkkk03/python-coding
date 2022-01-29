DAY 1 SESSION 1-THE FIRST BYTE 
print("3.5 * 4 / 2 - 2.5 is")        
output - 3.5 * 4 / 2 - 2.5 is

print(3.5 * 4 / 2 - 2.5 )
output-4.5

# print("3.5 * 4 / 2 - 2.5 is") 
output- nothing will print as it is an comment now

'''
for two multiple comments
we need used this bracket
'''
print('raja')
output-raja
DAY 2 SESSION 2-READING USER MIND
radius=15
area=3.14*radius*radius
print("Area is:",area)
OUTPUT-Area is: 706.5
  
  width=5.5
height=2

print("Area is",width*height)
output=Area is:11.0

  total_coins=20+10*365-52*3
print (total_coins)
output-3514
IN VARIABLE FORM ABOBE EXPRESSION
found_coins=20
magic_coins=10
stolen_coins=3
total_coins=found_coins+magic_coins*365-stolen_coins*52
print (total_coins)
output-3514
stolen_coins=2
total_coins=found_coins+magic_coins*365-stolen_coins*52
print(total_coins)
output-3566

Question is-we have given -
used a variable named miles with initial value100 Multiply miles by1.609 and assign to a variable named kilometers,display kilometers.
miles=100
kilometers=miles*1.609
print(kilometers)
output-160.9

TO TAKE INPUT FROM USER-"EVAL"
radius=eval(input("enter the radius"))
area=3.14*radius*radius
print("Area is:",area)
output-enter the radius15
Area is: 706.5

  radius=10
radius=eval(input("enter the radius"))
area=3.14*radius*radius
print("Area is:",area)
output-enter the radius20
1256.0

radius=eval(input("enter the radius"))
radius=10
area=3.14*radius*radius
print("Area is:",area)
ouput-enter the radius20
314.0
num=eval(input("enter the number"))
enter the number12
num
12
TO COMPUTE THE AVERAGE OF THREE NUMBERS BY THE INPUT USER
a=eval(input("enter the first number"))
b=eval(input("enter the second number"))
c=eval(input("enter the third number"))
avg=(a+b+c)/3
print("Avg is:",avg)
OUTPUT-
enter the first number6
enter the second number5
enter the third number11
Avg is: 7.333333333333333
TO SWAP OF TWO VARIABLES USING THIRD VARIABLE
a=10
b=20
print("before swapping")
print("a=",a,"b=",b)
c=0
c=a
a=b
b=c
print("after swapping")
print("a=",a,"b=",b)
OUTPUT-
before swapping
a= 10 b= 20
after swapping
a= 20 b= 10
TO SWAP TWO VARIABLES WITHOUT USING THIRD VARIABLE
a=10
b=20
print("before swapping")
print("a=",a,"b=",b)
a,b=b,a
print("after swapping")
print("a=",a,"b=",b)
OUTPUT-
before swapping
a= 10 b= 20
after swapping
a= 20 b= 10

TO COMPUTE THE AVERAGE OF THREE NUMBERS BY THE INPUT USER IN A SINGLE LINE
a,b,c=eval(input("enter 3 numbers separated by,"))
avg=(a+b+c)/3
print("avg is:",avg)
OUTPUT-
enter 3 numbers separated by,10,20,30
avg is: 20.0
NUMBERS REPLACED
INPUT-2/4
0.5
INPUT-2//4
0
REMOVE LAST DIGIT OF A GIVEN NUMBER
56425//10
OUPUT-5642
num=eval(input("enter the number"))
num=num//10
print("after removing last digit:",num)
OUTPUT-ENTER THE NUMBER=65423
6542
if we take an float number then
enter the number=425.6
ouput=42.0
FETCH THE LAST DIGIT
num=eval(input("enter the number"))
last=num%10
print("fetch the last digit:",last)
OUTPUT-ENTER THE NUMBER=854256
6
num=eval(input("enter the number"))
last=num%100
print("fetch the last digit:",last)
output-
enter the number256455
fetch the last digit: 55
DISTNCE BETWEEN TWO PONTS TAKING INPUT BY USER
x1,y1=eval(input("enetr x1,y1"))
x2,y2=eval(input("enter x2,y2"))
distance=((x2-x1)**2 + (y2-y1)**2)**0.5
print("distance is:",distance)
OUTPUT-
enter x1,y10,0
enter x2,y24,0
distance is: 4.0
IF-ELSE-ELIF STATEMENT
radius=eval(input("enter the radius"))
if radius>0:
    area=3.14*radius*radius
    print("area is :",area)
OUPUT-ENTER THE RADIUS=6
area is : 113.03999999999999
DIVISIBILITY BY 10 AND 5
num=eval(input("enter the number"))
if num%5==0:
    print("hifive")

if num%2==0:
    print("hieven")
OUTPUT-
enter the number25
hifive
enter the number12
hieven
enter the number10
hifive
hieven
TO CHECH NUMBER IS EVEN OR ODD
num=eval(input("enter the number"))
if num%2==0:
    print("even number")

if num%2!=0:
    print("odd number")
OUTPUT-
enter the number14
even number
enter the number23
odd number
USE ELSE STATEMENT
num=eval(input("enter the number"))
if num%2==0:
    print("even number")

else:
    print("odd number")
OUTPUT-
enter the number14
even number
enter the number23
odd number
TO FIND THE DISTANCE
x1,y1=eval(input("enter center coordinates x1,y1:"))
radius=eval(input("enter radius of circle"))
x2,y2=eval(input("enter point coordinates x2,y2:"))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
if distance>radius:
    print("outside the curcle")
else:
    print("inside the circle")
OUTPUT-
enter center coordinates x1,y1:2,1
enter radius of circle2
enter point coordinates x2,y2:3,2
inside the circle

x1,y1=eval(input("enter center coordinates x1,y1:"))
radius=eval(input("enter radius of circle"))
x2,y2=eval(input("enter point coordinates x2,y2:"))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
if distance>radius:
    print("outside the curcle")
else:
    print("inside the circle")
OUPUT-
enter center coordinates x1,y1:2,1
enter radius of circle2
enter point coordinates x2,y2:3,4
outside the curcle
USE ELIF STATEMENT
x1,y1=eval(input("enter center coordinates x1,y1:"))
radius=eval(input("enter radius of circle"))
x2,y2=eval(input("enter point coordinates x2,y2:"))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
if distance>radius:
    print("outside the curcle")
elif distance<radius:
    print("inside the circle")
else:
    print("on the circle")
OUTPUT-
enter center coordinates x1,y1:2,1
enter radius of circle2
enter point coordinates x2,y2:2,3
on the circle
USE LOOP
for i in range(1,101):
    print(i)
OUTPUT-
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
print any table by input user
num=eval(input("enter the number"))
for i in range(1,11):
    print(num*i)
  OUTPUT-
  2
  4
  6
  8
  10
  12
  14
  16
  18
  20
USING WHILE LOOP
i=1
while i<10:
    print(i)
    i=i+1
OUTPUT-
1
2
3
4
5
6
7
8
9
SUM OF 9 NUMBERS
sum=0
i=1
while i<10:
  sum=sum+i
  i=i+1
print(i)
OUTPUT-45 
 FIND RANDOM INTEGER NUMBER B/W 0 AND 100
  import random
num=random.randint(0,100)
guess=eval(input("enter a guess between 0 and 100"))
if guess < num:
    print("guess is too low!")
elif guess==num:
    print("guess is correct!!")
else:
    print("guess is too high!")
OUPUT-
enter a guess between 0 and 10034
guess is too high!

import random
num=random.randint(0,100)
guess=-1
while guess !=num:
    guess=eval(input("enter a guess between 0 and 100"))
    if guess < num:
        print("guess is too low!")
    elif guess==num:
        print("guess is correct!!")
    else:
        print("guess is too high!")
OUTPUT-
enter a guess between 0 and 10065
guess is too low!
enter a guess between 0 and 10095
guess is too high!
enter a guess between 0 and 10080
guess is too low!
enter a guess between 0 and 10085
guess is too high!
enter a guess between 0 and 10082
guess is too high!
enter a guess between 0 and 10081
guess is correct!!

for i in range(10):
    for j in range(10):
        print("going loopy n loopy")
OUTPUT-
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy
going loopy n loopy

TO CHECK ABOVE PROGRAM HOW MANY TIMES IT EXECUTES USE COUNT FUNCTION
count=0
for i in range(10):
    for j in range(10):
        count=count+1
print(count)
OUTPUT-
100
PROGRAM to find all the factors of a number input by user
num=eval(input())
for divisor in range(1,num+1):
    if num % divisor==0:
        print(divisor)
OUTPUT-
18
1
2
3
6
9
18
To find the hcf of two number by input user separated by ,
a,b=eval(input("enter two numbers separated by ,: "))
start=1
end=min(a,b)
for divisor in range(start,end+1):
    if a % divisor==0 and b % divisor==0:
        hcf=divisor
print("HCF is: ",hcf)        
OUTPUT-
HCF is :5
 To find the fast hcf of two number using machine
a,b=eval(input("enter two numbers separated by,:"))
r=a%b
while r!=0:
    a,b=b,r
    r=a%b
print("HCF is",b)    
OUTPUT-
enter two numbers separated by,:12345678654,854612358
HCF is 6

num=eval(input("enter the number"))
count=0
for divisor in range(1,num+1):
    if num % divisor == 0:
        count=count+1
if count ==2:
    print("prime number")
else:
    print("non-prime number")
OUTPUT-
enter the number13
prime number
enter the number26
non-prime number
USE BREAK STATEMENT
for i in range(1,11):
    print(i)
    if i==5:
        break
print("out of loop")    
OUTPUT-
1
2
3
4
5
out of loop

num=eval(input("enter the number"))
isprime = True
for divisor in range(2,num):
 if num % divisor ==0:
    isprime=False
    break
 if isprime:
    print("prime number")
 else:
    print("non-prime number")
OUTPUT-
enter the number13
prime number
prime number
prime number
prime number
prime number
prime number
prime number
prime number
prime number
prime number
prime number
TO FIND THE LCM OF TWO NUMBER
num1,num2=eval(input())
if num1>num2:
    small=num2
else:
    small=num1
for i in range(1,small+1):
    if((num1%i==0 and num2%i==0)):
        gcd=i
lcm=(num1*num2)//gcd
print(lcm)
OUTPUT-
ENTER TWO NUMBER2,3
6
USING DEF FUNCTION
TO FIND THE SUM OF  GIVEN NUMBER
def mysum(start,end):
    sum=0
    for i in range(start,end):
        sum=sum+i
    print("sum is",sum)

mysum(1,11)
mysum(50,100)
mysum(20,200)
OUTPUT-
sum is 55
sum is 3725
sum is 19710
FIND THE GRADE SCORE-
def printgrade(score):
    if score >=90.0:
        print('A')
    elif score >=80.0:
        print('B')
    elif score >=70.0:
        print('C')
    elif score >=60.0:
        print('D')
    else:
        print('F')


score=eval(input("enter a score: "))
print("before calling function")
printgrade(score)
print("after calling function")
OUTPUT-
enter a score: 75
before calling function
C
after calling function
IF WE USE GET THEN WE USE RETURN-
def getgrade(score):
    if score >=90.0:
        return('A')
    elif score >=80.0:
        return('B')
    elif score >=70.0:
        return('C')
    elif score >=60.0:
        return('D')
    else:
        return('F')


score=eval(input("enter a score: "))
print("before calling function")
grade=getgrade(score)
print(grade)
print("after calling function")
OUTPUT-
enter a score: 75
before calling function
C
after calling function
TO FIND THE HCF BY USING FUNCTION
def hcf (a,b):
 start=1
 end=min(a,b)
 for divisor in range(start,end+1):
     if a % divisor==0 and b % divisor==0:
         hcf=divisor
 print("HCF is: ",hcf)

a,b=eval(input("enter two numbers separated by ,: "))
hcf(a,b)  
OUTPUT-
enter two numbers separated by ,: 10,15
HCF is:  5
  LCM-
  def hcf (a,b):
 start=1
 end=min(a,b)
 for divisor in range(start,end+1):
     if a % divisor==0 and b % divisor==0:
         hcf=divisor
 return hcf

a,b=eval(input("enter two numbers separated by ,: "))
result = hcf(a,b)  
print("HCF is:",result)
lcm=a*b/result
print("LCM is:",lcm)
OUTPUT-
enter two numbers separated by ,: 10,15
HCF is: 5
LCM is: 30.0
USING MODULE
TIME MODULE
time.time()
1643478102.6222088
>>> time.ctime(1643478102.6222088)
'Sat Jan 29 23:11:42 2022'
TIME DELAY MODULE
import time
for i in range(10):
    print (i)
    time.sleep(2)
OUTPUT-
0
1
2
3
4
5
6
7
8
9
IT WILL WORK IN 2 SECONDS

OPEN YOUTUBE LINK BY USING PYTHON
import webbrowser
import time
webbrowser.open('https://www.youtube.com/watch?v=wn8VH6MWK4M')

import webbrowser
import time
time.sleep(5)
webbrowser.open('https://www.youtube.com/watch?v=wn8VH6MWK4M')

import webbrowser
import time
while True:
  time.sleep(5)
  webbrowser.open('https://www.youtube.com/watch?v=wn8VH6MWK4M')
MAKE A NEW FOLDER BY USING COMMAND PROMPY

C:\Users\AJAY GUPTA>cd C:\Users\AJAY GUPTA\Desktop\Neenu

C:\Users\AJAY GUPTA\Desktop\Neenu>mkdir new2

C:\Users\AJAY GUPTA\Desktop\Neenu>
  USE OS MODULE-TO CREATE A NEW FOLDER BY USING PYTHON
  os.getcwd()
'C:\\Users\\AJAY GUPTA\\AppData\\Local\\Programs\\Python\\Python39'
>>> os.chdir("C:\\Users\\AJAY GUPTA\\Desktop")
>>> os.getcwd()
'C:\\Users\\AJAY GUPTA\\Desktop'
>>> os.mkdir('new')
