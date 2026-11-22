from pico2d import load_image


class Effect:
    FRAME_WIDTH = 362
    FRAME_HEIGHT = 724
    FRAME_COUNT = 6
    FRAME_CENTERS = (
        (163.2, 360.4),
        (146.7, 351.0),
        (161.8, 347.0),
        (185.5, 345.7),
        (199.3, 347.1),
        (191.3, 354.7),
    )

    def __init__(self):
        self.image = load_image('Effect/Treat.png')
        self.x = 0
        self.y = 0
        self.frame = 0
        self.animation_time = 0
        self.frame_delay = 0.07
        self.is_active = False

    def start(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.animation_time = 0
        self.is_active = True

    def update(self, x, y):
        if not self.is_active:
            return

        self.x = x
        self.y = y
        self.animation_time += 0.01

        if self.animation_time >= self.frame_delay:
            self.frame += 1
            self.animation_time = 0
            if self.frame >= self.FRAME_COUNT:
                self.is_active = False

    def draw(self):
        if not self.is_active:
            return

        center_x, center_y = self.FRAME_CENTERS[self.frame]
        scale_x = 140 / self.FRAME_WIDTH
        scale_y = 280 / self.FRAME_HEIGHT
        draw_x = self.x + (self.FRAME_WIDTH / 2 - center_x) * scale_x
        draw_y = self.y + (center_y - self.FRAME_HEIGHT / 2) * scale_y

        self.image.clip_draw(
            self.frame * self.FRAME_WIDTH,
            0,
            self.FRAME_WIDTH,
            self.FRAME_HEIGHT,
            draw_x,
            draw_y,
            140,
            280,
        )


class FireEffect:
    FRAME_WIDTH = 362
    FRAME_HEIGHT = 724
    FRAME_COUNT = 6
    DRAW_Y_OFFSET = 25

    def __init__(self):
        self.image = load_image('Effect/Fire.png')
        self.x = 0
        self.y = 0
        self.frame = 0
        self.animation_time = 0
        self.frame_delay = 0.07
        self.is_active = False

    def start(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.animation_time = 0
        self.is_active = True

    def update(self, x, y):
        if not self.is_active:
            return

        self.x = x
        self.y = y
        self.animation_time += 0.01

        if self.animation_time >= self.frame_delay:
            self.frame += 1
            self.animation_time = 0
            if self.frame >= self.FRAME_COUNT:
                self.is_active = False

    def draw(self):
        if not self.is_active:
            return

        self.image.clip_draw(
            self.frame * self.FRAME_WIDTH,
            0,
            self.FRAME_WIDTH,
            self.FRAME_HEIGHT,
            self.x,
            self.y + self.DRAW_Y_OFFSET-10,
            140,
            280,
        )
