from pico2d import load_image

class stage_03:
    def __init__(self):
        self.Tile_01=load_image('Map_03/purple_space/P_Tile_01.png')
        pass

    def draw(self):
        self.Tile_01.draw(500,300,300,100)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False