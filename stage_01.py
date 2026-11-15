from pico2d import load_image,draw_rectangle
from collision import check_platform_collision


class stage_01:
    def __init__(self):
        self.tile_01=load_image('Map_01/Green_Grass/Tile_01.png')
        self.tile_02=load_image('Map_01/Green_Grass/Tile_02.png')
        self.tile_04=load_image('Map_01/Green_Grass/Tile_04.png')
        self.tile_05=load_image('Map_01/Green_Grass/Tile_05.png')
        self.platforms = [
            {
                'image': self.tile_01,
                'x': 550, 'y': 0, 'width': 1250, 'height': 367,
                'collision_width': 1250, 'collision_height': 100,
                'collision_offset_x': 0, 'collision_offset_y': -150,
            },
            {
                'image': self.tile_04,
                'x': 200, 'y': 350, 'width': 400, 'height': 200,
                'collision_width': 320, 'collision_height': 60,
                'collision_offset_x': 0, 'collision_offset_y': -20,
            },
            {
                'image': self.tile_05,
                'x': 480, 'y': 230, 'width': 400, 'height': 200,
                'collision_width': 320, 'collision_height': 60,
                'collision_offset_x': 0, 'collision_offset_y': -20,
            },
            {
                'image': self.tile_02,
                'x': 730, 'y': 450, 'width': 600, 'height': 230,
                'collision_width': 480, 'collision_height': 69,
                'collision_offset_x': 0, 'collision_offset_y': -20,
            },
            {
                'image': self.tile_05,
                'x': 700, 'y': 100, 'width': 400, 'height': 200,
                'collision_width': 320, 'collision_height': 60,
                'collision_offset_x': 0, 'collision_offset_y': -20,
            }
        ]
        pass

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
            x = platform['x']
            y = platform['y']
            w = platform['width']
            h = platform['height']

            platform['image'].draw(x, y, w, h)

            left, bottom, right, top = self._get_platform_collision_box(platform)
            draw_rectangle(left, bottom, right, top, 255, 0, 0)

    def resolve_character_collision(self, character, _previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_y):
                break

    def update(self):
        pass