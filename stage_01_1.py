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
            },
            {
            'image': self.Tile_02,
            'x': 550, 'y': 150, 'width': 400, 'height': 200,
            },
            {
            'image': self.Tile_03,
            'x': 220, 'y': 250, 'width': 400, 'height': 200,
            },
            {
            'image': self.Tile_03,
            'x': 900, 'y': 250, 'width': 400, 'height': 200,
            },
            {
            'image': self.Tile_02,
            'x': 500, 'y': 400, 'width': 400, 'height': 200,
            },
            {
            'image': self.Tile_02,
            'x': 800, 'y': 480, 'width': 400, 'height': 200,
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

    def resolve_character_collision(self, character, previous_x, previous_y):
        pass
