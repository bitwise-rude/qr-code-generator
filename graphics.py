import pygame

class Renderer:
    HEIGHT = 800
    WIDTH = 600
    BLOCK_SIZE = 40 # block means the individual square of a QR code, and size since it is a square

    def __init__(self,qr_size):
        self.size_qr= qr_size

        pygame.init()
        pygame.display.init()

        
        self.screen = pygame.display.set_mode((Renderer.HEIGHT,Renderer.WIDTH))
        pygame.display.set_caption("QR CODE")


    def pass_control(self) -> None:
        self.running = True

        while self.running:
            for evs in pygame.event.get():
                if evs.type == pygame.QUIT:
                    self.running = False
        
        pygame.quit()
        return
    


