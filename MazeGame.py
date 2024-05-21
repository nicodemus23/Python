import pygame
import time
import random

pygame.init()

# window
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height)) # set the window size

pygame.display.set_caption("Get Away Maze") # set the window title

# colors
black = (0, 0, 0)
white = (255, 255, 255)
purple = (128, 0, 128)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# maze layout
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # row 0
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # row 16
]   # columns: 20, rows: 17

cell_size = 41
maze_position = (10, 10) # adjust the maze position to center it on the screen

# player start position
player_x = 1
player_y = 1

# jailed person position
cube_x = 10
cube_y = 10

# police characters
police_positions = []
police_speed = 0.5
police_flash_timer = 0
police_flash_interval = 30

# game state
running = True 
move_up = False
move_down = False
move_left = False
move_right = False
cube_rescued = False
game_won = False
game_over = False
game_over_reason = ""

# timer
timer_duration = 60 # 60 seconds
timer_start = time.time()

# UI positions
title_area = (window_width - 392, 20, 370, 60)
info_area = (window_width - 380, 90, 350, 600)

# font
font_path = "C:/Windows/Fonts/orbitron.ttf"
title_font = pygame.font.SysFont("Orbitron-ExtraBold", 50)
font = pygame.font.SysFont("Orbitron-Medium", 36)

# draw text with word wrap
def draw_text(surface, text, color, rect, font):
    words = text.split() # split the text into words
    lines = []
    current_line = ""
    for word in words:
        if font.size(current_line + " " + word)[0] < rect[2] - 20:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    y = rect[1] + 8
    for line in lines:
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (rect[0] + 12, y)) # https://realpython.com/lessons/using-blit-and-flip/#:~:text=blit()%20is%20how%20you,Surface%20%2C%20that's%20not%20a%20problem.
        y += font.get_height() # move down one line
    
# resets the game when the player wins or loses (resets the player and cube positions)
def reset_game():
    global player_x, player_y, cube_x, cube_y, cube_rescued, game_won, game_over, timer_start, police_positions
    player_x = 1
    player_y = 1
    cube_x = 10
    cube_y = 10
    cube_rescued = False
    game_won = False
    game_over = False
    timer_start = time.time()
    police_positions = []
    game_over_reason = ""  # Reset the game over reason

# frame rate (helps controls the speed of the game and player movement)
clock = pygame.time.Clock()
frame_rate = 10 # 10 frames per second

# main game loop
while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # player movement (WASD) Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and maze[player_y-1][player_x] != 1:  # up
                move_up = True
            elif event.key == pygame.K_s and maze[player_y+1][player_x] != 1:  # down
                move_down = True
            elif event.key == pygame.K_a and maze[player_y][player_x-1] != 1:  # left
                move_left = True
            elif event.key == pygame.K_d and maze[player_y][player_x+1] != 1:  # right
                move_right = True
            elif event.key == pygame.K_RETURN and (game_over or game_won):  # Enter key to restart the game
                reset_game()
                
        # check for KEYUP event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_s:
                move_down = False
            elif event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False
                
    # move player based on key press (keeps the player moving as long as the key is pressed - better than single key press check)
    #If the player's position -/+ 1 is 0, then the player can move to that cell (part of the path)
    if move_up and maze[player_y-1][player_x] != 1:
        player_y -= 1  # new player position
    if move_down and maze[player_y+1][player_x] != 1:
        player_y += 1
    if move_left and maze[player_y][player_x-1] != 1:
        player_x -= 1
    if move_right and maze[player_y][player_x+1] != 1:
        player_x += 1
        
    # check if player has rescued the cube
    if player_x == cube_x and player_y == cube_y:
        cube_rescued = True
        #police_positions = [(1 * cell_size, 1 * cell_size), (1* cell_size, 18 * cell_size), (16 * cell_size, 1 * cell_size), (16 * cell_size, 18 * cell_size)]
        police_positions = [(1, 1), (1, 16), (15, 1), (15, 11)]
        
    # move cube with player (if cube is rescued)
    if cube_rescued:
        if move_up and maze[cube_y-1][cube_x] != 1:
            cube_y -= 1
        if move_down and maze[cube_y+1][cube_x] != 1:
            cube_y += 1
        if move_left and maze[cube_y][cube_x-1] != 1:
            cube_x -= 1
        if move_right and maze[cube_y][cube_x+1] != 1:
            cube_x += 1
            
    for i in range(len(police_positions)):
        police_row, police_col = police_positions[i]  # get the row and column position of the police
        if cube_rescued:
            # Check if the police can move right
            if police_col < cube_x and police_col + 1 < len(maze[0]) and maze[police_row][police_col + 1] != 1:
                police_col += 1
            # Check if the police can move left
            elif police_col > cube_x and police_col - 1 >= 0 and maze[police_row][police_col - 1] != 1:
                police_col -= 1
            # Check if the police can move down
            if police_row < cube_y and police_row + 1 < len(maze) and maze[police_row + 1][police_col] != 1:
                police_row += 1
            # Check if the police can move up
            elif police_row > cube_y and police_row - 1 >= 0 and maze[police_row - 1][police_col] != 1:
                police_row -= 1

            # This is very basic collision detection
            if police_row == cube_y and police_col == cube_x:
                cube_rescued = False
                cube_x = 10
                cube_y = 10
                game_over = True
                game_over_reason = "arrested"
        police_positions[i] = (police_row, police_col)
            
    # timer logic
    # current_time = time.time()
    # elapsed_time = current_time - timer_start
    # remaining_time = max(timer_duration - elapsed_time, 0) # max function to prevent negative time
    if not game_over and not game_won:
        current_time = time.time()
        elapsed_time = current_time - timer_start
        remaining_time = max(timer_duration - elapsed_time, 0)
    
    # check if the timer has run out
    if remaining_time == 0 and not game_won:
        game_over = True
        game_over_reason = "timeout"
            
    # check if the player made it to the exit with the cube
    if maze[player_y][player_x] == 2 and cube_rescued:
        game_won = True
    
    # bg color
    window.fill(purple)
    
    # draw maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            cell_color = black if maze[row][col] == 1 else white
            if maze[row][col] == 2:
                cell_color = yellow  # this is the exit cell 
            x = col * cell_size + maze_position[0]  # x position of cell
            y = row * cell_size + maze_position[1]  # y position of  cell
            pygame.draw.rect(window, cell_color, (x, y, cell_size, cell_size))  # <-player path / rect: surface, color, (x, y, width, height)
                
    # draw player
    pygame.draw.circle(window, green, (player_x * cell_size + cell_size//2 + maze_position[0], player_y*cell_size + cell_size//2 + maze_position[1]), cell_size//4)
    
    # draw cube
    pygame.draw.rect(window, red, (cube_x * cell_size + maze_position[0], cube_y*cell_size + maze_position[1], cell_size, cell_size))
    
    # popo flasher timer
    police_flash_timer += 2
    if police_flash_timer >= police_flash_interval:
        police_flash_timer = 0
    
    for police_row, police_col in police_positions:
        police_x = police_col * cell_size + maze_position[0]
        police_y = police_row * cell_size + maze_position[1]
        if police_flash_timer < police_flash_interval // 2:
            pygame.draw.polygon(window, red, [
                (police_x, police_y),
                (police_x + cell_size // 2, police_y + cell_size),
                (police_x + cell_size, police_y)
            ])
        else:
            pygame.draw.polygon(window, blue, [
                (police_x, police_y),
                (police_x + cell_size // 2, police_y + cell_size),
                (police_x + cell_size, police_y)
            ])
    
    # draw GUI
    pygame.draw.rect(window, black, title_area)
    pygame.draw.rect(window, black, info_area)
    
    # outline for graphic elements
    pygame.draw.rect(window, white, title_area, 2)  # outline for title
    pygame.draw.rect(window, white, info_area, 2)  # outline for info box
    pygame.draw.rect(window, white, (maze_position[0]-2, maze_position[1]-2, cell_size*len(maze[0])+4, cell_size*len(maze)+4), 2)  # outline for maze
    
    draw_text(window, "Maze Game", white, title_area, title_font)
    draw_text(window, f"Time: {int(remaining_time)}", white, (info_area[0], info_area[1], info_area[2], 40), font)
    
    # if game_won:
    #     #draw_text(window, "You Win!", white, (info_area[0], info_area[1] + 20, info_area[2], 40)) 
    #     draw_text(window, "You got away!", green, (info_area[0], info_area[1] + 40, info_area[2], info_area[3] - 40), font)

    #     draw_text(window, "Press Enter to play again", white, (info_area[0], info_area[1] + 80, info_area[2], info_area[3] - 80), font)

    if game_won:
        draw_text(window, "You got away! Press Enter to play again.", green, (info_area[0], info_area[1] + 40, info_area[2], info_area[3] - 40), font)
    
    if game_over:
        if game_over_reason == "arrested":
            draw_text(window, "You lost! The cube was re-arrested. Press Enter to play again.", red, (info_area[0], info_area[1] + 40, info_area[2], info_area[3] - 40), font)
        elif game_over_reason == "timeout":
            draw_text(window, "You lost! Time's up. Press Enter to play again.", red, (info_area[0], info_area[1] + 40, info_area[2], info_area[3] - 40), font)

    
    # update display
    pygame.display.update()
    clock.tick(frame_rate) # set the frame rate (10 frames per second - runs every 0.1 seconds)
    
pygame.quit() # quit pygame