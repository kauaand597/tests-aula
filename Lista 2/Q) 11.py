numero = int(input("Número: "))

if numero % 3 ==0 and numero % 5==0:
    print("FizzBuzz")
elif numero % 3 ==0:
    print("Fizz")
else:
    if numero % 5 ==0:
        print("Buzz")


