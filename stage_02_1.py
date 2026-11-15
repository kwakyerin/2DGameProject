from pico2d import load_image, draw_rectangle
from collision import check_platform_collision

class stage_02_1:
    def __init__(self):
        self.Tile_01=load_image('Map_02/Purple_Cloud/PCloud_03.png')
        self.Tile_02=load_image('Map_02/Purple_Cloud/PCloud_05.png')
        self.Tile_03=load_image('Map_02/Purple_Cloud/PCloud_02.png')
        self.Tile_04=load_image('Map_02/Purple_Cloud/PCloud_03.png')
        self.Tile_05=load_image('Map_02/Space/P_Tile_10.png')
        self.platforms = [
            {
                'image': self.Tile_01,
                'x': 45, 'y': 550, 'width': 130, 'height': 50,
                'collision_width': 130, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_02,
                'x': 300, 'y': 400, 'width': 500, 'height': 50,
                'collision_width': 500, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_03,
                'x': 800, 'y': 600, 'width': 100, 'height': 50,
                'collision_width': 100, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_02,
                'x': 600, 'y': 200, 'width': 500, 'height': 50,
                'collision_width': 500, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_04,
                'x': 200, 'y': 50, 'width': 130, 'height': 50,
                'collision_width': 130, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_04,
                'x': 100, 'y': 140, 'width': 130, 'height': 50,
                'collision_width': 130, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': 0,
            },
            {
                'image': self.Tile_05,
                'x': 1200, 'y': 10, 'width': 500, 'height': 150,
                'collision_width': 470, 'collision_height': 80,
                'collision_offset_x': 0, 'collision_offset_y': -50,
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

    def resolve_character_collision(self, character, _previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_y):
                break