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
    groups_in_binary = [bin(int(i))[2:] for i in groups]    
    return "".join(groups_in_binary)

def _encode_alphanumeric_type(data:str) -> str:
    '''Encodes numeric data by the rules'''
    print("A")
    

encode_data = {""
     'numeric':_encode_numeric_type,
     'alphanumeric':_encode_alphanumeric_type,
}