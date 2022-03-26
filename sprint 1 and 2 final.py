# Niel Patel
# Word Problem Calculator
print("Welcome to my word problem calculator!")
   
# Problem number 1
print("Collin went to the bank to deposit some money."
"The bankteller gave him 25 $20 dollar bills."
"How much money does collin have in total?")
print(25*20)


# Problem number 2
print( "Mrs. Tracy's class contains 30 students." 
"She needs to have 5 students in each group."
"How many groups of students will there be?")
print(30/5)

#Problem number 3
print("Tim needs to spit the total amount of tip money with his staff at the end of everynight." 
"The total amount of tips made one night was $155.65 with a total of 4 staff memebers working during that night."
 "About how much does each member get rounded to the neartest whole number?")
print(155.65//4)

# Problem number 4
print(" Adam has 6 apples, while his sister Brittney has 8 apples."
      "How many apples do they have all together?")
print(6+8)

# Problem number 5
print(" Ale had a total of $45,000 in his checking account."
      "he went to deposit $5,000, how much does he have left in his checking account?")
print(45000-5000)

# Problem number 6
print(" what is the exponential of 2**?")
print(2**2)

print("what is 2% of 100?")
print(2%100)

print("My name is Niel. My age is",22, "My favorite number is",
      12, sep = ",")

x= input(" What is the first number?")
print(1,x)


print("If Sam had five Oranges, during her snack time she ate one."
 "Tom had 4 Oranges, and during his lunch break he ate one."
 "What calculations can be made to figure out if they have the"
 "equal amount of Oranges?")
T = 4
S = 4

if T==S:
    print(" Tom and Same have the equal amount of Oranges.")

print()

print("If Anthony had 2 touchdown passes and Brandon had 3, who had the"
      "  fewest touchdown passes?")
A= 2
B=3
if A<B:
    print("A is less than B")
elif A == B:
    print("A is equal to B")
else:
    print(" A is greater than B")

print( " Mark has $30,000 in his bank account. TIm has 40,000"
       "in his bank account. Who has the most money in their bank account?")

Mark = 30,000
Tim = 40,000

if not Mark > Tim:
    print("Mark is less than Tim")

a= 6
b=5
boolean_value= a>b
print(boolean_value)

strs = ['welcome', 'to', 'my', 'python', 'project']

def join_strs(strs):
    result = ''
    for s in strs:
        result += ' ' + s
    return result[1:]

##[36,25,16,9,4,1]
for x in range(6,0,-1):
    print(x)

given_list= [5,4,4,3,1,-2,-3,5]
total3 = 0
i=0
while given_list[i]>0:
    total3 += given_list[i]
    i += 1
    print(total3)
    
    
