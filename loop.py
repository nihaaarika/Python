#for loops: Repeat actions for each item in a sequence or for a specific number of times
#while loops: Repeat actions as long as certain condition remains true

for i in range(10):
    print("Hello Niharika") # For loop

fruits= ["Apple", "Banana", "Mango", "Orange"]
for i in fruits:
    print("Fruit is", i)

for num in range(2, 14):
    print("i=", num)    

num= [10, 20, 30, 40, 50] 
total= 0
for i in num:
    total+= i
    print("sum:", total)   