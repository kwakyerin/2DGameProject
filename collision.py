

def check_collision(character, platform, previous_y):
    half_width = 25
    half_height = 35

    left, bottom, right, top = platform

    previous_bottom = previous_y - half_height
    current_bottom = character.y - half_height

    if character.x + half_width <= left:
        return False

    if character.x - half_width >= right:
        return False

    if (
        character.vy <= 0
        and previous_bottom >= current_bottom
        and current_bottom <= top
    ):
        character.y = top + half_height
        character.vy = 0
        character.on_ground = True
        return True

    return False
