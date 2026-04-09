def square_and_multiply(base,exponent,modulus):  # fun fact the pow() function is C realization of this algorithm
    result = 1  # result is 1 because it does not affect other multiplications
    base = base % modulus  # initial values
    while exponent>0:  # this condition because we will right shift exponent until it becomes 0
        if exponent%2!=0:  # it shows that lower bit is 1
            result = (result * base)%modulus  # if our result has reminder it means that our rightmost bit = 1
        exponent = exponent >> 1  # that is rightshift (We've could write just exponent//=exponent thou) выпендрёж
        base = (base * base)%modulus  # raise it to the power of two and give it to the next person
    return result
