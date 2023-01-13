def fibo(n):
    if n <= 1:
        return (n)
    else:
        return (fibo(n-1) + fibo(n-2))


print("Fibo")
print("Sebastian Alchimowicz")
print("Grupa: I2S 2.1")
getW = input('Podaj liczbe: ')
getW = int(getW)
print("")

for i in range(getW):
    if i == (getW-1):
        print(fibo(i+1))
