from pico2d import load_image

class bossmap:
    def __init__(self):
        self.image=load_image('Map_03/gray_space/G_Tile_11.png')
        pass

    def draw(self):
        self.image.draw(550,10,1200,300)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        pass