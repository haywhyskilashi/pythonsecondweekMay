##################################################

# Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for i in range(50, 0, -10):
    print(i)


#######################################################


# Display numbers from -10 to -1 using for loop



for i in range(-10, 0, 1):
    print(i)


##########################################################################

# Use else block to display a message “Done” after successful
# execution of for loop

for i in range(5):
    print(i)

else:
    print("Done!")


################################################################################


# Write a program to display all prime numbers within a range

for i in range(25, 50 + 1):
    if i > 1:
        for j in range(2, i):
            if (j % i) == 0:
                break
        else:
            print(i)


#########################################################################################


num1 = 0
num2 = 1

for i in range(10):
    print(num1)
    res = num1 + num2
    num1 = num2
    num2 = res


##################################################################################


# Find the factorial of a given number

factorial = int(input("Enter a number to factorial: "))


for i in range(1, 5):
    factorial = factorial * i
    print(factorial)


#######################################################################################


# Reverse a given integer number

givenNumber = int(input("Enter a number you'd like to reverse"))
reversedNumber = str(givenNumber)[::-1]
print(reversedNumber)


#######################################################################

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in my_list[1::2]:
    print(i)


###############################################################################


# Calculate the cube of all numbers from 1 to a given number

inputNumber = int(input("Enter a number: "))

for i in range(inputNumber):
    result = i * i * i

    print("Current Number is: ", i, "and the cube is: ", result)


################################################################################


for i in range(0, 5):
    for j in range(i):
        print("*", end=" ")

    print("*")

for y in range(5, 0, -1):
    for z in range(0, y - 1):
        print("*", end=" ")

    print("*")

########################################################################################


# Create a string made of the first, middle and last character

str1 = "James"

firstCharacter = str1[0]
middleCharacter = str1[2]
lastCharacter = str1[-1]

print(firstCharacter + middleCharacter + lastCharacter)

###########################################################

# Create a string made of the middle three characters

str1 = "JhonDipPeta"

middle = int(len(str1) / 2)


res = str1[middle - 1:middle + 2]
print(res)

###############################################################

# Create a new string made of the first, middle, and last
# characters of each input string

s1 = "America"
s2 = "Japan"

first = s1[0] + s2[0]

# middle = s1[int(len(s1) / 2) : int(len(s1) / 2) + 1] + s2[int(len(s2) / 2) : int(len(s2)/ 2) + 1]
middlee = s1[3:4] + s2[2:3]

last = s1[len(s1) - 1] + s2[len(s2) - 1]

res = first + middlee + last
print(res)


###########################################################################

# Arrange string characters such that lowercase letters should come
# first

str1 = "PyNaTive"
lower = []
upper = []

for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)

sortedStr = ''.join(lower + upper)
print(sortedStr)
# allLower = str1.lower()
# restCharacter = allLower[3:]
# first3Cap = allLower[0:3].upper()
#
# print(first3Cap + restCharacter)


##################################################################


# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

alphabets = 0
digits = 0
symbols = 0

for i in str1:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
    else:
        symbols += 1

print("Alphabets =", alphabets, "Digits =", digits, "Symbols =", symbols)

########################################################################

# Append new string in the middle of a given string

s1 = "Ault"
s2 = "Kelly"

print(" ".join([s1, s2]))

##################################################################


# Create a mixed String using the following rules

s1 = "Abc"
s2 = "Xyz"

firstChar = s1[0] + s2[-1]
secondChar = s1[1] + s2[1]


#s  first char of s1, then the last char of s2
# char of s1 and second last char of s2

print(firstChar + secondChar)


###########################################################

# String characters balance Test

s1 = "Ynf"
s2 = "PYnative"

if(s1 in s2):
    print(True)
else:
    print(False)


########################################################################


# Find all occurrences of a substring in a given string by
# ignoring the case

str1 = "Welcome to USA. usa awesome, isnt it"
subString = "USA"

tempstr = str1.lower()

print(tempstr)

print(tempstr.count("usa"))


############################################################################

# Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"
total = 0
cnt = 0

for i in str1:

    if i.isdigit():

        total = total + int(i)
        cnt += 1

avg = total / cnt
print("Sum is: ", total, "Average: ", avg)



###################################################################


# Write a program to count occurrences of all characters within a string
char_dict = dict()
str1 = "Apple"
for i in str1:
    count = str1.count(i)
    char_dict[i] = count
    print("Result: ", char_dict)



#######################################################################

# reverse string

str1 = "PYnative"

str1 = str1[::-1]
print(str1)

### OR
str = "PYnative"
str = ''.join(reversed(str))
print(str)

print(list(reversed((6, 1, 3, 9))))
print(''.join(reversed("hello")))

#########################################

# Write a program to find the last position of a substring
# “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."

print(str1.rfind("Emma"))

#########################################################

#Write a program to split a given string on hyphens and
# display each substring.

str1 = 'Emma-is-a-data-scientist'
x = str1.split("-")
for sub in x:
    print(sub)


##############################################################

# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

def identify(x):
    return x

print(list(filter(identify, str_list)))


###########################################################

# Remove special symbols / punctuation from a string
import re
str1 = "/*Jon is @developer & musician"

s1 = re.sub("[/*@&]","",str1)
print(s1)


##############################################
# Removal all characters from a string except integers

str1 = 'I am 25 years and 10 months old'

res = "".join([item for item in str1 if item.isdigit()])
print(res)

######################################################

# Write a program to find words with both alphabets and
# numbers from an input string.


str1 = "Emma25 is Data scientist50 and AI Expert"
res = []
temp = str1.split()

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

for i in res:
    print(i)


#########################################################

# Replace each special symbol with # in the following string
import string

str1 = '/*Jon is @developer & musician!!'
replace_char = "#"
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print(str1)


##################################################
num = 8
print('%o' % num)