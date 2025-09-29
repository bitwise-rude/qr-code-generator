import string

# alpha numeric character contained in a string
ALPHA_NUMERIC = "".join([str(i) for i in range(10)])+ string.ascii_uppercase+" $%*+-./:"

# character capacities in different modes with correction level
STORAGE_CAPACITIES = {
    "1":{

        "L":{
            "numeric":41,
            "alphanumeric":25,
            "byte":17
            },
        
        "M":{
            "numeric":34,
            "alphanumeric":20,
            "byte":14
        },
        
         "Q":{
            "numeric":27,
            "alphanumeric":16,
            "byte":11
        },
        
         "H":{
            "numeric":17,
            "alphanumeric":10,
            "byte":7
        },
        

        }
    }
