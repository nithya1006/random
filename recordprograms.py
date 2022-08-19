#program 1
name = input("ENTER EMPLOYEE NAME:")
bp = float(input("ENTER BASIC PAY OF THE EMPLOYEE:"))
da = 0.2 * bp
hra = 0.3 * bp
ta = 0.1 * bp
pf = 0.13 * bp
it = 0.05 * bp
gross = bp + ta + da + hra
deduction = pf + it
np = gross - deduction
print("\t\t\t\t\tSALARY SLIP\t\t\t\t")
print("NAME:", name)
print("-" * 50)
print("BASIC PAY\t:", bp, "\t\tPF\t\t :", pf)
print("DA\t\t\t:", da, "\t\tIT\t\t :", it)
print("HRA\t\t\t:", hra)
print("TA\t\t\t:", ta)
print("Gross\t\t:", gross, "\t\tDeduction:", deduction)
print("Net Pay\t\t:", np)
print("-" * 50)

#program 2
import math
print("Quadratic function : (a * x^2) + b*x + c")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d= (b*b) - (4*a*c)

if d > 0:
    print("Roots are real & unequal\n")
    print("r1=",(-b+math.sqrt(d))/(2*a))
    print("r1=",(-b-math.sqrt(d))/(2*a))
elif d == 0:
    print("Roots are real & equal\n")
    print("r1=",-b/2*a,"\tr2=",-b/2*a)
else:
    print("Roots are imaginary")

#program 3
name = input("Enter consumer name:")
num = int(input("Enter EB number:"))
units = int(input("Enter number of units:"))
type_con = input("Enter type of consumption C(commercial)/ D(domestic):")
if type_con == 'D' or type_con=='d':
    if units <=100:
        a = units * 0
    elif units >= 101 and units <= 200:
        a = (100 * 0) + (units - 100) * 7
    elif units >= 201 and units <= 300:
        a = (100 * 0) + (100 * 7) + (units - 200) * 9.5
    else:
        a = (100 * 0) + (100 * 7) + (100 * 9.5) + (units - 300) * 12
if type_con == 'C' or type_con=='c':
    if units <= 100:
        a = units * 10
    elif units >= 101 and units <= 200:
        a = (100 * 10) + (units - 100) * 25
    elif units >= 201 and units <= 300:
        a = (100 * 10) + (100 * 25) + (units - 200) * 40
    else:
        a = (100 * 10) + (100 * 7) + (100 * 9.5) + (units - 300) * 55
print("\t\t\t\t\tELECTRICITY BILL\t\t\t\t")
print("CONSUMER NAME:", name)
print("EB NUMBER\t:", num)
print("TYPE OF CONSUMPTION:", type_con)
print("NUMBER OF UNITS:", units)
print("TOTAL AMOUNT:", a)

#program 4
choice =  input( "1.Area of circle\n2.Area of rectangle\n3.Area of square\n4.Area of triangle\nENTER YOUR CHOICE:")
if choice=="1" :
    r=float(input("Enter radius of circle:"))
    area_cir= 3.14*r*r
    print("Area of circle=",area_cir)
elif choice=="2" :
    l= float(input("Enter length of rectangle:"))
    b= float(input("Enter breadth of rectangle:"))
    area_rect = l * b
    print("Area of rectangle=",area_rect)
elif choice=="3" :
    s= float(input("Enter side of square:"))
    area_sq = s * s
    print("Area of square=",area_sq)
else:
    b= float(input("Enter base of triangle:"))
    h= float(input("Enter height of triangle:"))
    area_tri = (1 / 2) * b * h
    print("Area of triangle=",area_tri)

#program 5
n=int(input("Enter any number:"))
rev=e=s=0
a=n
while n>0:
    rem=n%10
    if rem%2==0:
        e+=1
    else:
        s+=1
    rev=rev*10+rem
    n=n//10
print("The number is",a)
print("Reversed number:",rev,"\nNo.of odd:",s,"\nNo.of even:",e)

#program 6
print("1.Sum of series with x and n values\n2.Sum of series with n values")
ch=int(input("Enter choice:"))
if ch==1:
    f=1
    x=int(input("Enter x value:"))
    n=int(input("Enter power:"))
    s=0
    for i in range(1,n+1):
        f=f*i
        if i%2==0:
            s=s-pow(x,i)/f
        else:
            s=s+pow(x,i)/f
        print("Sum of series:",s)
elif ch==2:
    n=int(input("Enter n value:"))
    s=0
    for a in range(1,n+2):
        term=0
        for b in range(1,a):
            term=term+b
            s=s+term
    print("Sum of",n,"terms is",s)

#program 7 a
n=1
for i in range(1,5):
    for j in range(0,i):
        print(n,end=' ')
        n=n+1
    print()

#program 7 b
a=ord('J')
for i in range(5,1,-1):
    for s in range(1,i):
        print(chr(a),end='')
        a=a-1
    print()

# 8. Accept line and print Number of Uppercase characters, lowercase characters, spaces,
# digits and special characters.
str = input("Enter string")
upper, lower, number, space, special = 0, 0, 0, 0, 0
for i in range(len(str)):
    if str[i].isupper():
        upper += 1
    elif str[i].islower():
        lower += 1
    elif str[i].isdigit():
        number += 1
    elif str[i].isspace():
        space += 1
    else:
        special += 1
print('Upper case letters:', upper)
print('Lower case letters:', lower)
print('Number:', number)
print('Number os Spaces:', space)
print('Number of special characters', special)

# 9.  Write a program that does the following.
# i) Accept two inputs: one integer and one string
# ii) Extract all the digits, in the order they occur from the given string, add the given integer
#    input and the digits extracted from the string.
# iii)  If no digits occur in the given string, set the extracted digit to 0.
#	Eg.   For input 12, ‘a4b5c6’ --- 12 + 456 = 468
# output :
# Enter integer no: 12
# Enter the string : a4b5c6
# given number = 12  given string =  a4b5c6  sum = 12 + 456 = 468

# For input 20 , ‘hello’ ----- 20 + 0 = 20
# output :
# Enter integer no: 20
# Enter the string : hello
# given number = 20  given string =  hello sum = 20+ 0 = 20

num = int(input("Enter an integer :-"))
st = input("Enter a string :-")
digit = ""
for i in st:
    if i.isdigit():
        digit += i
if digit == "":
    digit = 0
else:
    digit = int(digit)
print("Accepted  integer number:", num)
print("Accepted string", st)
print("Accepted  integer number:", num, ",", "Accepted string", st, "->", "sum", num, "+", digit, "=", num + digit)

# 10.Write a program to add ‘ing’ at the end of a given string (length should be at least 3). If the
# given string already ends with ‘ing’ then add ‘ly’ instead. If the length of the given string
# is less than 3, leave it unchanged.
# Input string: Land Expected output: Landing
# Input string: String Expected output: Smilingly
# input string:CV  Expected output:CV

str1 = input("Enter a string")
length = len(str1)
if length > 2:
    if str1[-3:] == 'ing':
        str1 += 'ly'
    else:
        str1 += 'ing'
print(str1)

#11.Write a program that reads a line and print all the palindrome words from the line.
# Eg. S=’Ajay has a racecar. He is a level 1 racer.’
#Palindrome words: racecar level

#a="Ajay has a racecar. He is a level 1 racer."
s=input("Enter any string:")
l=s.split()
for i in l:
    i=i.strip('.')
    rev=i[::-1]
    if i.upper()==rev.upper() and i.lower()==rev.lower() and len(i)>1:
        print(i)


# 12. Write a program to input a string S1. Input two substrings S2 and S3 existing in S1 and a
# replacement string S4. Replace the range of strings starting from S2 till end of S3 with S4.
# Eg: Given string S1= ‘Where there is a will there is a way’
# Substring  S2= ‘there’
# Substring S3 = ‘is’
# Substring S4 = ‘exists’
# Output:Where exists a will there is a way
s1 = input("Enter srting")
s2 = input("Enter starting from s1")
s3 = input("Enter ending string from s1")
if s2 in s1 and s3 in s1:
    a = s1.find(s2)
    b = s1.find(s3)
    if b > a:
        c = len(s3)
    n = s1[a:(b + c)]
    s4 = input("Enter the string which you wants to replace")
    s = s1.replace(n, s4, 1)
    print("Replaced string is:", s)

# 13. Write a program that takes a string with multiple words and then capitalizes the first letter of
# each word and reverses all three letter words.
# Eg: Given String = ‘I have a car in red colour’ New string = ‘I Have A raC In deR Colour’

a = input("Enter a sentence:")
b = a.title()
c = b.split()
for i in c:
    wlen = len(i)
    if (wlen == 3):
        st = ""
        for j in i:
            st = j + st
        print(st, " ", end='')
    else:
        print(i, " ", end='')

# 14. Write a program that reads a line and prints the longest word and its length and also print the
# same without vowels.

# Eg: Given String = ‘Python offers many methods for string manipulation’
# Output 1 = Longest word: manipulation        Its Length: 12
# Output 2 = Longest word  without vowels :mnpltn


a = input("Enter any string")
b = a.split()
c = len(b[0])
for i in b:
    if len(i) > c:
        c = len(i)
    d = i

f = ''
s = 'AEIOUaeiou'
for i in d:
    if i not in s:
        f += i
print("Longest word in the given string:", d)
print("Length of the longest word:", c)
print("Longest word withput vowel:", f)

# 15. Write a program to read N phone numbers with 10 digits and 2 dashes. Print all the valid
# phone numbers, if they are in the format 017-555-1212
# Eg: Given phone numbers
# 044-225-2461
# 12-234-1235
# 044-223-1234
# Output:
# Valid phone numbers
# 044-225-2461
# 044-223-1234


s = int(input("Enter limit:"))
c = ""
for a in range(s):
    b = input("Enter the phone number in the format;999-999-9999:")
    if len(b) == 12 and b[3] == '-' and b[7] == '-' and b[0:3].isdigit() and b[4:7].isdigit() and b[8:]:
        c += b
if c == "":
    print("no valid phone number")
else:
    a = c.split(',')
    for i in a:
        print(i)