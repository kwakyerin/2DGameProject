from pico2d import load_image

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
                'collision_left': -596, 'collision_right': 596,
                'collision_top': 39,
            },
            {
                'image': self.tile_04,
                'x': 200, 'y': 350, 'width': 400, 'height': 200,
                'collision_left': -162, 'collision_right': 161,
                'collision_top': 30,
            },
            {
                'image': self.tile_05,
                'x': 480, 'y': 230, 'width': 400, 'height': 200,
                'collision_left': -128, 'collision_right': 115,
                'collision_top': 31,
            },
            {
                'image': self.tile_02,
                'x': 730, 'y': 450, 'width': 600, 'height': 230,
                'collision_left': -270, 'collision_right': 268,
                'collision_top': 39,
            },
            {
                'image': self.tile_05,
                'x': 700, 'y': 100, 'width': 400, 'height': 200,
                'collision_left': -70, 'collision_right': 70,
                'collision_top': 27,
            }
        ]
        pass

    def draw(self):
        for platform in self.platforms:
            platform['image'].draw(
                platform['x'], platform['y'],
                platform['width'], platform['height']
            )
        pass

    def resolve_character_collision(self, character, previous_y):
        half_width = 25
        half_height = 35
        previous_bottom = previous_y - half_height
        current_bottom = character.y - half_height
        character.on_ground = False

        if character.vy > 0:
            return

        for platform in sorted(
            self.platforms,
            key=lambda item: item['y'] + item['collision_top'],
            reverse=True
        ):
            left = platform['x'] + platform['collision_left']
            right = platform['x'] + platform['collision_right']
            top = platform['y'] + platform['collision_top']
            overlaps_horizontally = (
                character.x + half_width > left
                and character.x - half_width < right
            )
            crossed_platform_top = (
                previous_bottom >= top >= current_bottom
            )

            if overlaps_horizontally and crossed_platform_top:
                character.y = top + half_height
                character.vy = 0
                character.on_ground = True
                return

    def update(self):
        pass