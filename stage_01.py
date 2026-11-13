from pico2d import load_image

class stage_01:
    def __init__(self):
        self.tile_01=load_image('Map_01/Green_Grass/Tile_01.png')
        self.tile_02=load_image('Map_01/Green_Grass/Tile_02.png')
        self.tile_03=load_image('Map_01/Green_Grass/Tile_03.png')
        self.tile_04=load_image('Map_01/Green_Grass/Tile_04.png')
        self.tile_05=load_image('Map_01/Green_Grass/Tile_05.png')
        self.platforms = [
            (530, 1068, 489),
            (322, 565, 381),
            (38, 361, 280),
            (416, 983, 134),
            (-46, 1146, 39),
        ]
        pass

    def draw(self):
        self.tile_01.draw(550, 0, 1250, 367)
        self.tile_03.draw(700, 100, 600, 230)
        self.tile_04.draw(200,250,400,200)
        self.tile_05.draw(450,350,400,200)
        self.tile_02.draw(800,450,600,250)
        pass

    def resolve_character_collision(self, character, previous_y):
        half_width = 30
        half_height = 35
        previous_bottom = previous_y - half_height
        current_bottom = character.y - half_height
        character.on_ground = False

        if character.vy > 0:
            return

        for left, right, top in self.platforms:
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