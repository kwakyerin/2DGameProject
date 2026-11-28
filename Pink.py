from pico2d import load_image


class Pink:
    HURT_BLINK_INTERVAL = 0.1
    HURT_BLINK_CYCLES = 2
    HURT_FRAME_SEQUENCE = (1, 2, 1, 2)

    def __init__(self):
        self.idle_image = load_image('Pink/Pink_Idle.png')
        self.run_image = load_image('Pink/Pink_Run.png')
        self.attack_image = load_image('Pink/Pink_Attack2.png')
        self.hurt_image = load_image('Pink/Pink_Hurt.png')
        self.jump_image = load_image('Pink/Pink_Jump.png')

        self.x = 35
        self.y = 74
        self.frame = 0
        self.speed = 0
        self.dir = 1

        self.on_ground = True
        self.vy = 0
        self.gravity = 0.5
        self.jump_power = 12

        self.is_attack = False
        self.is_hurt = False
        self.hurt_cycles_remaining = 0
        self.hurt_blink_time = 0
        self.animation_time = 0

    def draw(self):
        if (
            self.is_hurt
            and self.hurt_blink_time
            < self.HURT_BLINK_INTERVAL * self.HURT_BLINK_CYCLES * 2
            and int(self.hurt_blink_time / self.HURT_BLINK_INTERVAL) % 2
        ):
            return

        if self.is_hurt:
            image = self.hurt_image
        elif self.is_attack:
            image = self.attack_image
        elif self.speed == 0:
            image = self.idle_image
        else:
            image = self.run_image

        frame = self.HURT_FRAME_SEQUENCE[self.frame] if self.is_hurt else self.frame
        if self.dir < 0:
            image.clip_composite_draw(
                frame * 32, 0, 32, 32, 0, 'h', self.x, self.y, 70, 70
            )
        else:
            image.clip_draw(
                frame * 32, 0, 32, 32, self.x, self.y, 70, 70
            )

    def update(self):
        self.x += self.dir * self.speed
        self.animation_time += 0.01

        self.y += self.vy
        self.vy -= self.gravity

        if self.is_hurt:
            self.hurt_blink_time += 0.01
            frame_count = 4
            frame_delay = 0.1
        elif self.is_attack:
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

        if self.is_hurt and self.frame >= frame_count:
            self.hurt_cycles_remaining -= 1
            if self.hurt_cycles_remaining == 0:
                self.is_hurt = False
            self.frame = 0
        elif self.is_attack and self.frame >= 6:
            self.is_attack = False
            self.frame = 0
        elif not self.is_hurt and not self.is_attack:
            self.frame %= frame_count

    def attack(self):
        if not self.is_attack:
            self.is_attack = True
            self.frame = 0
            self.animation_time = 0

    def hurt(self):
        if not self.is_hurt:
            self.is_hurt = True
            self.hurt_cycles_remaining = 1
            self.hurt_blink_time = 0
            self.is_attack = False
            self.speed = 0
            self.frame = 0
            self.animation_time = 0

    def jump(self):
        if self.on_ground:
            self.vy = self.jump_power
            self.on_ground = False
