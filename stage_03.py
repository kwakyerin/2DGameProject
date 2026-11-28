import random
from pico2d import get_time, load_image
from collision import (
    CHARACTER_HALF_HEIGHT,
    CHARACTER_HALF_WIDTH,
    check_platform_collision,
)

class stage_03:
    ASTEROID_INTERVAL = 10.0
    ASTEROIDS_PER_SPAWN = 15
    ASTEROID_PASS_THROUGH_CHANCE = 0.4
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
    EXPLOSION_FRAMES = (
        (1018, 217, 275, 190),
        (1300, 217, 285, 260),
        (1585, 217, 285, 275),
        (1870, 222, 240, 205),
    )
    EXPLOSION_FRAME_DURATION = 0.15
    EXPLOSION_DURATION = 0.6
    EXPLOSION_DRAW_WIDTH = 132

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

    def _get_explosion_geometry(self, explosion):
        progress = min(
            explosion['elapsed'] / self.EXPLOSION_DURATION,
            1.0,
        )
        frame_index = min(
            int(explosion['elapsed'] / self.EXPLOSION_FRAME_DURATION),
            len(self.EXPLOSION_FRAMES) - 1,
        )
        frame = self.EXPLOSION_FRAMES[frame_index]
        frame_width, frame_height = frame[2], frame[3]
        scale = 0.7 + 0.5 * progress
        draw_width = self.EXPLOSION_DRAW_WIDTH * scale
        draw_height = draw_width * frame_height / frame_width
        draw_y = explosion['platform_top'] + draw_height / 2 - 8
        return frame, draw_width, draw_height, draw_y

    def _explosion_overlaps_character(self, explosion, character):
        _, draw_width, draw_height, draw_y = self._get_explosion_geometry(
            explosion
        )
        return (
            abs(character.x - explosion['x'])
            <= draw_width / 2 + CHARACTER_HALF_WIDTH
            and abs(character.y - draw_y)
            <= draw_height / 2 + CHARACTER_HALF_HEIGHT
        )

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
            frame, draw_width, draw_height, draw_y = (
                self._get_explosion_geometry(explosion)
            )
            frame_left, frame_bottom, frame_width, frame_height = frame
            self.asteroid_image.clip_composite_draw(
                frame_left,
                frame_bottom,
                frame_width,
                frame_height,
                0,
                '',
                explosion['x'],
                draw_y,
                draw_width,
                draw_height,
            )

    def update_asteroids(self, character):
        now = get_time()
        elapsed = now - self.last_asteroid_update_at
        self.last_asteroid_update_at = now

        if now >= self.next_asteroid_at:
            for _ in range(self.ASTEROIDS_PER_SPAWN):
                self.asteroids.append({
                    'x': random.uniform(0, 1100),
                    'y': 650,
                    'speed': random.uniform(250, 400),
                    'wind_speed': random.uniform(70, 140),
                    'pass_through_platforms': (
                        random.random()
                        < self.ASTEROID_PASS_THROUGH_CHANCE
                    ),
                    'frame_index': 1,
                    'animation_time': 0,
                })
            self.next_asteroid_at = now + self.ASTEROID_INTERVAL

        active_explosions = []
        for explosion in self.explosions:
            explosion['elapsed'] += elapsed
            if explosion['elapsed'] >= self.EXPLOSION_DURATION:
                continue
            if (
                not explosion['hit_character']
                and self._explosion_overlaps_character(explosion, character)
            ):
                hurt = getattr(character, 'hurt', None)
                if callable(hurt):
                    hurt()
                explosion['hit_character'] = True
            active_explosions.append(explosion)
        self.explosions = active_explosions

        remaining_asteroids = []
        radius = self.ASTEROID_DRAW_WIDTH / 2
        platform_boxes = [
            self._get_platform_collision_box(platform)
            for platform in self.platforms
        ]
        ground_top = min(box[3] for box in platform_boxes)
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
            for left, bottom, right, top in platform_boxes:
                if (
                    asteroid['pass_through_platforms']
                    and top > ground_top
                ):
                    continue

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
                    'hit_character': False,
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