# compare the three number and find the greatest number among them.

a = int ( input ( " Enter the first number : " ))
b = int ( input ( " Enter the second number : " ))
c = int ( input ( " Enter the third number : " ))

# if else condition can check the comparison between the three numbers, to find the smallest or the largest number among them.

if a>b and a>c :
    print ( " The First number is the greatest number, and the number is ", a)

elif b>a and b>c :
    print ( " The second number is the greatest bumber and the number is " , b)

elif c>a and c>b :
    print ( " The second number is the greatest bumber and the number is " , b)

else : 
    print ( "The all three number are equal, and the number is ", a)

