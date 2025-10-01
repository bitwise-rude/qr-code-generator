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
    
    lead_coeff = 32
    coeff = [gf_mul(c, lead_coeff) for c in g]
    coeff.reverse()
    return coeff


class ThonkySteps:
    def perfrom(message:list[int], generator:list[int]) -> None:
        pass