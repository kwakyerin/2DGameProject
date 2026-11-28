import random
from pico2d import get_time, load_image
from collision import check_platform_collision

class stage_03:
    ASTEROID_INTERVAL = 5.0
    ASTEROID_SPRITE_LEFT = 80
    ASTEROID_SPRITE_BOTTOM = 257
    ASTEROID_SPRITE_SIZE = 150
    ASTEROID_DRAW_SIZE = 80
    ASTEROID_ANGLE = -0.25

    def __init__(self):
        self.background=load_image('background/Stage_03.png')
        self.asteroid_image=load_image('Effect/asteroid.png')
        self.asteroids=[]
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
            self.asteroid_image.clip_composite_draw(
                self.ASTEROID_SPRITE_LEFT,
                self.ASTEROID_SPRITE_BOTTOM,
                self.ASTEROID_SPRITE_SIZE,
                self.ASTEROID_SPRITE_SIZE,
                self.ASTEROID_ANGLE,
                '',
                asteroid['x'],
                asteroid['y'],
                self.ASTEROID_DRAW_SIZE,
                self.ASTEROID_DRAW_SIZE,
            )

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
            })
            self.next_asteroid_at = now + self.ASTEROID_INTERVAL

        for asteroid in self.asteroids:
            asteroid['x'] -= asteroid['wind_speed'] * elapsed
            asteroid['y'] -= asteroid['speed'] * elapsed

        self.asteroids = [
            asteroid for asteroid in self.asteroids
            if asteroid['y'] > -self.ASTEROID_DRAW_SIZE
            and asteroid['x'] > -self.ASTEROID_DRAW_SIZE
        ]

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_x, previous_y):
                break