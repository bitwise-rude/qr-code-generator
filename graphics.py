import pygame

class Renderer:
    HEIGHT = 600
    WIDTH = 600
    BLOCK_SIZE = 20 # block means the individual square of a QR code, and size since it is a square

    def __init__(self,qr_size:int):
        self.size_qr= qr_size

        pygame.init()
        pygame.display.init()

        self.screen = pygame.display.set_mode((Renderer.HEIGHT,Renderer.WIDTH))
        pygame.display.set_caption("QR CODE")
        self.screen.fill((20,255,20))
        pygame.display.update()

        self.block_initial_y= (Renderer.HEIGHT - Renderer.BLOCK_SIZE *qr_size)//2 # placing the first block, in such way at the end the qr code will be in perfect center of teh screen
        self.block_initial_x = (Renderer.WIDTH - Renderer.BLOCK_SIZE *qr_size)//2 # placing the first block, in such way at the end the qr code will be in perfect center of teh screen

        self.control_matrix = [[1 for _ in range(qr_size)] for _ in range(qr_size)]

    def draw_functional_element(self):
        """Draw finder patterns (top-left, top-right, bottom-left)."""

        def place_finder(top, left):
            """Stamp a 7x7 finder pattern at (top,left)."""
            for i in range(7):
                for j in range(7):
                    # outer border
                    if i in (0,6) or j in (0,6):
                        self.control_matrix[top+i][left+j] = 0
                    # inner 3x3 black square
                    elif 2 <= i <= 4 and 2 <= j <= 4:
                        self.control_matrix[top+i][left+j] = 0
                    else:
                        self.control_matrix[top+i][left+j] = 1

                size = len(self.control_matrix)

                # place in three corners
        place_finder(0, 0)               # top-left
        place_finder(0, self.size_qr-7)          # top-right
        place_finder(self.size_qr-7, 0)          # bottom-left

        self.fill_screen_with_matrix()
                    
        print(self.control_matrix)
        self.fill_screen_with_matrix()
    
    def fill_screen_with_matrix(self):
        '''Fills the screen according to control matrix'''
        for i in range(len(self.control_matrix)):
            for j in range(len(self.control_matrix[i])):
                self.fill((j,i),self.control_matrix[i][j])

    def fill(self,index:tuple[int,int],white_:bool) -> None:
        '''Fills the block at 'index' white_ or not_white'''
        # print(self.X(index[0]),self.Y(index[1]),Renderer.BLOCK_SIZE,Renderer.BLOCK_SIZE)

        pygame.draw.rect(self.screen,((255,255,255) if white_ else (0,0,0)),(self.X(index[0]),self.Y(index[1]),Renderer.BLOCK_SIZE,Renderer.BLOCK_SIZE))
        pygame.display.update()

    def X(self,i:int) -> int:
        '''Gives the coordinate for i element of row'''
        return self.block_initial_x + Renderer.BLOCK_SIZE * i


    def Y(self,j:int) -> int:
        ''' Gives the coordinate for j element of  column'''
        return self.block_initial_y + Renderer.BLOCK_SIZE * j

    def pass_control(self) -> None:
        self.running = True

        while self.running:
            for evs in pygame.event.get():
                if evs.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
        pygame.quit()

        return
    


