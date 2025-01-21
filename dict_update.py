marks = {
    "abhishek": 100,
    "ayush": 95,
    "rahul": 88,
    "sachin": 23
}


marks.update({"abhishek": 65, "pankaj": 43})

print(marks)

print(marks.values())

print(marks.get("abhishek"))
print(marks.get("Abhilasha"))

print(marks["abhishek"])
marks.clear()


print(marks)