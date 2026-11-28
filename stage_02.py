from pico2d import get_time, load_image
from collision import check_platform_collision

class stage_02:
    def __init__(self):
        self.background=load_image('background/Stage_02.png')
        self.rain_background=load_image('background/Stage_02_Rain.png')
        self.rain_opacity=0
        self.rain_transition_started_at=None
        self.rain_transition_from=0
        self.rain_target_opacity=0
        self.next_rain_toggle_at=get_time() + 5.0
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

    def update_rain(self):
        now = get_time()
        fade_duration = 8.0

        if now >= self.next_rain_toggle_at:
            self.rain_transition_from = self.rain_opacity
            self.rain_target_opacity = 1 - self.rain_target_opacity
            self.rain_transition_started_at = now
            self.next_rain_toggle_at = now + 5.0

        if self.rain_transition_started_at is None:
            return

        elapsed = now - self.rain_transition_started_at
        progress = min(elapsed / fade_duration, 1)
        eased_progress = progress * progress * (3 - 2 * progress)
        self.rain_opacity = self.rain_transition_from + (
            self.rain_target_opacity - self.rain_transition_from
        ) * eased_progress

        if progress >= 1:
            self.rain_transition_started_at = None

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_x, previous_y):
                break