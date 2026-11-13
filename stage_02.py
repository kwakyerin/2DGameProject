from pico2d import load_image

class stage_02:
    def __init__(self):
        self.grass=load_image('Map_02/DGrass/Tile_01.png')
        self.Tile_01=load_image('Map_02/Blue_Cloud/BCloud_03.png')
        self.Tile_02=load_image('Map_02/Blue_Cloud/BCloud_04.png')
        self.Tile_03=load_image('Map_02/Blue_Cloud/BCloud_05.png')
        self.Tile_04=load_image('Map_02/Blue_Cloud/BCloud_02.png')
        pass

    def draw(self):
        self.grass.draw(30,0,400,200)
        self.Tile_01.draw(200,130,100,50)
        self.Tile_02.draw(400,200,150,50)
        self.Tile_03.draw(50,320,500,50)
        self.Tile_01.draw(420,420,100,50)
        self.Tile_04.draw(580,320,80,50)
        self.Tile_01.draw(700,150,100,50)
        self.Tile_02.draw(880,300,150,50)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_y):
        character.on_ground = False