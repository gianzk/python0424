def sumar(n):
    if n==1:
        return 1
    else:
        return n+sumar(n-1)


print(sumar(100))

#factorial m*m-1
def factorial(m):
    if m!=1:
        return m*factorial(m-1)
    else:
        return 1

print(factorial(120))



#n=1+2+3+4+5+6+7+8+9.............+n
#S10=10+suma(9)
#S1= 10+9+sum(8)
#..
#S1= 10+9+8........suma(1)