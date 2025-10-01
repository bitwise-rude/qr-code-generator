# contains system to manage error correction

def get_coefficients_from_data(data:str) ->list[int]:
    ''' Returns a lists of integer formed by taking 8 bits at a time from the data'''
    return [int(data[i:i+8],2) for i in range(0,len(data),8)]