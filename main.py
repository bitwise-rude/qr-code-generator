from encoder import Encoder

def get_input() -> str:
    '''Gets input from the user and returns the input'''
    return "HELLO WORLD"

encoder = Encoder.choose_most_efficient_mode(get_input())

