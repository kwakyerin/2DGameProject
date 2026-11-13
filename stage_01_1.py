from pico2d import load_image

class stage_01_1:

    def __init__(self):
        self.Tile_01=load_image('Map_01/DGreen_Grass/Tile_04.png')
        pass

    def draw(self):
        self.Tile_01.draw(550,0,1250,367)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_y):
        character.on_ground = False
