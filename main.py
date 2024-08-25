# Realease 1 Creating the base chess board and downloading the piceas 

import pygame 
pygame.init()

Width = 1000
Height = 900
screen = pygame.display.set_mode([Width,Height])
pygame.display.set_caption('Two-Player Chess Game :)')
font = pygame.font.Font('freesansbold.ttf',20)
big_font = pygame.font.Font('freesansbold.ttf',50)
timer = pygame.time.Clock()
fps = 60


# Setting up my variables for my chess piceas and adding the coordinates on the board  
white_pieces = ['rook', 'knight','bishop','king','queen','bishop','knight','rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                   (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
black_pieces = ['rook', 'knight','bishop','king','queen','bishop','knight','rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                   (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]

captured_pieces_white = []
captured_pieces_black = []


# TURN Variable tracks where the user is at in the game : 0 white no selection , 1 white turn picea selected, 2 black turn no selection , 3 black turn piece selected 
turn_step = 0
selection = 100
valid_moves = []


# LOADING IN AND SIZING THE CHESS PIECES
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
# The small piceas I'm using here will be used to represent the piceas on the side of the board that have been beaten that is why they are small
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen' , 'king','knight','rook','bishop']

# insert a check variable and flashing counter here 



# DRAWING MY CHESS BOARD
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray',[600 -(column * 200), row * 100, 100,100])
        else:
            pygame.draw.rect(screen, 'light gray',[700 -(column * 200), row * 100, 100,100])
        pygame.draw.rect(screen, 'gray', [0,800,Width,100]) # bottom menu outline
        pygame.draw.rect(screen, 'gold', [0,800,Width,100], 5)
        pygame.draw.rect(screen, 'gold', [800,0,200,Height], 5) # side menu outline
        status_text = ['white: select your piece','white: select a destination',
                       'black: select your piece','black: select a destination']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black',(0,100 * i),(800,100 * i), 2)
            pygame.draw.line(screen, 'black',(100 * i ,0),(100 * i,800), 2)

# DRAWING MY CHESS PIECES
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1]* 100 + 30))
        else :
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1]* 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red',[white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,100,100],2)

        

    
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1]* 100 + 30))
        else :
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1]* 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue',[black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,100,100],2)

# CREATING a function here that checks all the valid options for a piece on the board
def check_options():
    pass

# THE MAIN GAME LOOP

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
# Event Handling 
    for event  in pygame.event.get():
        # event where pygame crashes and quits 
        if event.type == pygame.QUIT:
            run = False
        # event where user succefully clicks on the screen aswell as fetching the coordinates of where the user clicks on the screen
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord,y_coord)
            
            # CODE for if its WHITES turn 
            if turn_step <= 1:
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves  and selection !=100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        # REMOVES THE BLACK PICEA FROM THE BOARD WHEN A WHITE PICEA LANDS ON IT I.E removes it from the black piceas list if its been captured
                        black_pieces.pop(black_piece) 
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces,black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100 
                    valid_moves = []# clears out the valid moves list everytime its a new turn

                    # CODE for if its BLACKS turn 
            if turn_step > 1:
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves  and selection !=100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece) 
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces,black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0 # goes back to whites turn after black has moved its piece
                    selection = 100 
                    valid_moves = []


    pygame.display.flip()
pygame.quit()