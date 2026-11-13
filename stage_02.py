from pico2d import load_image

class stage_02:
    def __init__(self):
        self.grass=load_image('Map_02/DGrass/Tile_01.png')
        pass

    def draw(self):
        self.grass.draw(30,0,400,200)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_y):
        character.on_ground = False