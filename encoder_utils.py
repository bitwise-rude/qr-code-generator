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