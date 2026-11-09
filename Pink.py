from pico2d import load_image


class Pink:
    def __init__(self):
        self.idle_image = load_image('Pink/Pink_Idle.png')
        self.run_image = load_image('Pink/Pink_Run.png')
        self.attack_image = load_image('Pink/Pink_Attack2.png')
        self.jump_image = load_image('Pink/Pink_Jump.png')

        self.x = 35
        self.y = 35
        self.frame = 0
        self.speed = 0
        self.dir = 1

        self.ground_y = 35
        self.vy = 0
        self.gravity = 0.5
        self.jump_power = 10

        self.is_attack = False
        self.animation_time = 0

    def draw(self):
        if self.is_attack:
            image = self.attack_image
        elif self.speed == 0:
            image = self.idle_image
        else:
            image = self.run_image

        if self.dir < 0:
            image.clip_composite_draw(
                self.frame * 32, 0, 32, 32, 0, 'h', self.x, self.y, 70, 70
            )
        else:
            image.clip_draw(
                self.frame * 32, 0, 32, 32, self.x, self.y, 70, 70
            )

    def update(self):
        self.x += self.dir * self.speed
        self.animation_time += 0.01

        self.y += self.vy
        self.vy -= self.gravity

        if self.y <= self.ground_y:
            self.y = self.ground_y
            self.vy = 0

        if self.is_attack:
            frame_count = 6
            frame_delay = 0.06
        elif self.speed == 0:
            frame_count = 4
            frame_delay = 0.15
        else:
            frame_count = 6
            frame_delay = 0.08

        if self.animation_time >= frame_delay:
            self.frame += 1
            self.animation_time = 0

        if self.is_attack and self.frame >= 6:
            self.is_attack = False
            self.frame = 0
        elif not self.is_attack:
            self.frame %= frame_count

    def attack(self):
        if not self.is_attack:
            self.is_attack = True
            self.frame = 0
            self.animation_time = 0

    def jump(self):
        if self.y <= self.ground_y:
            self.vy = self.jump_power
