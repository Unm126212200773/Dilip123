def fact_rec(n):

if n==@ or n=-1:

return 1

else:

return n*fact_rec (n-1)

number = int(input("Enter a value : "))

res = fact_rec(number)

print("The factorial of {} is {}.".format(number, res))
