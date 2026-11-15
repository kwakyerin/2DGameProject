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
            },
            {
                'image': self.tile_04,
                'x': 200, 'y': 350, 'width': 400, 'height': 200,
            },
            {
                'image': self.tile_05,
                'x': 480, 'y': 230, 'width': 400, 'height': 200,
            },
            {
                'image': self.tile_02,
                'x': 730, 'y': 450, 'width': 600, 'height': 230,
            },
            {
                'image': self.tile_05,
                'x': 700, 'y': 100, 'width': 400, 'height': 200,
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

    def resolve_character_collision(self, character, previous_x, previous_y):
        pass

    def update(self):
        pass