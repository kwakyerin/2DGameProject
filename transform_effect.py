from pico2d import load_image

class transform_effect:
    def __init__(self,x,y):
        self.image=load_image('Effect/Change_Light.png')
        self.x=x
        self.y=y

        self.frame=0
        self.animation_time=0
        self.frame_delay=0.07
        pass

    def update(self):
        self.animation_time += 0.01

        if self.animation_time >= self.frame_delay:
         self.frame = (self.frame + 1) % 8
         self.animation_time = 0
        pass

    def draw(self):
        frame_width = 271
        frame_height = 724

        self.image.clip_draw(
            self.frame * frame_width, 0, frame_width, frame_height,
            self.x, self.y, 120, 320)
        pass
