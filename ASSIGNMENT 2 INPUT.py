#ASSIGNMENT2
#--------------------------------------
#Q1
statement = "Python is a case sensitive language"
#a)
print(len(statement))
#b)
print(statement[::-1])
#c)
print(statement[10:26])
#d)
print(statement.replace("a case sensitive","object oriented"))
#e)
print(statement.find("a"))
#f)
print(statement.replace(" ",""))
#___________________________________________________________________________________
#Q2
NAME='ARSH SHARMA'
SID='21103057'
DEPARTMENT='COMPUTER SCIENCE'
CGPA='9.9'
print(f'''Hey, {NAME} Here!
My SID is {SID}
I am from {DEPARTMENT} department and my CGPA IS {CGPA}''')
#_____________________________________________________________________________________
#Q3
a=56
b=10
#a)
print(a&b)
#b)
print(a|b)
#c)
print(a^b)
#d)
a=a<<2
b=b<<2
#e)
a=a>>2
b=b>>4
#_________________________________________________________________________________________
#Q4
numbers=[]
for count in range(3):
 NUMBERS=float(input('enter the number: '))
numbers.append(NUMBERS)
max=numbers[0]
if NUMBERS>max:
 max=number
print('Largest number is: ',max)
#______________________________________________________________________________________________
#Q5
Statement=input("enter a statement: ")
list= Statement.split()
for word in list:
 if word =='name':
  print('yes')
  break
else:
 print('no')
#____________________________________________________________________________________________
#Q6
lenght1 = int(input('lenght of first side: '))
lenght2 = int(input('lenght of second side: '))
lenght3 = int(input('lenght of third side: '))
if lenght1+lenght2>lenght3 and lenght2+lenght3>lenght1 and lenght3+lenght1>lenght2:
  print('yes')
else:
 print('no')
