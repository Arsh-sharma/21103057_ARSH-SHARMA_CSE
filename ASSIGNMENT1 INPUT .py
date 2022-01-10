# assignment1
# question1
number1 = int(input('number one is: '))
number2 = int(input('number two is: '))
number3 = int(input('number three is: '))
average = (number1+number2+number3)/3
print('average is:', average)

# question2
Gross_income = int(input('what is your gross income? '))
standard_deduction = 10000
deduction_per_dependent = 3000
Number_of_dependents = int(input('how many members are in your family? '))
Taxable_income = Gross_income - standard_deduction - (deduction_per_dependent * Number_of_dependents)
flat_tax_rate = 20/100
TAX = Taxable_income * flat_tax_rate
print('income tax:', TAX)

# question3
Name_of_student = input('what is your name? ')
SID = int(input('what is yor sid? '))
Gender = input('what is your gender? ')
Course_name = input('what is the name of your course? ')
CGPA = float(input('what is your CGPA? '))
DETAILS = (Name_of_student, SID, Gender, Course_name, CGPA)
print('details are:', DETAILS)

# question4
student1 = int(input('marks of student one: '))
student2 = int(input('marks of student two: '))
student3 = int(input('marks of student three: '))
student4 = int(input('marks of student four: '))
student5 = int(input('marks of student five: '))
LIST = [student1, student2, student3, student4, student5]
print('List before sorting:', LIST)
LIST.sort()
print('list after sorting:', LIST)

# question5a
Colour = ['red', 'green', 'white', 'black', 'pink', 'yellow']
# index of fourth element is 3
Colour.pop(3)
print(Colour)

# question5b
Colour = ['red', 'green', 'white', 'black', 'pink', 'yellow']
Colour[3] = 'purple'; Colour[4] = 'purple'
print(Colour)




