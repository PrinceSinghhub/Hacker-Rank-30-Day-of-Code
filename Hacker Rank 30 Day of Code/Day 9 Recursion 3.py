def factorial(n,ans):

    if n < 1:
        return ans

    ans *= n

    return factorial(n-1,ans)



print(factorial(3,1))