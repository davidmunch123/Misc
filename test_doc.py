def splitint(number):
    """
    Splits an integer into a list of its digits. 

    Parameters 
    --------- 
    number: int 
        Any integer. 

    Return
    ------ 
    List
        List  of the digits of the int in order from least to greatest. 
    
    """
    arr = []
    for i in str(number):
        number_1 = number % 10 
        arr.append(int(number_1)) 
        number -= number_1 
        number /= 10 
    arr.sort()
    return arr


print(splitint(int(input())))