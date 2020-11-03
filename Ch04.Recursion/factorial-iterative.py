def factorial(num: int) -> int:
    result: int = 1
    while num > 1:
        result *= num
        num -= 1
    return result
    
 print(factorial(1))
 print(factorial(5))
