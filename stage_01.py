from pico2d import load_image, draw_rectangle

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
        for platform in self.platforms:
            left = platform['x'] + platform['collision_left']
            right = platform['x'] + platform['collision_right']
            top = platform['y'] + platform['collision_top']
            bottom = platform['y'] - platform['height'] / 2
            draw_rectangle(left, bottom, right, top, 255, 0, 0)
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        half_width = 25
        half_height = 35
        previous_left = previous_x - half_width
        previous_right = previous_x + half_width
        previous_bottom = previous_y - half_height
        previous_top = previous_y + half_height
        current_left = character.x - half_width
        current_right = character.x + half_width
        current_bottom = character.y - half_height
        current_top = character.y + half_height
        character.on_ground = False

        for platform in sorted(
            self.platforms,
            key=lambda item: item['y'] + item['collision_top'],
            reverse=True
        ):
            left = platform['x'] + platform['collision_left']
            right = platform['x'] + platform['collision_right']
            top = platform['y'] + platform['collision_top']
            bottom = platform['y'] - platform['height'] / 2
            overlaps_horizontally = (
                current_right > left and current_left < right
            )
            if not overlaps_horizontally:
                continue

            if character.vy <= 0 and previous_bottom >= top >= current_bottom:
                character.y = top + half_height
                character.vy = 0
                character.on_ground = True
                return
            if character.vy > 0 and previous_top <= bottom <= current_top:
                character.y = bottom - half_height
                character.vy = 0
                return
            overlaps_vertically = (
                current_top > bottom and current_bottom < top
            )
            if not overlaps_vertically:
                continue
            if previous_right <= left <= current_right:
                character.x = left - half_width
                return
            if previous_left >= right >= current_left:
                character.x = right + half_width
                return

            penetrations = [
                (current_right - left, 'left'),
                (right - current_left, 'right'),
                (current_top - bottom, 'bottom'),
                (top - current_bottom, 'top'),
            ]
            _, direction = min(penetrations)
            if direction == 'left':
                character.x = left - half_width
            elif direction == 'right':
                character.x = right + half_width
            elif direction == 'bottom':
                character.y = bottom - half_height
                character.vy = min(character.vy, 0)
            else:
                character.y = top + half_height
                character.vy = 0
                character.on_ground = True
            return

    def update(self):
        pass