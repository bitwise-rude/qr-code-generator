import constants

class Encoder:
    '''Manages the encoding of the input to respective correct data type '''
    def choose_most_efficient_mode(data:str) -> "Encoder":
        '''Chooses the most efficient mode'''
        try:
            int(data)  # check for numeric
            return Encoder("numeric")
        except ValueError:
            # checking every word if it is alphanumeric
            for letter in data:
                if not letter in constants.ALPHA_NUMERIC:
                    return Encoder('byte') # if not in there, then it is byte mode
            # if nothing is byte then 
            return Encoder("alphanumeric")
    
    def __init__(self,encoding_type:str) -> None:
        self.encoding_type = encoding_type

        # check if some other type is there
        if self.encoding_type not in ('numeric','byte','alphanumeric'):
            raise NotImplementedError("Not implemented for this type")
        
        # TODO: make implementation for other error correction level
        self.error_correction_level = "M" # 15% of data is recovered
        