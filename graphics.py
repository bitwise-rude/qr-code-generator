import pygame,constants

class Renderer:
    HEIGHT = 600
    WIDTH = 600
    BLOCK_SIZE = 5 # block means the individual square of a QR code, and size since it is a square

    def __init__(self,qr_version:int):
        self.qr_version = qr_version

        self.size_qr= (((self.qr_version-1)*4)+21)

        pygame.init()
        pygame.display.init()

        self.screen = pygame.display.set_mode((Renderer.HEIGHT,Renderer.WIDTH))
        pygame.display.set_caption("QR CODE")
        self.screen.fill((20,255,20))
        pygame.display.update()

        self.block_initial_y= (Renderer.HEIGHT - Renderer.BLOCK_SIZE *self.size_qr)//2 # placing the first block, in such way at the end the qr code will be in perfect center of teh screen
        self.block_initial_x = (Renderer.WIDTH - Renderer.BLOCK_SIZE *self.size_qr)//2 # placing the first block, in such way at the end the qr code will be in perfect center of teh screen

        self.control_matrix = [[.2 for _ in range(self.size_qr)] for _ in range(self.size_qr)]

    def draw_functional_element(self):
        """Draw finder patterns (top-left, top-right, bottom-left)."""

        def place_finder(top, left):
            """Stamp a 7x7 finder pattern at (top,left). and alos the separator"""
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
            
            # separator
            # top
            if top - 1 >=0:
                for i in range(8):
                    self.control_matrix[top-1][left + i] = 1 
            
            # right
            if left+7 < self.size_qr:
                for i in range(7):
                    self.control_matrix[top+i][left+7] = 1
            
            # bottom
            if top + 7 < self.size_qr:
                for i in range(7):
                    self.control_matrix[top+7][left+i] = 1
            
                if  left-1 >=0: # only happens for right
                    self.control_matrix[top+7][left-1] = 1
                    for i in range(7):
                        self.control_matrix[top+i][left-1] = 1

                if left+7 <self.size_qr:
                    self.control_matrix[top+7][left+7] = 1

            


                size = len(self.control_matrix)

                # place in three corners
        place_finder(0, 0)               # top-left
        place_finder(0, self.size_qr-7)          # top-right
        place_finder(self.size_qr-7, 0)          # bottom-left

        self.fill_screen_with_matrix()
                    
        print(self.control_matrix)
        self.fill_screen_with_matrix()

        # now placing alignment pattern
        if self.qr_version >= 2:
    # Only for version up to 6 in your note, but can be extended
            locations = constants.ALIGNMENT_PATTER_LOCATIONS[self.qr_version]

            def place_alignment(center_row, center_col):
                """Stamp a 5x5 alignment pattern centered at (center_row,center_col)."""
                for i in range(-2, 3):   # -2..+2
                    for j in range(-2, 3):
                        r, c = center_row + i, center_col + j
                        # outer border black
                        if abs(i) == 2 or abs(j) == 2:
                            self.control_matrix[r][c] = 0
                        # center black
                        elif i == 0 and j == 0:
                            self.control_matrix[r][c] = 0
                        else:
                            self.control_matrix[r][c] = 1

            # Place all alignment patterns
            for r in locations:
                for c in locations:
                    # skip overlap with finder patterns (corners)
                    if (r <= 6 and c <= 6) or (r <= 6 and c >= len(self.control_matrix)-7) or (r >= len(self.control_matrix)-7 and c <= 6):
                        continue
                    place_alignment(r, c)
            
            # place timing pattern
            # 8th row  and 6th column is where it begins
            color_mode = False
            for i in range(8,self.size_qr-8): 
                self.control_matrix[i][6] = 0 if not color_mode else 1 # verticle one
                self.control_matrix[6][i] = 0 if not color_mode else 1 # horizontal one
                color_mode = not color_mode
            
            # adding the dark module
            self.control_matrix[(4*self.qr_version)+9][8] = 0


        self.fill_screen_with_matrix()

    
    def fill_screen_with_matrix(self):
        '''Fills the screen according to control matrix'''
        for i in range(len(self.control_matrix)):
            for j in range(len(self.control_matrix[i])):
                self.fill((j,i),self.control_matrix[i][j])

    def fill(self,index:tuple[int,int],white_:int) -> None:
        '''Fills the block at 'index' white_ or not_white'''
        # print(self.X(index[0]),self.Y(index[1]),Renderer.BLOCK_SIZE,Renderer.BLOCK_SIZE)
        if white_==1:
            color = (255,255,255)
        elif white_ ==0:
            color = (0,0,0)
        elif white_ == 0.2:
            color =(255,0,0)
        elif white_ == 0.5:
            color = (0,0,255) # indicated reserved area
        pygame.draw.rect(self.screen,color,(self.X(index[0]),self.Y(index[1]),Renderer.BLOCK_SIZE,Renderer.BLOCK_SIZE))
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
    


