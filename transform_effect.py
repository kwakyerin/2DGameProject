from pico2d import load_image

class transform_effect:
    def __init__(self):
        self.image=load_image('Effect/Change_Light.png')
        self.x=400
        self.y=300

        self.frame=0
        self.animation_time=0
        self.frame_delay=0.07
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0,0,256,682,self.x,self.y,120,320)
        pass

