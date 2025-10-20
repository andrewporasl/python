def my_steps(n:int) -> int:
    if n < 1 or n > 25:
        raise ValueError("n must be between 1 and 25")
    
    if n == 1:
        return 1   
    if n == 2:
        return 2    
    a, b = 1, 2
    
    
    
    for _ in range(3, (n + 1)):
        a, b = b, a + b
    return b