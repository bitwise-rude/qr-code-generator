# contains system to manage error correction

# https://www.thonky.com/qr-code-tutorial/error-correction-coding#step-2-understand-polynomial-long-division

# i have used steps mentioned here as the actual function names

def get_coefficients_from_data(data:str) ->list[int]:
    ''' Returns a lists of integer formed by taking 8 bits at a time from the data'''
    return [int(data[i:i+8],2) for i in range(0,len(data),8)]

def gf_mul(x, y):
    """Multiply two numbers in GF(256)."""
    r = 0
    while y:
        if y & 1:
            r ^= x
        x <<= 1
        if x & 0x100:  # if overflow
            x ^= 0x11d  # reduce modulo the primitive polynomial
        y >>= 1
    return r

def gf_pow(x, power):
    """Compute x^power in GF(256)."""
    r = 1
    for _ in range(power):
        r = gf_mul(r, x)
    return r

def rs_generator_poly(nsym):
    """Generate generator polynomial for nsym EC codewords."""
    g = [1]
    for i in range(nsym):
        # multiply g(x) by (x - α^i)
        g_next = [0] * (len(g) + 1)
        for j in range(len(g)):
            g_next[j] ^= gf_mul(g[j], gf_pow(2, i))  # constant term
            g_next[j+1] ^= g[j]                      # x term
        g = g_next
    return g
    

def get_mul_coefficient_generator(g,lead_coeff):
    coeff = [gf_mul(c, lead_coeff) for c in g]
    coeff.reverse()
    return coeff
 


class ThonkySteps:
    ''' 
        https://www.thonky.com/qr-code-tutorial/error-correction-coding#step-2-understand-polynomial-long-division 
        use perfrom function to add data 
        generator is assumed to have crossed the step 1a
    '''
    def perfrom(message:list[int],n:int) -> None:
        # this is step_1b
        # XORing everything
        # print(len(message),len(generator))
        going = len(message)
        
        stuff = rs_generator_poly(n)
        leader = 32
        for i in range(going):
            got = (get_mul_coefficient_generator(stuff,leader))
            message = [i^j for i,j in zip(message + [0]*(len(got) - len(message)),got+[0]*(len(message)-len(got)))]
            message = message[1:]
            leader = message[0]
           
        return message