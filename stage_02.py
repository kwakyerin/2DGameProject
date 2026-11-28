import random
from pico2d import get_time, load_image
from collision import check_platform_collision

class stage_02:
    RAIN_MIN_SPAWN_INTERVAL = 0.03
    RAIN_MAX_SPAWN_INTERVAL = 0.3
    RAIN_DENSITY_RAMP_DURATION = 2.5
    RAIN_START_Y = 650
    RAIN_DROP_WIDTH = 24
    RAIN_DROP_HEIGHT = 62
    RAIN_DROP_ANGLE = -0.25
    RAIN_DURATION = 20.0
    CLEAR_DURATION = 10.0
    WHITE_FLASH_COUNT = 2
    WHITE_FLASH_DURATION = 0.15
    WHITE_FLASH_GAP_DURATION = 0.15
    LIGHTNING_FRAME_COUNT = 8
    LIGHTNING_FRAME_DURATION = (
        WHITE_FLASH_DURATION / LIGHTNING_FRAME_COUNT
    )
    LIGHTNING_SHEET_WIDTH = 2172
    LIGHTNING_FRAME_HEIGHT = 724
    LIGHTNING_SCREEN_WIDTH = 1100
    LIGHTNING_SCREEN_HEIGHT = 650
    LIGHTNING_DRAW_WIDTH = 320
    LIGHTNING_DRAW_HEIGHT = 650
    LIGHTNING_TOP_OVERSHOOT = 155

    def __init__(self):
        self.background=load_image('background/Stage_02.png')
        self.rain_background=load_image('background/Stage_02_Rain.png')
        self.white_background=load_image('background/White.png')
        self.rain_image=load_image('Effect/Rain.png')
        self.lightning_image=load_image('Effect/lightning.png')
        self.rain_opacity=0
        self.rain_density=0
        self.next_rain_toggle_at=get_time() + self.CLEAR_DURATION
        self.white_flash_active=False
        self.white_flash_visible=False
        self.white_flash_count=0
        self.next_white_flash_at=0
        self.lightning_frame=0
        self.next_lightning_frame_at=0
        self.lightning_bolts=[]
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

    def draw_white_flash(self):
        if self.white_flash_visible:
            self.white_background.draw(550, 325, 1100, 650)
            frame_left = int(
                self.lightning_frame
                * self.LIGHTNING_SHEET_WIDTH
                / self.LIGHTNING_FRAME_COUNT
            )
            frame_right = int(
                (self.lightning_frame + 1)
                * self.LIGHTNING_SHEET_WIDTH
                / self.LIGHTNING_FRAME_COUNT
            )
            for bolt in self.lightning_bolts:
                self.lightning_image.clip_draw(
                    frame_left,
                    0,
                    frame_right - frame_left,
                    self.LIGHTNING_FRAME_HEIGHT,
                    bolt['x'],
                    bolt['y'],
                    bolt['width'],
                    bolt['height'],
                )

    def _start_lightning_animation(self, now):
        self.lightning_frame = 0
        self.next_lightning_frame_at = (
            now + self.LIGHTNING_FRAME_DURATION
        )
        bolt_count = random.randint(2, 3)
        self.lightning_bolts = []
        for index in range(bolt_count):
            scale = (
                1
                if index == 0
                else random.uniform(0.4, 0.7)
            )
            width = self.LIGHTNING_DRAW_WIDTH * scale
            height = self.LIGHTNING_DRAW_HEIGHT * scale
            self.lightning_bolts.append({
                'x': random.uniform(
                    width / 2,
                    self.LIGHTNING_SCREEN_WIDTH - width / 2,
                ),
                'y': (
                    self.LIGHTNING_SCREEN_HEIGHT
                    - height / 2
                    + self.LIGHTNING_TOP_OVERSHOOT
                    * height / self.LIGHTNING_DRAW_HEIGHT
                ),
                'width': width,
                'height': height,
            })

    def update_rain(self):
        now = get_time()
        elapsed_since_update = now - self.last_rain_update_at
        self.last_rain_update_at = now

        if self.white_flash_active:
            if now >= self.next_white_flash_at:
                if self.white_flash_visible:
                    self.white_flash_count += 1
                    self.white_flash_visible = False
                    if self.white_flash_count >= self.WHITE_FLASH_COUNT:
                        self.white_flash_active = False
                        self.rain_opacity = 1
                        self.next_rain_toggle_at = now + self.RAIN_DURATION
                    else:
                        self.next_white_flash_at = (
                            now + self.WHITE_FLASH_GAP_DURATION
                        )
                else:
                    self.white_flash_visible = True
                    self._start_lightning_animation(now)
                    self.next_white_flash_at = (
                        now + self.WHITE_FLASH_DURATION
                    )
        elif now >= self.next_rain_toggle_at:
            if self.rain_opacity > 0:
                self.rain_opacity = 0
                self.next_rain_toggle_at = now + self.CLEAR_DURATION
            else:
                self.white_flash_active = True
                self.white_flash_visible = True
                self.white_flash_count = 0
                self._start_lightning_animation(now)
                self.next_white_flash_at = now + self.WHITE_FLASH_DURATION

        while (
            self.white_flash_visible
            and now >= self.next_lightning_frame_at
        ):
            if self.lightning_frame < self.LIGHTNING_FRAME_COUNT - 1:
                self.lightning_frame += 1
                self.next_lightning_frame_at += (
                    self.LIGHTNING_FRAME_DURATION
                )
            else:
                self.next_lightning_frame_at = (
                    now + self.LIGHTNING_FRAME_DURATION
                )

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