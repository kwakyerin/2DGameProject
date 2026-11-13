from pico2d import load_image

class stage_01:
    def __init__(self):
        self.tile_01=load_image('Map_01/Green_Grass/Tile_01.png')
        pass

    def draw(self):
        self.tile_01.draw(550, 0, 1250, 367)
        pass

    def update(self):
        pass