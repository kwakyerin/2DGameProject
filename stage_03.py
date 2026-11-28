import random
from pico2d import get_time, load_image
from collision import check_platform_collision

class stage_03:
    ASTEROID_INTERVAL = 5.0
    ASTEROID_FRAMES = (
        (80, 252, 150, 165),
        (295, 247, 220, 225),
        (520, 227, 250, 305),
        (750, 217, 268, 375),
    )
    ASTEROID_FRAME_DURATION = 0.1
    ASTEROID_DRAW_WIDTH = 80
    ASTEROID_MAX_DRAW_HEIGHT = 112
    ASTEROID_ANGLE = -0.25
    EXPLOSION_SPRITE_LEFT = 990
    EXPLOSION_SPRITE_BOTTOM = 217
    EXPLOSION_SPRITE_WIDTH = 330
    EXPLOSION_SPRITE_HEIGHT = 190
    EXPLOSION_DURATION = 0.8
    EXPLOSION_DRAW_WIDTH = 132
    EXPLOSION_DRAW_HEIGHT = 76

    def __init__(self):
        self.background=load_image('background/Stage_03.png')
        self.asteroid_image=load_image('Effect/asteroid.png')
        self.asteroids=[]
        self.explosions=[]
        self.next_asteroid_at=get_time() + self.ASTEROID_INTERVAL
        self.last_asteroid_update_at=get_time()
        self.Tile_01=load_image('Map_03/purple_space/P_Tile_01.png')
        self.Tile_02=load_image('Map_03/purple_space/P_Tile_11.png')
        self.Tile_03=load_image('Map_03/purple_space/P_Tile_10.png')
        self.Tile_04=load_image('Map_03/purple_space/P_Tile_08.png')
        self.Tile_05=load_image('Map_03/purple_space/P_Tile_03.png')
        self.Tile_06=load_image('Map_03/purple_space/P_Tile_02.png')
        self.Tile_07=load_image('Map_03/purple_space/P_Tile_08.png')
        self.platforms = [
            {
                'image': self.Tile_01,
                'x': 600, 'y': 280, 'width': 300, 'height': 100,
                'collision_width': 280, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -20,
            },
            {
                'image': self.Tile_02,
                'x': 550, 'y': 10, 'width': 1200, 'height': 300,
                'collision_width': 1200, 'collision_height': 70,
                'collision_offset_x': 0, 'collision_offset_y': -125,
            },
            {
                'image': self.Tile_03,
                'x': 250, 'y': 430, 'width': 500, 'height': 150,
                'collision_width': 490, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -50,
            },
            {
                'image': self.Tile_04,
                'x': 50, 'y': 200, 'width': 150, 'height': 100,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -30,
            },
            {
                'image': self.Tile_05,
                'x': 800, 'y': 400, 'width': 150, 'height': 100,
                'collision_width': 80, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -30,
            },
            {
                'image': self.Tile_06,
                'x': 950, 'y': 500, 'width': 230, 'height': 100,
                'collision_width': 160, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -30,
            },
            {
                'image': self.Tile_07,
                'x': 330, 'y': 150, 'width': 150, 'height': 100,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -30,
            },
        ]

    def _get_platform_collision_box(self, platform):
        x = platform['x'] + platform['collision_offset_x']
        width = platform['collision_width']
        top = (
            platform['y'] + platform['height'] / 2
            + platform['collision_offset_y']
        )
        height = platform['collision_height']

        left = x - width / 2
        right = x + width / 2
        bottom = top - height
        return left, bottom, right, top

    def draw(self):
        self.background.draw(550, 325, 1100, 650)

        for platform in self.platforms:
            platform['image'].draw(
                platform['x'], platform['y'],
                platform['width'], platform['height']
            )

        for asteroid in self.asteroids:
            left, bottom, frame_width, frame_height = self.ASTEROID_FRAMES[
                asteroid['frame_index']
            ]
            self.asteroid_image.clip_composite_draw(
                left,
                bottom,
                frame_width,
                frame_height,
                self.ASTEROID_ANGLE,
                '',
                asteroid['x'],
                asteroid['y'],
                self.ASTEROID_DRAW_WIDTH,
                self.ASTEROID_DRAW_WIDTH * frame_height / frame_width,
            )

        for explosion in self.explosions:
            progress = explosion['elapsed'] / self.EXPLOSION_DURATION
            scale = 0.5 + progress
            draw_height = self.EXPLOSION_DRAW_HEIGHT * scale
            self.asteroid_image.opacify(1 - progress)
            self.asteroid_image.clip_composite_draw(
                self.EXPLOSION_SPRITE_LEFT,
                self.EXPLOSION_SPRITE_BOTTOM,
                self.EXPLOSION_SPRITE_WIDTH,
                self.EXPLOSION_SPRITE_HEIGHT,
                0,
                '',
                explosion['x'],
                explosion['platform_top'] + draw_height / 2-8,
                self.EXPLOSION_DRAW_WIDTH * scale,
                draw_height,
            )
        self.asteroid_image.opacify(1)

    def update_asteroids(self):
        now = get_time()
        elapsed = now - self.last_asteroid_update_at
        self.last_asteroid_update_at = now

        if now >= self.next_asteroid_at:
            self.asteroids.append({
                'x': random.uniform(0, 1100),
                'y': 650,
                'speed': random.uniform(250, 400),
                'wind_speed': random.uniform(70, 140),
                'frame_index': 1,
                'animation_time': 0,
            })
            self.next_asteroid_at = now + self.ASTEROID_INTERVAL

        for explosion in self.explosions:
            explosion['elapsed'] += elapsed
        self.explosions = [
            explosion for explosion in self.explosions
            if explosion['elapsed'] < self.EXPLOSION_DURATION
        ]

        remaining_asteroids = []
        radius = self.ASTEROID_DRAW_WIDTH / 2
        for asteroid in self.asteroids:
            previous_x = asteroid['x']
            previous_y = asteroid['y']
            asteroid['x'] -= asteroid['wind_speed'] * elapsed
            asteroid['y'] -= asteroid['speed'] * elapsed
            asteroid['animation_time'] += elapsed
            while asteroid['animation_time'] >= self.ASTEROID_FRAME_DURATION:
                asteroid['animation_time'] -= self.ASTEROID_FRAME_DURATION
                asteroid['frame_index'] = (
                    asteroid['frame_index'] + 1
                ) % len(self.ASTEROID_FRAMES)

            impact_y = None
            for platform in self.platforms:
                left, bottom, right, top = self._get_platform_collision_box(platform)
                asteroid_left = asteroid['x'] - radius
                asteroid_right = asteroid['x'] + radius
                asteroid_bottom = asteroid['y'] - radius
                asteroid_top = asteroid['y'] + radius
                swept_left = min(previous_x, asteroid['x']) - radius
                swept_right = max(previous_x, asteroid['x']) + radius
                crossed_platform_top = (
                    previous_y - radius >= top
                    and asteroid_bottom <= top
                    and swept_right > left
                    and swept_left < right
                )
                overlaps_platform = (
                    asteroid_right > left
                    and asteroid_left < right
                    and asteroid_top > bottom
                    and asteroid_bottom < top
                )

                if crossed_platform_top or overlaps_platform:
                    impact_y = top
                    break

            if impact_y is not None:
                self.explosions.append({
                    'x': asteroid['x'],
                    'platform_top': impact_y,
                    'elapsed': 0,
                })
            elif (
                asteroid['y'] > -self.ASTEROID_MAX_DRAW_HEIGHT
                and asteroid['x'] > -self.ASTEROID_DRAW_WIDTH
            ):
                remaining_asteroids.append(asteroid)

        self.asteroids = remaining_asteroids

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_x, previous_y):
                break