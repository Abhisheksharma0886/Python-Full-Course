# create a dictionary and find the items and keys present in the dictionary...

# dictionary is the combination of key and there values, seperated with "" : "" this symbol.....
 
marks = {
    "abhishek": 100,
    "ayush": 95,
    "rahul": 88,
    "sachin": 23,
    0 : "Ranjan"
}

# item() :-  thhis keywords helps to fing the all items present in the dictionary....

print(marks.items())  

# key() :- this keywords helps to find the keys that are present in the dictionary....

print(marks.keys())  

# update() :- this keywords helps to update the elements of the dictionary and ans also add the new elements in the dictionary .....


marks.update({"abhishek": 97})
print(marks)

# marks["key_name"] :- this keywords helps to find the value of the key present in the dictionary....

print(marks["abhishek"])