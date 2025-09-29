# contains general function that an encoder needs
import constants,math

def determine_smallest_version(data:str,level:str,encoding_type:str) -> str:
        '''Determines the  smallest version of QR Code needed'''
        for version in constants.STORAGE_CAPACITIES.keys():
            if constants.STORAGE_CAPACITIES[version][level][encoding_type] >= len(data):
                 return version
            else:
                raise NotImplementedError("Cannot Encode this input, It has exceed the maximum characters that can be encoded.")
        else:
             raise NotImplementedError("Data is too long!")

def _encode_numeric_type(data:str) -> str:
    '''Encodes numeric data by the rules'''

    # breaking up string in the groups of three
    groups = [data[i:i+3] for i in range(0,len(data),3)]
    
    # converting each group into binary
    groups_in_binary = []

    for group_data in groups:
        _ = (bin(int(group_data))[2:])

        if len(group_data) == 1:
         groups_in_binary.append(_.zfill(4))

        elif len(group_data) == 2:
         groups_in_binary.append(_.zfill(7))
        
        else:
            groups_in_binary.append(_.zfill(10))

    return "".join(groups_in_binary)

def _encode_alphanumeric_type(data:str) -> str:
    '''Encodes alphanumeric data by the rules'''
    
    # breaking the string into pair
    pairs = [data[i:i+2] for i in range(0,len(data),2)]
    
    pairs_in_binary = []

    for pair in pairs:
        if len(pair) ==2:
              pairs_in_binary.append(bin(constants.ALPHA_NUMERIC.index(pair[0]) * 45 + constants.ALPHA_NUMERIC.index(pair[1]))[2:].zfill(11))
        else:
             pairs_in_binary.append(bin(constants.ALPHA_NUMERIC.index(pair))[2:].zfill(6))
    
    return "".join(pairs_in_binary)
              
def _encode_byte(data:str) -> str:
    '''Encodes byte data by the rules'''
    data_utf8 = data.encode(errors="ignore") # encoding into UTF-8
    data_bytes = [bin(i)[2:].zfill(8) for i in data_utf8] # each byte into its binary

    return "".join(data_bytes)
    

def get_terminator(version:str,error_level:str,data:str)-> str:
    '''
        Figures out the total number of required number of bits used as terminator
        `data` needs to be the complete data
    
    '''
    total_number_of_bits = constants.TOTAL_NUMBERS_CODEWORDS[version+"-"+error_level] * 8
    
    remaining_bits = total_number_of_bits - len(data)
    terminator_size = min(4, remaining_bits)

    return "0" * terminator_size

def get_padded_string(string:str,error_level:str,version:str)-> str:
        ''' Returns a padding string to make a multiple of 8 and adds remaning pad bytes'''
        total_number_of_bits = constants.TOTAL_NUMBERS_CODEWORDS[version+"-"+error_level] * 8

        until_multiple_8 = (8*math.ceil(len(string) / 8)) - len(string)
        string += "0"*until_multiple_8

        remaining_padding_iteration = (total_number_of_bits - len(string)) // 8

        string+="".join([constants.PADDINGS[(0 if i%2==0 else 1)] for i in range(0,remaining_padding_iteration)])

        return string








encode_data = {""
     'numeric':_encode_numeric_type,
     'alphanumeric':_encode_alphanumeric_type,
     'byte':_encode_byte
}