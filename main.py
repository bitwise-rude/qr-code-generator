from encoder import Encoder

def get_input() -> str:
    '''Gets input from the user and returns the input'''
    return "12121"

encoder = Encoder.choose_most_efficient_mode(get_input())

print(encoder.encoding_type)