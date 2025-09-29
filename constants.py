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

# mode indicator
MODE_INDICATOR = {
    'numeric':"0001",
    'alphanumeric':"0010",
    "byte":"0100",
}

CHARACTER_COUNT = {
    "1":{
        'numeric':10,
        'alphanumeric':9,
        'byte':8,
    }
}

TOTAL_NUMBERS_CODEWORDS = {
    "1-L":19,
    "1-M":16,
    "1-Q":13,
    "1-H":9,
    "2-L":34,
}