
print("""if the number is divisible by 3, it will print Fizz
if the number is divisible by 5, it will print Buzz
if the number is divisible by 3 and 5, it will print Fizz Buzz
""")
      
    
number = int(input('Enter number: '))

if number % 3 == 0 and number % 5 == 0:
    print('Fizz Buzz')

elif number % 3 == 0:
    print('Fizz')

elif number % 5 == 0:
    print('Buzz')
else:
    print('The number is not divisible by 3 or 5')
    