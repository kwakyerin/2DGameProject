from pico2d import load_image

class stage_02_1:
    def __init__(self):
        self.Tile_01=load_image('Map_02/Purple_Cloud/PCloud_03.png')
        pass

    def draw(self):
        self.Tile_01.draw(40,500,130,50)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False