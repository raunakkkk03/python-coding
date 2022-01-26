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
for i in range(101):
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
for i in range(101):
    print(i)
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
for i in range(101):
    print(i)
OUTPUT-
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
