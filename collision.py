
CHARACTER_HALF_WIDTH = 25
CHARACTER_HALF_HEIGHT = 35


def check_collision(character, platform, previous_x, previous_y):
    return check_platform_collision(character, platform, previous_x, previous_y)


def check_platform_collision(character, platform, previous_x, previous_y):
    left, bottom, right, top = platform

    previous_left = previous_x - CHARACTER_HALF_WIDTH
    previous_right = previous_x + CHARACTER_HALF_WIDTH
    previous_bottom = previous_y - CHARACTER_HALF_HEIGHT
    previous_top = previous_y + CHARACTER_HALF_HEIGHT

    current_left = character.x - CHARACTER_HALF_WIDTH
    current_right = character.x + CHARACTER_HALF_WIDTH
    current_bottom = character.y - CHARACTER_HALF_HEIGHT
    current_top = character.y + CHARACTER_HALF_HEIGHT

    overlaps_x = current_right > left and current_left < right
    overlaps_y = current_top > bottom and current_bottom < top
    horizontal_movement = character.x - previous_x
    vertical_movement = character.y - previous_y

    if overlaps_x and vertical_movement <= 0:
        crossed_top = previous_bottom >= top and current_bottom <= top
        was_overlapping_x = previous_right > left and previous_left < right
        started_inside = (
            was_overlapping_x
            and bottom <= previous_bottom < top
            and current_bottom <= top
        )
        if crossed_top or started_inside:
            character.y = top + CHARACTER_HALF_HEIGHT
            character.vy = 0
            character.on_ground = True
            return True

    if (
        overlaps_x
        and vertical_movement > 0
        and previous_top <= bottom
        and current_top >= bottom
    ):
        character.y = bottom - CHARACTER_HALF_HEIGHT
        character.vy = 0
        return True

    if (
        overlaps_y
        and horizontal_movement > 0
        and previous_right <= left
        and current_right >= left
    ):
        character.x = left - CHARACTER_HALF_WIDTH
        return True

    if (
        overlaps_y
        and horizontal_movement < 0
        and previous_left >= right
        and current_left <= right
    ):
        character.x = right + CHARACTER_HALF_WIDTH
        return True

    return False
