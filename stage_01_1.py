from pico2d import load_image, draw_rectangle
from collision import check_platform_collision

class stage_01_1:

    def __init__(self):
        self.background=load_image('background/Stage_01_2.png')
        self.Tile_01=load_image('Map_01/DGreen_Grass/Tile_04.png')
        self.Tile_02=load_image('Map_01/DGreen_Grass/Tile_01.png')
        self.Tile_03=load_image('Map_01/DGreen_Grass/Tile_02.png')
        self.platforms = [
            {
            'image': self.Tile_01,
            'x': 550, 'y': 0, 'width': 1250, 'height': 367,
            'collision_width': 1250, 'collision_height': 100,
            'collision_offset_x': 0, 'collision_offset_y': -150,
            },
            {
            'image': self.Tile_02,
            'x': 550, 'y': 150, 'width': 400, 'height': 200,
            'collision_width': 180, 'collision_height': 50,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
            'image': self.Tile_03,
            'x': 220, 'y': 250, 'width': 400, 'height': 200,
            'collision_width': 320, 'collision_height': 60,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
            'image': self.Tile_03,
            'x': 900, 'y': 250, 'width': 400, 'height': 200,
            'collision_width': 320, 'collision_height': 60,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
            'image': self.Tile_02,
            'x': 500, 'y': 400, 'width': 400, 'height': 200,
            'collision_width': 180, 'collision_height': 50,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
            'image': self.Tile_02,
            'x': 800, 'y': 480, 'width': 400, 'height': 200,
            'collision_width': 180, 'collision_height': 50,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            }

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
