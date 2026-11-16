from pico2d import load_image, draw_rectangle
from collision import check_platform_collision

class stage_02:
    def __init__(self):
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
                'x': 200, 'y': 130, 'width': 100, 'height': 50,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_02,
                'x': 400, 'y': 200, 'width': 150, 'height': 50,
                'collision_width': 150, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_03,
                'x': 50, 'y': 320, 'width': 500, 'height': 50,
                'collision_width': 500, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_01,
                'x': 420, 'y': 420, 'width': 100, 'height': 50,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_04,
                'x': 580, 'y': 280, 'width': 80, 'height': 50,
                'collision_width': 80, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_01,
                'x': 700, 'y': 150, 'width': 100, 'height': 50,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_02,
                'x': 880, 'y': 300, 'width': 150, 'height': 50,
                'collision_width': 150, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_03,
                'x': 900, 'y': 550, 'width': 500, 'height': 50,
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
                'x': 230, 'y': 600, 'width': 50, 'height': 50,
                'collision_width': 50, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_05,
                'x': 600, 'y': 490, 'width': 50, 'height': 50,
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
        for platform in self.platforms:
            platform['image'].draw(
                platform['x'], platform['y'],
                platform['width'], platform['height']
            )

            left, bottom, right, top = self._get_platform_collision_box(platform)
            draw_rectangle(left, bottom, right, top, 255, 0, 0)

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_x, previous_y):
                break