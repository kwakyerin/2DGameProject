from pico2d import load_image

class transform_effect:
    def __init__(self,x,y):
        self.image=load_image('Effect/change.png')
        self.x=x
        self.y=y

        self.frame=0
        self.animation_time=0
        self.frame_delay=0.07
        self.is_active=False
        pass

    def start(self):
        self.frame=0
        self.animation_time=0
        self.is_active=True

    def update(self):
        if not self.is_active:
            return

        self.animation_time += 0.01

        if self.animation_time >= self.frame_delay:
            self.frame += 1
            self.animation_time = 0
            if self.frame >= 8:
                self.is_active=False
        pass

    def draw(self):
        if not self.is_active:
            return

        frame_width = 209
        frame_top = 320
        frame_height = 300

        self.image.clip_draw(
            self.frame * frame_width, frame_top, frame_width, frame_height,
            self.x, self.y, 140, 200)
        pass
