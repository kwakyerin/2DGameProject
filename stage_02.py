import random
from pico2d import get_time, load_image
from collision import check_platform_collision

class stage_02:
    RAIN_MIN_SPAWN_INTERVAL = 0.03
    RAIN_MAX_SPAWN_INTERVAL = 0.3
    RAIN_DENSITY_RAMP_DURATION = 2.5
    RAIN_START_Y = 650
    RAIN_DROP_WIDTH = 28
    RAIN_DROP_HEIGHT = 72
    RAIN_DROP_ANGLE = -0.25
    RAIN_DURATION = 10.0
    CLEAR_DURATION = 5.0

    def __init__(self):
        self.background=load_image('background/Stage_02.png')
        self.rain_background=load_image('background/Stage_02_Rain.png')
        self.rain_image=load_image('Effect/Rain.png')
        self.rain_opacity=0
        self.rain_density=0
        self.next_rain_toggle_at=get_time() + self.CLEAR_DURATION
        self.last_rain_update_at=get_time()
        self.rain_spawn_accumulator=0
        self.rain_drops=[]
        self.grass=load_image('Map_02/DGrass/Tile_01.png')
        self.Tile_01=load_image('Map_02/Blue_Cloud/BCloud_03.png')
        self.Tile_02=load_image('Map_02/Blue_Cloud/BCloud_04.png')
        self.Tile_03=load_image('Map_02/Blue_Cloud/BCloud_05.png')
        self.Tile_04=load_image('Map_02/Blue_Cloud/BCloud_02.png')
        self.Tile_05=load_image('Map_02/Blue_Cloud/BCloud_01.png')
        self.platforms = [
            {
                'image': self.grass,
                'x': 30, 'y': 0, 'width': 400, 'height': 200,
                'collision_width': 200, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
                'image': self.Tile_01,
                'x': 200, 'y': 100, 'width': 100, 'height': 50,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_02,
                'x': 400, 'y': 50, 'width': 150, 'height': 50,
                'collision_width': 120, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_03,
                'x': 50, 'y': 300, 'width': 500, 'height': 50,
                'collision_width': 500, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_01,
                'x': 580, 'y': 550, 'width': 100, 'height': 50,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_04,
                'x': 270, 'y': 610, 'width': 80, 'height': 50,
                'collision_width': 80, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_01,
                'x': 580, 'y': 190, 'width': 100, 'height': 50,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_03,
                'x': 900, 'y': 300, 'width': 500, 'height': 50,
                'collision_width': 500, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_02,
                'x': 80, 'y': 500, 'width': 150, 'height': 50,
                'collision_width': 150, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_05,
                'x': 400, 'y': 300, 'width': 50, 'height': 50,
                'collision_width': 50, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_05,
                'x': 750, 'y': 600, 'width': 50, 'height': 50,
                'collision_width': 50, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
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
        if self.rain_opacity > 0:
            self.rain_background.opacify(self.rain_opacity)
            self.rain_background.draw(550, 325, 1100, 650)
            self.rain_background.opacify(1)

        for platform in self.platforms:
            platform['image'].draw(
                platform['x'], platform['y'],
                platform['width'], platform['height']
            )

        if self.rain_drops and self.rain_density > 0:
            self.rain_image.opacify(self.rain_density)
            for drop in self.rain_drops:
                self.rain_image.composite_draw(
                    self.RAIN_DROP_ANGLE,
                    '',
                    drop['x'],
                    drop['y'],
                    self.RAIN_DROP_WIDTH,
                    self.RAIN_DROP_HEIGHT,
                )
            self.rain_image.opacify(1)

    def update_rain(self):
        now = get_time()
        elapsed_since_update = now - self.last_rain_update_at
        self.last_rain_update_at = now

        if now >= self.next_rain_toggle_at:
            self.rain_opacity = 1 - self.rain_opacity
            duration = (
                self.RAIN_DURATION if self.rain_opacity > 0
                else self.CLEAR_DURATION
            )
            self.next_rain_toggle_at = now + duration

        density_change = (
            elapsed_since_update / self.RAIN_DENSITY_RAMP_DURATION
        )
        if self.rain_opacity > self.rain_density:
            self.rain_density = min(
                self.rain_opacity, self.rain_density + density_change
            )
        else:
            self.rain_density = max(
                self.rain_opacity, self.rain_density - density_change
            )

        for drop in self.rain_drops:
            drop['x'] -= drop['wind_speed'] * elapsed_since_update
            drop['y'] -= drop['speed'] * elapsed_since_update

        if self.rain_density > 0:
            spawn_interval = self.RAIN_MAX_SPAWN_INTERVAL - (
                self.RAIN_MAX_SPAWN_INTERVAL - self.RAIN_MIN_SPAWN_INTERVAL
            ) * self.rain_density
            self.rain_spawn_accumulator += elapsed_since_update
            while self.rain_spawn_accumulator >= spawn_interval:
                self.rain_drops.append({
                    'x': random.uniform(0, 1100),
                    'y': self.RAIN_START_Y,
                    'speed': random.uniform(250, 400),
                    'wind_speed': random.uniform(70, 140),
                })
                self.rain_spawn_accumulator -= spawn_interval
        else:
            self.rain_spawn_accumulator = 0

        self.rain_drops = [
            drop for drop in self.rain_drops
            if drop['y'] > -32 and drop['x'] > -32
        ]

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_x, previous_y):
                break