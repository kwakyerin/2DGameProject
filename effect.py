from pico2d import load_image


class Effect:
    FRAME_WIDTH = 362
    FRAME_HEIGHT = 724
    FRAME_COUNT = 6
    DURATION = 5.0
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
        self.elapsed_time = 0
        self.frame_delay = 0.07
        self.is_active = False

    def start(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.animation_time = 0
        self.elapsed_time = 0
        self.is_active = True

    def update(self, x, y):
        if not self.is_active:
            return

        self.x = x
        self.y = y
        self.elapsed_time += 0.01
        if self.elapsed_time >= self.DURATION:
            self.is_active = False
            return

        self.animation_time += 0.01

        if self.animation_time >= self.frame_delay:
            self.frame = (self.frame + 1) % self.FRAME_COUNT
            self.animation_time = 0

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
    DURATION = 10.0

    def __init__(self):
        self.image = load_image('Effect/Fire.png')
        self.x = 0
        self.y = 0
        self.frame = 0
        self.animation_time = 0
        self.elapsed_time = 0
        self.frame_delay = 0.07
        self.is_active = False

    def start(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.animation_time = 0
        self.elapsed_time = 0
        self.is_active = True

    def update(self, x, y):
        if not self.is_active:
            return

        self.x = x
        self.y = y
        self.elapsed_time += 0.01
        if self.elapsed_time >= self.DURATION:
            self.is_active = False
            return

        self.animation_time += 0.01

        if self.animation_time >= self.frame_delay:
            self.frame = (self.frame + 1) % self.FRAME_COUNT
            self.animation_time = 0

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


class FireAttackEffect:
    FRAME_RECTS = (
        (92, 306, 58, 60),
        (230, 288, 134, 95),
        (423, 280, 182, 121),
        (665, 266, 225, 151),
        (945, 255, 254, 182),
        (1243, 250, 279, 196),
        (1566, 250, 283, 211),
        (1887, 283, 194, 155),
    )
    FRAME_COUNT = len(FRAME_RECTS)
    FRAME_DELAY = 0.07
    DRAW_SCALE = 0.24
    DRAW_MAX_WIDTH = max(frame[2] for frame in FRAME_RECTS) * DRAW_SCALE
    SPAWN_OFFSET = 50
    MOVE_SPEED = 8
    SCREEN_WIDTH = 1100

    def __init__(self):
        self.image = load_image('Effect/Fire_Attack.png')
        self.projectiles = []

    def start(self, x, y, direction):
        direction = 1 if direction >= 0 else -1
        self.projectiles.append({
            'x': x + direction * self.SPAWN_OFFSET,
            'y': y,
            'direction': direction,
            'frame': 0,
            'animation_time': 0,
        })

    def update(self):
        active_projectiles = []
        for projectile in self.projectiles:
            projectile['x'] += projectile['direction'] * self.MOVE_SPEED
            projectile['animation_time'] += 0.01
            if projectile['animation_time'] >= self.FRAME_DELAY:
                projectile['frame'] += 1
                projectile['animation_time'] -= self.FRAME_DELAY

            if (
                projectile['frame'] < self.FRAME_COUNT
                and -self.DRAW_MAX_WIDTH <= projectile['x']
                <= self.SCREEN_WIDTH + self.DRAW_MAX_WIDTH
            ):
                active_projectiles.append(projectile)

        self.projectiles = active_projectiles

    def draw(self):
        for projectile in self.projectiles:
            frame_left, frame_bottom, frame_width, frame_height = (
                self.FRAME_RECTS[projectile['frame']]
            )
            draw_width = frame_width * self.DRAW_SCALE
            draw_height = frame_height * self.DRAW_SCALE
            if projectile['direction'] < 0:
                self.image.clip_composite_draw(
                    frame_left,
                    frame_bottom,
                    frame_width,
                    frame_height,
                    0,
                    'h',
                    projectile['x'],
                    projectile['y'],
                    draw_width,
                    draw_height,
                )
            else:
                self.image.clip_draw(
                    frame_left,
                    frame_bottom,
                    frame_width,
                    frame_height,
                    projectile['x'],
                    projectile['y'],
                    draw_width,
                    draw_height,
                )


class BubbleEffect:
    DURATION = 10.0
    DRAW_SIZE = 110

    def __init__(self):
        self.image = load_image('Effect/Bubble.png')
        self.x = 0
        self.y = 0
        self.elapsed_time = 0
        self.is_active = False

    def start(self, x, y):
        self.x = x
        self.y = y
        self.elapsed_time = 0
        self.is_active = True

    def update(self, x, y):
        if not self.is_active:
            return

        self.x = x
        self.y = y
        self.elapsed_time += 0.01
        if self.elapsed_time >= self.DURATION:
            self.is_active = False

    def draw(self):
        if not self.is_active:
            return

        self.image.draw(self.x, self.y, self.DRAW_SIZE, self.DRAW_SIZE)
