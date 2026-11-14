from pico2d import load_image

class eventmap_01:
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False
