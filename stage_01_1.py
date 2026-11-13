from pico2d import load_image

class stage_01_1:

    def __init__(self):
        self.Tile_01=load_image('Map_01/DGreen_Grass/Tile_04.png')
        self.Tile_02=load_image('Map_01/DGreen_Grass/Tile_01.png')
        self.Tile_03=load_image('Map_01/DGreen_Grass/Tile_02.png')
        self.platforms = [
            {
            'image': self.Tile_01,
            'x': 550, 'y': 0, 'width': 1250, 'height': 367,
            'collision_left': -596, 'collision_right': 596,
            'collision_top': 39,
            },
            {
            'image': self.Tile_02,
            'x': 550, 'y': 150, 'width': 400, 'height': 200,
            'collision_left': -596, 'collision_right': 596,
            'collision_top': 39,
            },
            {
            'image': self.Tile_03,
            'x': 220, 'y': 250, 'width': 400, 'height': 200,
            'collision_left': -596, 'collision_right': 596,
            'collision_top': 39,
            },
            {
            'image': self.Tile_03,
            'x': 900, 'y': 250, 'width': 400, 'height': 200,
            'collision_left': -596, 'collision_right': 596,
            'collision_top': 39,
            },
            {
            'image': self.Tile_02,
            'x': 500, 'y': 400, 'width': 400, 'height': 200,
            'collision_left': -596, 'collision_right': 596,
            'collision_top': 39,
            },
            {
            'image': self.Tile_02,
            'x': 800, 'y': 480, 'width': 400, 'height': 200,
            'collision_left': -596, 'collision_right': 596,
            'collision_top': 39,
            }

        ]

    def draw(self):
        for platform in self.platforms:
            platform['image'].draw(
                platform['x'], platform['y'],
                platform['width'], platform['height']
            )

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_y):
        character.on_ground = False
        half_width = 25
        half_height = 35

        previous_bottom = previous_y - half_height
        current_bottom = character.y - half_height

        for platform in self.platforms:
            left = platform['x'] + platform['collision_left']
            right = platform['x'] + platform['collision_right']
            top = platform['y'] + platform['collision_top']

            if (
                character.vy <= 0
                and character.x + half_width > left
                and character.x - half_width < right
                and previous_bottom >= top >= current_bottom
            ):
                character.y = top + half_height
                character.vy = 0
                character.on_ground = True
                return
