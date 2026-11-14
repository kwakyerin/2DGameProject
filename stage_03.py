from pico2d import load_image

class stage_03:
    def __init__(self):
        self.Tile_01=load_image('Map_03/purple_space/P_Tile_01.png')
        self.Tile_02=load_image('Map_03/purple_space/P_Tile_11.png')
        self.Tile_03=load_image('Map_03/purple_space/P_Tile_10.png')
        self.Tile_04=load_image('Map_03/purple_space/P_Tile_08.png')
        self.Tile_05=load_image('Map_03/purple_space/P_Tile_03.png')
        self.Tile_06=load_image('Map_03/purple_space/P_Tile_02.png')
        pass

    def draw(self):
        self.Tile_01.draw(600,300,300,100)
        self.Tile_02.draw(550,10,1200,300)
        self.Tile_03.draw(250,450,500,150)
        self.Tile_04.draw(50,200,150,100)
        self.Tile_05.draw(800,400,150,100)
        self.Tile_06.draw(950,500,230,100)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False