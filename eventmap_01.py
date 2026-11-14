from pico2d import load_image

class eventmap_01:
    def __init__(self):
        self.Tile_01=load_image('Event_Map/Pink.png')
        self.Tile_02=load_image('Event_Map/Blue.png')
        self.Tile_03=load_image('Event_Map/Yellow.png')
        pass

    def draw(self):
        self.Tile_01.draw(400,50,300,120)
        self.Tile_02.draw(600,300,200,80)
        self.Tile_02.draw(10,500,200,80)
        self.Tile_03.draw(750,200,200,80)
        self.Tile_03.draw(1000,600,200,80)
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False
