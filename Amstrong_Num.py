'''Armstrong number is the number in any given number base, 
which forms the total of the same number, when each of its digits is
 raised to the power of the number of digits in the number '''

num = int(input("Enter a number: "))
 
sum = 0 
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
