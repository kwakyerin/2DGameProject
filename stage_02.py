from pico2d import load_image, draw_rectangle

class stage_02:
    def __init__(self):
        self.grass=load_image('Map_02/DGrass/Tile_01.png')
        self.Tile_01=load_image('Map_02/Blue_Cloud/BCloud_03.png')
        self.Tile_02=load_image('Map_02/Blue_Cloud/BCloud_04.png')
        self.Tile_03=load_image('Map_02/Blue_Cloud/BCloud_05.png')
        self.Tile_04=load_image('Map_02/Blue_Cloud/BCloud_02.png')
        self.Tile_05=load_image('Map_02/Blue_Cloud/BCloud_01.png')
        self.platforms = [
            {
                'x': 30, 'y': 0, 'width': 400, 'height': 200,
                'collision_left': -200, 'collision_right': 200,
                'collision_top': 39,
            },
            {
                'x': 200, 'y': 130, 'width': 100, 'height': 50,
                'collision_left': -50, 'collision_right': 50,
                'collision_top': 25,
            },
            {
                'x': 400, 'y': 200, 'width': 150, 'height': 50,
                'collision_left': -75, 'collision_right': 75,
                'collision_top': 25,
            },
            {
                'x': 50, 'y': 320, 'width': 500, 'height': 50,
                'collision_left': -250, 'collision_right': 250,
                'collision_top': 25,
            },
            {
                'x': 420, 'y': 420, 'width': 100, 'height': 50,
                'collision_left': -50, 'collision_right': 50,
                'collision_top': 25,
            },
            {
                'x': 580, 'y': 280, 'width': 80, 'height': 50,
                'collision_left': -40, 'collision_right': 40,
                'collision_top': 25,
            },
            {
                'x': 700, 'y': 150, 'width': 100, 'height': 50,
                'collision_left': -50, 'collision_right': 50,
                'collision_top': 25,
            },
            {
                'x': 880, 'y': 300, 'width': 150, 'height': 50,
                'collision_left': -75, 'collision_right': 75,
                'collision_top': 25,
            },
            {
                'x': 900, 'y': 550, 'width': 500, 'height': 50,
                'collision_left': -250, 'collision_right': 250,
                'collision_top': 25,
            },
            {
                'x': 80, 'y': 500, 'width': 150, 'height': 50,
                'collision_left': -75, 'collision_right': 75,
                'collision_top': 25,
            },
            {
                'x': 230, 'y': 600, 'width': 50, 'height': 50,
                'collision_left': -25, 'collision_right': 25,
                'collision_top': 25,
            },
            {
                'x': 600, 'y': 490, 'width': 50, 'height': 50,
                'collision_left': -25, 'collision_right': 25,
                'collision_top': 25,
            },
        ]
        pass

    def draw(self):
        self.grass.draw(30,0,400,200)
        self.Tile_01.draw(200,130,100,50)
        self.Tile_02.draw(400,200,150,50)
        self.Tile_03.draw(50,320,500,50)
        self.Tile_01.draw(420,420,100,50)
        self.Tile_04.draw(580,280,80,50)
        self.Tile_01.draw(700,150,100,50)
        self.Tile_02.draw(880,300,150,50)
        self.Tile_03.draw(900,550,500,50)
        self.Tile_02.draw(80,500,150,50)
        self.Tile_05.draw(230,600,50,50)
        self.Tile_05.draw(600,490,50,50)
        for platform in self.platforms:
            left = platform['x'] + platform['collision_left']
            right = platform['x'] + platform['collision_right']
            top = platform['y'] + platform['collision_top']
            bottom = platform['y'] - platform['height'] / 2
            draw_rectangle(left, bottom, right, top, 255, 0, 0)
        pass

    def update(self):
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