from encoder import Encoder
from graphics import Renderer

def get_input() -> str:
    '''Gets input from the user and returns the input'''
    return "HELLO WORLD"

encoder = Encoder.choose_most_efficient_mode(get_input())
encoded_string = encoder.encode() # perform the encoding steps

rendering_element = Renderer(2)
rendering_element.draw_functional_element()
rendering_element.pass_control() # now rendering element will get the control and maybe go in an infinite loop