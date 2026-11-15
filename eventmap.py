from pico2d import load_image, draw_rectangle
from collision import check_platform_collision

class eventmap:
    def __init__(self):
        self.current_color=1

        self.Tile_01=load_image('Event_Map/Pink.png')
        self.Tile_02=load_image('Event_Map/Blue.png')
        self.Tile_03=load_image('Event_Map/Yellow.png')
        self.Tile_04=load_image('Map_03/purple_space/P_Tile_10.png')
        self.Tile_05=load_image('Map_03/gray_space/G_Tile_10.png')
        self.platforms = [
            {
                'image': self.Tile_01, 'color': 1,
                'x': 370, 'y': 50, 'width': 250, 'height': 130,
                'collision_width': 163, 'collision_height': 60,
                'collision_offset_x': 0, 'collision_offset_y': -33,
            },
            {
                'image': self.Tile_01, 'color': 1,
                'x': 130, 'y': 230, 'width': 250, 'height': 130,
                'collision_width': 163, 'collision_height': 60,
                'collision_offset_x': 0, 'collision_offset_y': -33,
            },
            {
                'image': self.Tile_01, 'color': 1,
                'x': 900, 'y': 500, 'width': 250, 'height': 130,
                'collision_width': 163, 'collision_height': 60,
                'collision_offset_x': 0, 'collision_offset_y': -33,
            },
            {
                'image': self.Tile_01, 'color': 1,
                'x': 200, 'y': 580, 'width': 250, 'height': 130,
                'collision_width': 163, 'collision_height': 60,
                'collision_offset_x': 0, 'collision_offset_y': -33,
            },
            {
                'image': self.Tile_02, 'color': 2,
                'x': 600, 'y': 300, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -18,
            },
            {
                'image': self.Tile_02, 'color': 2,
                'x': 10, 'y': 500, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -18,
            },
            {
                'image': self.Tile_02, 'color': 2,
                'x': 500, 'y': 660, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -18,
            },
            {
                'image': self.Tile_02, 'color': 2,
                'x': 350, 'y': 380, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -18,
            },
            {
                'image': self.Tile_02, 'color': 2,
                'x': 1000, 'y': 430, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -18,
            },
            {
                'image': self.Tile_03, 'color': 3,
                'x': 750, 'y': 200, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -20,
            },
            {
                'image': self.Tile_03, 'color': 3,
                'x': 1000, 'y': 600, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -20,
            },
            {
                'image': self.Tile_03, 'color': 3,
                'x': 350, 'y': 450, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -20,
            },
            {
                'image': self.Tile_03, 'color': 3,
                'x': 190, 'y': 660, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -20,
            },
            {
                'image': self.Tile_03, 'color': 3,
                'x': 370, 'y': 200, 'width': 200, 'height': 80,
                'collision_width': 165, 'collision_height': 60,
                'collision_offset_x': 5, 'collision_offset_y': -20,
            },
            {
                'image': self.Tile_04, 'color': None,
                'x': 0, 'y': 50, 'width': 500, 'height': 150,
                'collision_width': 480, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -50,
            },
            {
                'image': self.Tile_05, 'color': None,
                'x': 1200, 'y': 50, 'width': 500, 'height': 150,
                'collision_width': 480, 'collision_height': 50,
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
            if platform['color'] is not None and platform['color'] != self.current_color:
                continue

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
            if platform['color'] is not None and platform['color'] != self.current_color:
                continue

            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_y):
                break
