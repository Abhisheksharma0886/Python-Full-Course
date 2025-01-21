message = " Hey, good morning, you are such a nice person, Mr. Abhishek sharma"

# string are immutable, so we cant change the original string, we can only create a noew string with the changes time.

new_message = message.replace(" Abhishek", "Aayush").replace("sharma", "Kumar")
                              
print("First message:  ",message)
print("Second message:  ",new_message)