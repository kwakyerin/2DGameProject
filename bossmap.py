from pico2d import load_image, draw_rectangle
from collision import check_collision

class bossmap:
    def __init__(self):
        self.background=load_image('background/Boss.png')
        self.image=load_image('Map_03/gray_space/G_Tile_11.png')
        
        self.left = 0
        self.right = 1100
        self.bottom = 0
        self.top = 40
        
        pass

    def draw(self):
        self.background.draw(550, 325, 1100, 650)
        self.image.draw(550,10,1200,300)

        #빨간색 충돌 박스
        draw_rectangle(self.left,self.bottom,self.right,self.top,
            255, 0, 0
        )
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False

        platform = (self.left, self.bottom, self.right, self.top)

        check_collision(character, platform, previous_x, previous_y)
