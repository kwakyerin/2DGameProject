from pico2d import load_image

class stage_02_1:
    def __init__(self):
        self.Tile_01=load_image('Map_02/Purple_Cloud/PCloud_03.png')
        self.Tile_02=load_image('Map_02/Purple_Cloud/PCloud_05.png')
        self.Tile_03=load_image('Map_02/Purple_Cloud/PCloud_02.png')
        self.Tile_04=load_image('Map_02/Purple_Cloud/PCloud_03.png')
        self.Tile_05=load_image('Map_02/Space/P_Tile_10.png')
        pass

    def draw(self):
        self.Tile_01.draw(45,500,130,50)
        self.Tile_02.draw(300,400,500,50)
        self.Tile_03.draw(800,600,100,50)
        self.Tile_02.draw(600,200,500,50)
        self.Tile_04.draw(200,50,130,50)
        self.Tile_04.draw(100,140,130,50)
        self.Tile_05.draw(1200,10,500,150)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False