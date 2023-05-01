#The break statement terminates a for loop completely

print("Break Statement")
for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break

'''The continue statement terminates execution of the statements 
within a for loop and continues the loop in the next iteration'''

print("Continue Statement")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)     