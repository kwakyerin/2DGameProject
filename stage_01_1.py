from pico2d import load_image

class stage_01_1:

    def __init__(self):
        self.Tile_01=load_image('Map_01/DGreen_Grass/Tile_04.png')
        self.platforms = [
            {
                'image': self.Tile_01,
                'x': 550, 'y': 0, 'width': 1250, 'height': 367,
                'collision_left': -596, 'collision_right': 596,
                'collision_top': 39,
            },
        ]
        pass

    def draw(self):
        for platform in self.platforms:
            platform['image'].draw(
                platform['x'], platform['y'],
                platform['width'], platform['height']
            )
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_y):
        character.on_ground = False
        half_width = 25
        half_height = 35

        if character.vy > 0:
            return

        previous_bottom = previous_y - half_height
        current_bottom = character.y - half_height

        for platform in self.platforms:
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
