# contains general function that an encoder needs
import constants

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
                
    return groups_in_binary

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
    
    return pairs_in_binary
              
def _encode_byte(data:str) -> str:
    '''Encodes byte data by the rules'''
    data_utf8 = data.encode(errors="ignore") # encoding into UTF-8
    data_bytes = [bin(i)[2:].zfill(8) for i in data_utf8] # each byte into its binary

    return data_bytes
    
    

encode_data = {""
     'numeric':_encode_numeric_type,
     'alphanumeric':_encode_alphanumeric_type,
     'byte':_encode_byte
}