import constants
from encoder_utils import * 

class Encoder:
    '''Manages the encoding of the input to respective correct data type '''
    def choose_most_efficient_mode(data:str) -> "Encoder":
        '''Chooses the most efficient mode'''
        try:
            int(data)  # check for numeric
            return Encoder("numeric",data)
        except ValueError:
            # checking every word if it is alphanumeric
            for letter in data:
                if not letter in constants.ALPHA_NUMERIC:
                    return Encoder('byte',data) # if not in there, then it is byte mode
            # if nothing is byte then 
            return Encoder("alphanumeric",data)
    
    def __init__(self,encoding_type:str,data:str) -> None:
        self.encoding_type = encoding_type
        self.data = data

        # check if some other type is there
        if self.encoding_type not in ('numeric','byte','alphanumeric'):
            raise NotImplementedError("Not implemented for this type")
        
        # TODO: make implementation for other error correction level
        self.error_correction_level = "M" # 15% of data is recovered

        self.best_version = determine_smallest_version(self.data,self.error_correction_level,self.encoding_type)
        

    


        