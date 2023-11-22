
Assignment :- 01

Question 1) Write a Python program to check whether the string is Symmetrical or Palindrome.

Ans: 
Code :-
def palindrome(a):
  
    mid = (len(a)-1)//2   
    start = 0                
    last = len(a)-1
    flag = 0
 
    while(start <= mid):
  
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break;
             
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
              
def symmetry(a):
     
    n = len(a)
    flag = 0
     
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
         
    start1 = 0
    start2 = mid
     
    while(start1 < mid and start2 < n):
         
        if (a[start1]== a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
      
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
         
string = 'amaama'
palindrome(string)
symmetry(string)

Output :-
 

Question 2) Write a Python Program to Accept the Strings Which Contains all Vowels. Given a string, the task is to check if every vowel is present or not. We consider a vowel to be present if it is present in upper case or lower case. i.e., ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’

Ans: 
Code :-
def check(string) :
 
    string = string.lower()
 
    vowels = set("aeiou")
 
    s = set({})
 
    for char in string :
 
        if char in vowels :
            s.add(char)
        else:
            pass
             
    if len(s) == len(vowels) :
        print("Accepted")
    else :
        print("Not Accepted")
 
if __name__ == "__main__" :
     
    string = "SEEquoiaL"
 
    check(string)

Output :-
 

Question 3)Write a Python program that reads two integers representing a month and day and prints the season for that month and day.

Ans: 
Code :-
month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March') and (day > 19):
	season = 'spring'
elif (month == 'June') and (day > 20):
	season = 'summer'
elif (month == 'September') and (day > 21):
	season = 'autumn'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("Season is",season)

Output :-
 

Question 4) Write a Python program to display the astrological sign for a given date of birth.

Ans: 
Code :-
day = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ")
if month == 'december':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",astro_sign)
Output :-
 

Question 5) Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
	
Ans: 
Code :-
print("Input some integers to calculate their sum and average. Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1

if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)

Output :-
 

Question 6) Write a Python program to create the multiplication table (from 1 to 10) of a number.

Ans: 
Code :-
n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)

Output :-
 

Question 7) Write a Python program that iterates the integers from 1 to 20. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "Fizz Buzz".

Ans: 
Code :-
for fizzbuzz in range(21):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

Output :-
 

Assignment :- 02

Question 1) Find the number of rows and columns of a given matrix using NumPy.
(a)Using .shape Attribute.
(b)Using Indexing.

Ans: 
⦁	Using .shape Attribute.

Code :-
import numpy as np
matrix = np.array([[6, 9, 8], [0, 9, 8]])
 
dimensions = np.shape(matrix)
rows, columns = dimensions
 
print("Rows:", rows)
print("Columns:", columns)
Output :-
 

⦁	Using Indexing.

Code :-
import numpy as np
 
matrix = np.array([[6, 3, 1], [9, 7, 2]])
rows = matrix.shape[0]
columns = matrix.shape[1]
 
print("Rows:", rows)
print("Columns:", columns)

Output :-
 

Question 2) Finding the sum of diagonal elementsof a NumPy array.
(a)For 3X3 Numpy matrix.
(b)For 5X5 Numpy Matrix.
Ans: 
(a)For 3X3 Numpy matrix.

Code :-
import numpy as np
  
# creating a 3X3 Numpy matrix
n_array = np.array([[505, 5, 105],
                    [370, 74, 77],
                    [9875, 7,98]])
  
# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)
  
# calculating the Trace of a matrix
trace = np.trace(n_array)
  
  
print("\nTrace of given 3X3 matrix:")
print(trace)

Output :-
 

(b)For 5X5 Numpy Matrix.

Code :-
import numpy as np
  
# creating a 3X3 Numpy matrix
n_array = np.array([[45, 27, 15,12,45],
                    [20, 84, 2,65,34],
                    [255, 425, 105,67,67],
                    [545, 5, 1,67,65],
                    [1, 5, 747,66,35]])
  
# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)
  
# calculating the Trace of a matrix
trace = np.trace(n_array)
  
  
print("\nTrace of given 3X3 matrix:")
print(trace)


Output :-
 

Question 3) Write a python program to Calculate inner, outer, and cross products of matrices and vectors using NumPy.

Ans: 
(a)Using Inner Method

Code :-
import numpy as np

# Vectors
a = np.array([2, 6])
b = np.array([3, 10])
print("Vectors :")
print("a = ", a)
print("\nb = ", b)

# Inner Product of Vectors
print("\nInner product of vectors a and b =")
print(np.inner(a, b))

print("---------------------------------------")

# Matrices
x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])
print("\nMatrices :")
print("x =", x)
print("\ny =", y)

# Inner product of matrices
print("\nInner product of matrices x and y =")
print(np.inner(x, y))

Output :-
 

(b)Using Outer Method

Code :-
import numpy as np

# Vectors
a = np.array([2, 6])
b = np.array([3, 10])
print("Vectors :")
print("a = ", a)
print("\nb = ", b)

# Outer product of vectors
print("\nOuter product of vectors a and b =")
print(np.outer(a, b))

print("------------------------------------")

# Matrices
x = np.array([[3, 6, 4], [9, 4, 6]])
y = np.array([[1, 15, 7], [3, 10, 8]])
print("\nMatrices :")
print("x =", x)
print("\ny =", y)

# Outer product of matrices
print("\nOuter product of matrices x and y =")
print(np.outer(x, y))

Output :-
 

(c) Using Cross Method 

Code :-
import numpy as np

# Vectors
a = np.array([3, 6])
b = np.array([9, 10])
print("Vectors :")
print("a = ", a)
print("\nb = ", b)

# Cross product of vectors
print("\nCross product of vectors a and b =")
print(np.cross(a, b))

print("------------------------------------")

# Matrices
x = np.array([[2, 6, 9], [2, 7, 3]])
y = np.array([[7, 5, 6], [3, 12, 3]])
print("\nMatrices :")
print("x =", x)
print("\ny =", y)

# Cross product of matrices
print("\nCross product of matrices x and y =")
print(np.cross(x, y))

Output :-
 

Question 4) How to count the frequency of unique values in NumPy array.

Ans: 
Code :-
import numpy as np

# create a 1d-array
ini_array = np.array([10, 20, 5,
					10, 8, 20,
					8, 9])

# Get a tuple of unique values
# and their frequency in
# numpy array
unique, frequency = np.unique(ini_array,
							return_counts = True)

# convert both into one numpy array
# and then transpose it
count = np.asarray((unique,frequency )).T

print("The values and their frequency are in transpose form:\n",
	count)

Output :-
 

Question 5) Write a program Compute the Kronecker product of two multi dimension NumPy arrays.

Ans: 
Code :-
import numpy

# Creating arrays
array1 = numpy.array([[1, 2], [3, 4]])
print('Array1:\n', array1)

array2 = numpy.array([[5, 6], [7, 8]])
print('\nArray2:\n', array2)

# Computing the Kronecker Product
kroneckerProduct = numpy.kron(array1, array2)
print('\nArray1 ⊗ Array2:')
print(kroneckerProduct)

Output :-
 

Question 6) Write a program Calculate the QR decomposition of a given matrix using NumPy.

Ans: 
Code :-
import numpy as np


# Original matrix
matrix1 = np.array([[1, 2, 3], [3, 4, 5]])
print(matrix1)

# Decomposition of the said matrix
q, r = np.linalg.qr(matrix1)
print('\nQ:\n', q)
print('\nR:\n', r)

Output :-
 
Question 7) How to use numpy.random.choice() method to choose elements from the list with different probability.

Ans: 
Code :-
import numpy as np

# create a list
num_list = [10, 20, 30, 40, 50]

# uniformly select any element
# from the list
number = np.random.choice(num_list)

print(number)

Output :-
 

Assignment :- 03

Question 1) 
(a) Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.

Ans: 
Code :-
import pandas as pd
ds = pd.Series([2,4,6,8,10])
print(ds)



Output :-
 

(b) Write a Pandas program to convert a Panda module Series to Python list and it's type.
Code :-
import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))

Output :-
 

c) Write a Pandas program to add, subtract, multiple and divide two Pandas Series. Series [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

Code :-
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)

Output :-
 
(d) Write a Pandas program to convert a dictionary to a Pandas series. dictionary:
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
Code :-

import pandas as pd
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print("Original dictionary:")
print(d1)
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)

Output :-
 

(e) Write a Pandas program to convert a NumPy array to a Pandas series.
NumPy array: d1 = [10, 20, 30, 40, 50].

Code :-
import numpy as np
import pandas as pd
np_array = np.array([10, 20, 30, 40, 50])
print("NumPy array:")
print(np_array)
new_series = pd.Series(np_array)
print("Converted Pandas series:")
print(new_series)

Output :-
 

Question 2) 
(a) Write a Pandas program to convert the first column of a DataFrame as a Series. The items are:-- {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}

Ans: 
Code :-
import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
s1 = df.ix[:,0]
print("\n1st column as a Series:")
print(s1)
print(type(s1))

Output :-
 
(b) Write a Pandas program to convert a given Series to an array. 
List is ['100', '200', 'python', '300.12', '400']

Ans: 
Code :-

import pandas as pd
import numpy as np
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Series to an array")
a = s1.values
print(a)
print(type(a))

Output :-
 

Question 3) 
(a) Write a Pandas program to sort a given Series. ['100', '200', 'python', '300.12', '400']

Ans: 
Code :-
import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)
Output :-
 

(b) Write a Pandas program to add some data to an existing Series. ['100', '200', 'python', '300.12', '400']

Ans: 
Code :-

import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
print("\nData Series after adding some data:")
new_s = pd.concat([s, pd.Series([500, "php"])], ignore_index=True)
print(new_s)

Output :-
 
Assignment :- 04

Question 1) Write a Pandas program to select rows from a given Data Frame based on values in some columns.
Data Frame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
Rows for colum1 value == 4
col1 col2 col3
1 4 5 8
3 4 7 0

Ans: 
Code :-
import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print('Rows for colum1 value == 4')
print(df.loc[df['col1'] == 4])

Output :-
 
Question 2) Write a Pandas program to delete Data Frame row(s) based on given column value.
Original Data Frame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
New Data Frame
col1 col2 col3
0 1 4 7
2 3 6 9
3 4 7 0
4 5 8 1

Ans: 
Code :-

import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
df = df[df.col2 != 5]
print("New DataFrame")
print(df)

Output :-
 
Question 3) Write a Pandas program to remove white spaces, left sided whites paces and right sided white spaces of the string values of a given pandas series.

Ans: 
Code :-
import pandas as pd
color1 = pd.Index([' Green', 'Black ', ' Red ', 'White', ' Pink '])
print("Original series:")
print(color1)
print("\nRemove whitespace")
print(color1.str.strip())
print("\nRemove left sided whitespace")
print(color1.str.lstrip())
print("\nRemove Right sided whitespace")
print(color1.str.rstrip())

Output :-
 

Question 4) Write a Pandas program to count of occurrence of a specified sub string in a Data Frame column..Write a Pandas program to count of occurrence of a specified sub string in a Data Frame column.
Ans: 
Code :-
import pandas as pd
df = pd.DataFrame({
    'name_code': ['c001','c002','c022', 'c2002', 'c2222'],
    'date_of_birth ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)
print("\nCount occurrence of 2 in date_of_birth column:")
df['count'] = list(map(lambda x: x.count("2"), df['name_code']))
print(df)

Output :-
 

Question 5) Write a Pandas program to check whether only numeric values present in a given column of a Data Frame.
Ans: 
Code :-
import pandas as pd
df = pd.DataFrame({
    'company_code': ['Company','Company a001', '2055', 'abcd', '123345'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})
	
print("Original DataFrame:")
print(df)
print("\nNumeric values present in company_code column:")
df['company_code_is_digit'] = list(map(lambda x: x.isdigit(), df['company_code']))
print(df)
Output :-

 

Question 6) Write a Pandas program to check whether only proper case or title case is present in a given column of a Data Frame.

Ans: 
Code :-
import pandas as pd
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'Hhhh', 'abcd', 'EAWQaaa'],
    'date_of_sale ': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]})

print("Original DataFrame:")
print(df)
print("\nIs proper case or title case?")
df['company_code_is_title'] = list(map(lambda x: x.istitle(), df['company_code']))
print(df)


Output :-
 

Question 7) Write a Pandas program to replace arbitrary values with other values in a given Data Frame.

Ans: 
Code :-
import pandas as pd
df = pd.DataFrame({
    'company_code': ['A','B', 'C', 'D', 'A'],
    'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})

print("Original DataFrame:")
print(df)

print("\nReplace A with c:")
df = df.replace("A", "C")
print(df)




Output :-
 

Question 8) Write a Pandas program to remove repetitive characters from the specified column of a given Data Frame.

Ans: 
Code :-
import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'text_code': ['t0001.','t0002','t0003', 't0004'],
    'text_lang': ['She livedd a long life.', 'How oold is your father?', 'What is tthe problem?','TThhis desk is used by Tom.']
    })
print("Original DataFrame:")
print(df)
def rep_char(str1):
    tchr = str1.group(0)
    if len(tchr) > 1:
        return tchr[0:1] # can change the value here on repetition
def unique_char(rep, sent_text):
    convert = re.sub(r'(\w)\1+', rep, sent_text) 
    return convert
df['normal_text']=df['text_lang'].apply(lambda x : unique_char(rep_char,x))
print("\nRemove repetitive characters:")
print(df)
Output :-
 

Question 9) Write a Pandas program to extract date (format: mm-dd-yyyy) from a given column of a given Data
Frame.

Ans: 
Code :-
import pandas as pd
import re as re
df = pd.DataFrame({
    'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
    'date_of_sale': ['12/05/2002','16/02/1999','05/09/1998','12/02/2022','15/09/1997'],
    'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})
print("Original DataFrame:")
print(df)
def find_valid_dates(dt):
    #format: mm-dd-yyyy
    result = re.findall(r'\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b',dt)
    return result
df['valid_dates']=df['date_of_sale'].apply(lambda dt : find_valid_dates(dt))
print("\nValid dates (format: mm-dd-yyyy):")
print(df)




Output :-
 

Question 10) Write a Pandas program to extract numbers less than 100 from the specified column of a given Data
Frame.

Ans: 
Code :-

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'company_code': ['c0001','c0002','c0003', 'c0003', 'c0004'],
    'address': ['72 Surrey Ave.11','92 N. Bishop Ave.','9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court']
    })
print("Original DataFrame:")
print(df)

def test_num_less(n):
    nums = []
    for i in n.split():
        result = re.findall(r'\b(0*(?:[1-9][0-9]?|100))\b',i)
        nums.append(result)
        all_num=[",".join(x) for x in nums if x != []]
    return " ".join(all_num)

df['num_less'] = df['address'].apply(lambda x : test_num_less(x))
print("\nNumber less than 100:")
print(df)

Output :-
 




Assignment :- 05

Question 1) write a program to implement tic-tac-toe game problem.

Ans: 
Code :-
import numpy as np
import random
from time import sleep
 
def create_board():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
 
def possibilities(board):
    l = []
 
    for i in range(len(board)):
        for j in range(len(board)):
 
            if board[i][j] == 0:
                l.append((i, j))
    return(l)

def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return(board)
  
def row_win(board, player):
    for x in range(len(board)):
        win = True
 
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
 
        if win == True:
            return(win)
    return(win)
 
def col_win(board, player):
    for x in range(len(board)):
        win = True
 
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
 
        if win == True:
            return(win)
    return(win)
 
def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win
 
def evaluate(board):
    winner = 0
 
    for player in [1, 2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
 
            winner = player
 
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
 
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)
 
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return(winner)
 
print("Winner is: " + str(play_game()))

Output :-
 
Question 2) Write a program to simulate 4-Queen problem.

Ans: 
Code :-
global N
N = 4
 
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j],end=' ')
        print()

def isSafe(board, row, col):
 
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True
 
def solveNQUtil(board, col):
    if col >= N:
        return True
 
    for i in range(N):
 
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQUtil(board, col + 1) == True:
                return True
 
            board[i][col] = 0

    return False
 
def solveNQ():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]
             ]
 
    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")
        return False
 
    printSolution(board)
    return True

solveNQ()

Output :-
 

Question 3) Write a program to implement breadth first search algorithm.

Ans: 
Code :-
from collections import defaultdict
 
class Graph:
 
    def __init__(self):
 
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def BFS(self, s):
 
        visited = [False] * (max(self.graph) + 1)
 
        queue = []

        queue.append(s)
        visited[s] = True
 
        while queue:

            s = queue.pop(0)
            print(s, end=" ")
 
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
if __name__ == '__main__':

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)

Output :-
 

Question 4) Write a program to implement depth first search algorithm.

Ans: 
Code :-
from collections import defaultdict

class Graph:

    def __init__(self):
 
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end=' ')
 
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):

        visited = set()

        self.DFSUtil(v, visited)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Depth First Traversal (starting from vertex 2)")
     
    g.DFS(2)

Output :-
 

Assignment :- 06

Question 1) Write a program to implement A* search algorithm using python.

Ans: 
Code :-
import heapq
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = float('inf')
        self.h = 0  
        self.parent = None

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(grid, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(start[0], start[1])
    goal_node = Node(end[0], end[1])

    start_node.g = 0
    start_node.h = heuristic(start_node, goal_node)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = []
            while current_node:
                path.insert(0, (current_node.x, current_node.y))
                current_node = current_node.parent
            return path

        closed_list.add((current_node.x, current_node.y))
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_x, neighbor_y = current_node.x + dx, current_node.y + dy
            if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]) and grid[neighbor_x][neighbor_y] == 0:
                neighbors.append((neighbor_x, neighbor_y))

        for neighbor in neighbors:
            neighbor_node = Node(neighbor[0], neighbor[1])

            if (neighbor_node.x, neighbor_node.y) in closed_list:
                continue

            tentative_g = current_node.g + 1

            if tentative_g < neighbor_node.g:
                neighbor_node.parent = current_node
                neighbor_node.g = tentative_g
                neighbor_node.h = heuristic(neighbor_node, goal_node)
                if neighbor_node not in open_list:
                    heapq.heappush(open_list, neighbor_node)

    return None

grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)

if path:
    print("Shortest path:", path)
else:
    print("No path found.")


Output :-
 

Question 2) Write a program to implement Ao* search algorithm using python.

Ans: 
Code :-
import heapq
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = float('inf') 
        self.h = 0  
        self.f = None
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f
def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def ao_star(grid, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(start[0], start[1])
    goal_node = Node(end[0], end[1])

    start_node.g = 0
    start_node.h = heuristic(start_node, goal_node)
    start_node.f = start_node.g + start_node.h
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            return reconstruct_path(current_node)

        closed_list.add((current_node.x, current_node.y))
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_x, neighbor_y = current_node.x + dx, current_node.y + dy
            if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]) and grid[neighbor_x][neighbor_y] == 0:
                neighbors.append((neighbor_x, neighbor_y))

        for neighbor in neighbors:
            neighbor_node = Node(neighbor[0], neighbor[1])

            if (neighbor_node.x, neighbor_node.y) in closed_list:
                continue

            tentative_g = current_node.g + 1

            if tentative_g < neighbor_node.g:
                neighbor_node.parent = current_node
                neighbor_node.g = tentative_g
                neighbor_node.h = heuristic(neighbor_node, goal_node)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if neighbor_node not in open_list:
                    heapq.heappush(open_list, neighbor_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.insert(0, (node.x, node.y))
        node = node.parent
    return path

grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = ao_star(grid, start, end)

if path:
    print("Shortest path:", path)
else:
    print("No path found.")

Output :-
 

Question 3) Write a program to implement Hill Climbing algorithm using python.

Ans: 
Code :-
import random
def objective_function(x):
    return -x**2 

def hill_climbing(max_iterations, step_size, initial_solution):
    current_solution = initial_solution
    current_value = objective_function(current_solution)
    for _ in range(max_iterations):
        neighbor = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor)
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
    return current_solution, current_value

if __name__ == "__main__":
    max_iterations = 1000 
    step_size = 0.1   
    initial_solution = random.uniform(-10, 10)  
    best_solution, best_value = hill_climbing(max_iterations, step_size, initial_solution)
    print(f"Best Solution: {best_solution}")
    print(f"Best Value: {best_value}")

Output :-
 

Assignment :- 07

Question 1) Write a program to Minimax and Alpha-Beta Pruning Using Python.

Ans: 
(a) Minimax

Code :-
# Tic-Tac-Toe board representation
board = [' ' for _ in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])

def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != ' ':
            return board[i]
    
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != ' ':
            return board[i]
    
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]
 
    if ' ' not in board:
        return 'Draw'
    
    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    if winner is not None:
        if winner == 'X':
            return -1
        elif winner == 'O':
            return 1
        else:
            return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_eval = float('-inf')
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    
    return best_move

while True:
    print_board(board)
    move = int(input("Enter your move (0-8): "))

    if board[move] == ' ':
        board[move] = 'X'
        if check_winner(board) is not None:
            print("You win!")
            break

        if ' ' not in board:
            print("It's a draw!")
            break

        ai_move = best_move(board)
        board[ai_move] = 'O'
        if check_winner(board) is not None:
            print("AI wins!")
            break
    else:
        print("Invalid move. Try again.")

Output :-
 

(b) Alpha-Beta Pruning

Code :-
class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

# Alpha-beta pruning function
def alpha_beta(node, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value  # Leaf node, return its value
    
    if is_maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Prune the remaining branches
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Prune the remaining branches
        return min_eval

if __name__ == "__main__":
    # Create a sample game tree
    leaf1 = Node(3)
    leaf2 = Node(6)
    leaf3 = Node(2)
    leaf4 = Node(8)
    node1 = Node(10, [leaf1, leaf2])
    node2 = Node(12, [leaf3, leaf4])
    root = Node(0, [node1, node2])

    # Perform alpha-beta pruning
    result = alpha_beta(root, 3, float('-inf'), float('inf'), True)
    print("Optimal value:", result)
Output :-
 

Question 2) Write a program to shuffle Deck of cards.

Ans: 
Code :-
import itertools, random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

random.shuffle(deck)

print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])

Output :-
 




Question 3) Write a program to A star Using simulated annealing.

Ans: 
Code :-
import random
import math

def objective_function(x):
    return x**2

initial_state = 10.0
initial_temperature = 100.0
cooling_rate = 0.95

def a_star_search():
    best_state = initial_state
    best_cost = objective_function(best_state)
    for state in range(-100, 101):
        cost = objective_function(state)
        if cost < best_cost:
            best_state = state
            best_cost = cost
    return best_state, best_cost

def simulated_annealing():
    current_state = initial_state
    current_cost = objective_function(current_state)
    best_state = current_state
    best_cost = current_cost
    temperature = initial_temperature

    while temperature > 0.1:
        neighbor_state = current_state + random.uniform(-1, 1)
        neighbor_cost = objective_function(neighbor_state)

        if neighbor_cost < current_cost:
            current_state = neighbor_state
            current_cost = neighbor_cost
            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost
        else:
            acceptance_probability = math.exp(-(neighbor_cost - current_cost) / temperature)
            if random.random() < acceptance_probability:
                current_state = neighbor_state
                current_cost = neighbor_cost

        temperature *= cooling_rate

    return best_state, best_cost

if __name__ == "__main__":
    a_star_solution, a_star_cost = a_star_search()
    print(f"A* Solution: x = {a_star_solution}, Cost = {a_star_cost}")

    # Simulated Annealing
    sa_solution, sa_cost = simulated_annealing()
    print(f"Simulated Annealing Solution: x = {sa_solution}, Cost = {sa_cost}")

Output :-
 


Assignment :- 08

Question 1) Write a program to solve water jug problem using python.

Ans: 
Code :-
from collections import deque
def Solution(a, b, target):
    m = {}
    isSolvable = False
    path = []

    q = deque()

    q.append((0, 0))

    while (len(q) > 0):

        # Current state
        u = q.popleft()
        if ((u[0], u[1]) in m):
            continue
        if ((u[0] > a or u[1] > b or
            u[0] < 0 or u[1] < 0)):
            continue
        path.append([u[0], u[1]])

        m[(u[0], u[1])] = 1

        if (u[0] == target or u[1] == target):
            isSolvable = True

            if (u[0] == target):
                if (u[1] != 0):
                    path.append([u[0], 0])
            else:
                if (u[0] != 0):

                    path.append([0, u[1]])

            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",",
                    path[i][1], ")")
            break

        q.append([u[0], b]) 
        q.append([a, u[1]]) 

        for ap in range(max(a, b) + 1):
            c = u[0] + ap
            d = u[1] - ap

            if (c == a or (d == 0 and d >= 0)):
                q.append([c, d])
            c = u[0] - ap
            d = u[1] + ap

            if ((c == 0 and c >= 0) or d == b):
                q.append([c, d])

        q.append([a, 0])

        q.append([0, b])

    if (not isSolvable):
        print("Solution not possible")

if __name__ == '__main__':

    Jug1, Jug2, target = 4, 3, 2
    print("Path from initial state "
        "to solution state ::")

    Solution(Jug1, Jug2, target)

Output :-
 

Question 2) Write a program to shuffle Deck of cards using python .

Ans: 
Code :-
import itertools, random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

random.shuffle(deck)

print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
Output :-
 

Question 3) Write a program to solve the Monkey Banana problem using python .

Ans: 
Code :-
def Monkey_go_box(monkey, box):
    print(f"Monkey goes from {monkey} to {box}")

def Monkey_move_box(box, banana):
    print(f"Monkey moves the box from {box} to {banana}")

def Monkey_climb_box():
    print("Monkey climbs onto the box")

def Monkey_get_banana():
    print("Monkey gets the banana")

if __name__ == "__main__":
    monkey = "start_position"
    banana = "banana_position"
    box = "box_position"

    print("The steps are as follows:")

    Monkey_go_box(monkey, box)
    Monkey_move_box(box, banana)
    Monkey_climb_box()
    Monkey_get_banana()

Output :-

 

Question 4) Write a program to solve traveling salesman problem using python .

Ans: 
Code :-
from sys import maxsize 
from itertools import permutations
V = 4

def travellingSalesmanProblem(graph, s): 

    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 

    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:

        current_pathweight = 0

        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        min_path = min(min_path, current_pathweight) 

    return min_path 

if __name__ == "__main__": 

    graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
            [15, 35, 0, 30], [20, 25, 30, 0]] 
    s = 0
    print(travellingSalesmanProblem(graph, s))

Output :-
 

Assignment :- 09

Question 1) Develop a Python script to model adsorption using a simple adsorption isotherm equation, allowing users to input values and plot the adsorption curve.

Ans: 
Code :-
import numpy as np
import matplotlib.pyplot as plt

# Define the Langmuir isotherm equation
def langmuir_adsorption(q_max, K, c):
    return (q_max * K * c) / (1 + K * c)

# Input values from the user
q_max = float(input("Enter Qmax (maximum adsorption capacity): "))
K = float(input("Enter Langmuir constant (adsorption affinity): "))
c_values = np.linspace(0, 10, 100)  # Concentration values for the curve

# Calculate the adsorption data
adsorption_data = [langmuir_adsorption(q_max, K, c) for c in c_values]

plt.figure()
plt.plot(c_values, adsorption_data, label='Adsorption Isotherm')
plt.xlabel('Concentration (c)')
plt.ylabel('Adsorption (q)')
plt.title('Langmuir Adsorption Isotherm')
plt.legend()
plt.grid(True)
plt.show()

Output :-
 

Question 2) Write a Python function to apply double negation to a logical expression represented as a string and return the simplified expression.

Ans: 
Code :-
def simplify_double_negation(expression):
    while "not not" in expression:
        expression = expression.replace("not not", "")

    return expression

input_expression = "not not (A and (B or not C)) or not not (D and E)"
simplified_expression = simplify_double_negation(input_expression)
print("Original Expression:", input_expression)
print("Simplified Expression:", simplified_expression)

Output :-
 

Question 3) Create a Python program that checks if a given logical expression violates the law of contradiction and provides feedback on the contradiction if found.

Ans: 
Code :-
import sympy

def check_contradiction(expression):
    try:
        parsed_expression = sympy.sympify(expression)
        simplified = sympy.simplify(parsed_expression)

        if simplified is True:
            print("The expression is a tautology (always true). It does not violate the law of contradiction.")
        elif simplified is False:
            print("The expression is a contradiction (always false) and violates the law of contradiction.")
        else:
            print("The expression is neither a tautology nor a contradiction.")
    except sympy.SympifyError:
        print("Invalid expression. Please check your logical expression.")

if __name__ == "__main__":
    expression = input("Enter a logical expression: ")
    check_contradiction(expression)

Output :-
 

Question 4) Implement a Python function that represents a Modus Ponens inference rule. Given a knowledge base with facts and an implication, the function should determine if the conclusion can be derived.

Ans: 
Code :-
def modus_ponens(knowledge_base, antecedent, conclusion):
    # Check if the antecedent is in the knowledge base
    if antecedent in knowledge_base:
        # Check if the implication (antecedent -> conclusion) is also in the knowledge base
        if (antecedent, conclusion) in knowledge_base:
            return True, conclusion  # Modus Ponens applies, return True and the conclusion
    return False, None  # Modus Ponens does not apply

# Example usage:
if __name__ == "__main__":
    # Define a knowledge base with facts and implications
    knowledge_base = {
        "A": True,
        "B": True,
        ("A", "C"): True,
        ("B", "D"): True
    }

    antecedent = "A"
    conclusion = "C"

    result, derived_conclusion = modus_ponens(knowledge_base, antecedent, conclusion)

    if result:
        print(f"Modus Ponens applies. Conclusion '{conclusion}' is derived.")
    else:
        print("Modus Ponens does not apply or the knowledge base is incomplete.")

Output :-
 

Question 5) Create a Python program that demonstrates Modus Tollens. Given a conditional statement and the negation of the consequent, the program should check if it implies the negation of the antecedent.

Ans: 
Code :-
def modus_tollens(conditional, negation_of_consequent, negation_of_antecedent):
    # Check if the conditional statement is in the form of "if P, then Q"
    if conditional.count("->") == 1:
        antecedent, consequent = conditional.split("->")
        antecedent = antecedent.strip()
        consequent = consequent.strip()
        
        # Check if the given conditional statement matches the expected form
        if conditional == f"{antecedent} -> {consequent}":
            # Check if the negation of the consequent matches the consequent of the conditional
            if negation_of_consequent == f"not {consequent}":
                # Check if the negation of the antecedent matches the antecedent of the conditional
                if negation_of_antecedent == f"not {antecedent}":
                    return True, f"not {antecedent}"  # Modus Tollens applies, return True and the negation of the antecedent
    return False, None  # Modus Tollens does not apply

# Example usage:
if __name__ == "__main__":
    conditional = "P -> Q"
    negation_of_consequent = "not Q"
    negation_of_antecedent = "not P"

    result, derived_negation = modus_tollens(conditional, negation_of_consequent, negation_of_antecedent)

    if result:
        print(f"Modus Tollens applies. Negation of antecedent '{derived_negation}' is derived.")
    else:
        print("Modus Tollens does not apply or the given statements do not match the expected form.")

Output :-
 


Assignment :- 10

Question 1) Write a Python function to demonstrate the commutative law for addition and multiplication using user input.

Ans: 
Code :-
def commutative_law():
    operation = input("Enter 'add' for addition or 'multiply' for multiplication: ").strip().lower()
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))

    if operation == "add":
        result1 = a + b
        result2 = b + a
        if result1 == result2:
            print(f"Commutative Law for Addition holds: {a} + {b} = {b} + {a} = {result1}")
        else:
            print("Commutative Law for Addition does not hold.")
    elif operation == "multiply":
        result1 = a * b
        result2 = b * a
        if result1 == result2:
            print(f"Commutative Law for Multiplication holds: {a} * {b} = {b} * {a} = {result1}")
        else:
            print("Commutative Law for Multiplication does not hold.")
    else:
        print("Invalid operation. Please enter 'add' or 'multiply'.")

if __name__ == "__main__":
    commutative_law()

Output :-

For Addition:-

 

For Multiplication:-

 

Question 2) Create a Python program that verifies the associative law for addition and multiplication with a list of numbers.

Ans: 
Code :-
def verify_associative_law(numbers, operation):
    if operation == "add":
        # Associative Law for Addition
        left_associative_result = sum(numbers)
        right_associative_result = numbers[0]
        for num in numbers[1:]:
            right_associative_result += num

        return left_associative_result == right_associative_result

    elif operation == "multiply":
        # Associative Law for Multiplication
        left_associative_result = 1
        right_associative_result = numbers[0]
        for num in numbers:
            left_associative_result *= num
        for num in numbers[1:]:
            right_associative_result *= num

        return left_associative_result == right_associative_result

    else:
        return False

if __name__ == "__main__":
    numbers = [2, 3, 4]
    operation = input("Enter 'add' for addition or 'multiply' for multiplication: ").strip().lower()

    result = verify_associative_law(numbers, operation)

    if result:
        print(f"Associative Law for {operation.capitalize()} holds for {numbers}.")
    else:
        print(f"Associative Law for {operation.capitalize()} does not hold for {numbers}.")


Output :-
 

Question 3) Write a Python function that implements De Morgan's Laws for two Boolean variables and returns the results for both AND and OR operations.

Ans: 
Code :-
def demorgans_laws(a, b):
    # Apply De Morgan's Laws
    not_a_and_b = (not a) or (not b)
    not_a_or_b = (not a) and (not b)

    return not_a_and_b, not_a_or_b

if __name__ == "__main__":
    a = True  # Change to True or False as needed
    b = False  # Change to True or False as needed

    result_and, result_or = demorgans_laws(a, b)

    print(f"De Morgan's Law for AND: not ({a} and {b}) = {result_and}")
    print(f"De Morgan's Law for OR: not ({a} or {b}) = {result_or}")

Output :-
 

Question 4) Implement a Python function that illustrates the law of excluded middle by determining if a given proposition is either true or false.
Ans: 
Code :-
def law_of_excluded_middle(proposition):
    if proposition:
        return "The proposition is true"
    else:
        return "The proposition is false"

if __name__ == "__main__":
    # You can change the value of the proposition as needed
    proposition = True

    result = law_of_excluded_middle(proposition)

    print(result)

Output :-
 


Assignment :- 11

Question 1)Implement a Python-based resolution theorem prover for predicate logic. Given a set of clauses, the program should determine if a query can be inferred.

Ans: 
Code :-
def resolution(clauses):
    """
    Resolve the given set of clauses using the resolution algorithm.

    :param clauses: List of clauses in CNF (Conjunctive Normal Form)
    :return: True if the query can be inferred, False otherwise
    """
    new_clause = set()

    while True:
        # Generate all possible pairs of clauses
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = resolve_pair(clauses[i], clauses[j])

                # Check if resolvent is empty (contradiction)
                if not resolvents:
                    return True

                # Add unique resolvents to the new_clause set
                new_clause.update(resolvents)

        # If new_clause is a subset of clauses, no new resolvents can be generated
        if new_clause.issubset(set(clauses)):
            return False

        # Update clauses with the new resolvents
        clauses.extend(new_clause)

def resolve_pair(c1, c2):
    """
    Resolve two clauses and return the set of resolvents.

    :param c1: First clause
    :param c2: Second clause
    :return: Set of resolvents
    """
    resolvents = set()

    for literal in c1:
        if ('-' + literal) in c2:
            # Resolve the two clauses by removing the resolved literals
            resolvent = (c1 - {literal}) | (c2 - {'-' + literal})
            resolvents.add(tuple(resolvent))

    return resolvents

# Example usage:
clauses = [
    {'A', '-B', 'C'},
    {'B', '-C'},
    {'-A', 'B'}
]

query = ['-C']

result = resolution(clauses + [set(query)])
print("Query can be inferred:", result)

Output :-
 

Question 2) Develop a Python function that identifies and counts the unique predicates and variables in a predicate logic expression.

Ans: 
Code :-
import re

def extract_predicates_variables(expression):
    # Define regular expressions for predicates and variables
    predicate_pattern = re.compile(r'([a-zA-Z_]\w*)\(')
    variable_pattern = re.compile(r'([a-zA-Z_]\w*)')

    # Find all matches for predicates and variables
    predicates = set(predicate_pattern.findall(expression))
    variables = set(variable_pattern.findall(expression))

    return predicates, variables

def count_predicates_variables(expression):
    predicates, variables = extract_predicates_variables(expression)

    # Count the number of unique predicates and variables
    predicate_count = len(predicates)
    variable_count = len(variables)

    return predicate_count, variable_count

# Example usage:
predicate_logic_expression = "parent(john, mary) && ancestor(mary, ann) || sibling(john, ann)"
predicate_count, variable_count = count_predicates_variables(predicate_logic_expression)

print("Predicates:", predicate_count)
print("Variables:", variable_count)

Output :-
 

Question 3) Write a Python program that uses Modus Ponens to perform inference on a set of predicate logic statements.

Ans: 
Code :-
def modus_ponens(rule, statement):
    """
    Apply Modus Ponens inference rule.

    :param rule: The implication rule in the form (P, Q), meaning if P then Q.
    :param statement: The given statement P.
    :return: The inferred statement Q if the rule is applicable, otherwise None.
    """
    antecedent, consequent = rule

    if antecedent == statement:
        return consequent
    else:
        return None

# Example usage:
if __name__ == "__main__":
    # Example Modus Ponens rule: If it's raining, then the ground is wet.
    modus_ponens_rule = ("raining", "ground is wet")

    # Given statement: It's raining.
    given_statement = "raining"

    # Apply Modus Ponens
    result = modus_ponens(modus_ponens_rule, given_statement)

    # Output the result
    if result is not None:
        print(f"Using Modus Ponens: If {given_statement}, then {result}.")
    else:
        print("Modus Ponens is not applicable for the given statements.")

Output :-
 






THANK   YOU
