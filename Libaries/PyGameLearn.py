import pygame
#initialise pygame modules: NEEDED
pygame.init()

#create display:
display = pygame.display.set_mode((1280,720))
display.fill("White")
tile_size = (32)
screen_height = 1280
screen_width = 720
grid_color = (200, 200, 200)

#creating tile logic:
def draw_tile_map(surface, tile_size):
    collums = surface.get_width() // tile_size
    rows = surface.get_hight() // tile_size
    #creates collums
    for x in range (collums + 1):
        pygame.draw.line(surface, grid_color, (x * tile_size, 0),
        (x * tile_size, surface.get_height()))
    #creates rows
    for y in range (rows + 1):
        pygame.draw.line(surface, grid_color, (0, y * tile_size, 0),
        (surface.get_width(), y * tile_size))

def get_tile_at_pos(pos, tile_size):
    #return the col and row of a tile at a given pixel:
    x, y = pos
    return x // tile_size, y // tile_size

def main():
    pygame.init()
    display = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Pygame Tile Grid For Chess")
    clock = pygame.time.Clock()

    selected_tiles = set()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Uses mouse clicks to return the position of the row and collum of the click (used to find what piece is at which row, colum, will be stored in a dictionary :piece:position)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    tile = get_tile_at_pos(event.pos, tile_size)
                    if tile in selected_tiles:
                        selected_tiles.remove(tile)
                    else:
                        selected_tiles.add(tile)

        # --- Drawing ---
        
        draw_tile_map(display, tile_size)

        # Highlight selected tiles
        for col, row in selected_tiles:
            rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
            pygame.draw.rect(display, (255, 100, 100), rect)

        pygame.display.flip()
        clock.tick(60)


#chess logic:

#create pieces:
class Pieces():
    



if __name__ == "__main__":
    main()