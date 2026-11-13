from pico2d import load_image

class stage_01:
    def __init__(self):
        self.tile_01=load_image('Map_01/Green_Grass/Tile_01.png')
        self.tile_02=load_image('Map_01/Green_Grass/Tile_02.png')
        self.tile_03=load_image('Map_01/Green_Grass/Tile_03.png')
        self.tile_04=load_image('Map_01/Green_Grass/Tile_04.png')
        self.tile_05=load_image('Map_01/Green_Grass/Tile_05.png')
        pass

    def draw(self):
        self.tile_01.draw(550, 0, 1250, 367)
        self.tile_03.draw(700, 150, 600, 230)
        self.tile_04.draw(200,250,400,200)
        self.tile_05.draw(450,350,400,200)
        self.tile_02.draw(800,450,600,250)
        pass

    def update(self):
        pass