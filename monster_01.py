from pico2d import load_image


class monster_01:
    def __init__(self):
        self.idle_image = load_image('monster/Green_Slime/Green_Slime_Idle.png')
        self.x = 500
        self.y = 55
        self.frame = 0
        self.animation_time = 0

    def draw(self):
        self.idle_image.clip_draw(
            (self.frame + 1) * 362, 0, 362, 725,
            self.x, self.y, 65, 120
        )

    def update(self):
        self.animation_time += 0.01
        if self.animation_time >= 0.15:
            self.frame = (self.frame + 1) % 4
            self.animation_time = 0
