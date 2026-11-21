from pico2d import draw_rectangle, load_image

from collision import CHARACTER_HALF_HEIGHT, CHARACTER_HALF_WIDTH


class monster_01:
    def __init__(self):
        self.idle_image = load_image('monster/Green_Slime/Green_Slime_Idle.png')
        self.walk_image = load_image('monster/Green_Slime/Green_Slime_Walk.png')
        self.hurt_image = load_image('monster/Green_Slime/Green_Slime_Hurt.png')
        self.death_image = load_image('monster/Green_Slime/Green_Slime_Death.png')
        self.x = 500
        self.y = 55
        self.state = 'idle'
        self.frame = 0
        self.animation_time = 0
        self.health = 3
        self.detection_distance = 250
        self.stop_distance = 60
        self.speed = 1.5
        self.direction = 1
        self.left_bound = 60
        self.right_bound = 1040
        self.character_touching = False

    def draw(self):
        if self.state == 'dead':
            return

        if self.state == 'walk':
            image = self.walk_image
            source_x = 341 + self.frame * 362
            source_height = 682
        elif self.state == 'hurt':
            image = self.hurt_image
            source_x = 318 + self.frame * 362
            source_height = 682
        elif self.state == 'death':
            image = self.death_image
            source_x = self.frame * 341
            source_height = 682
        else:
            image = self.idle_image
            source_x = (self.frame + 1) * 362
            source_height = 725

        if self.direction < 0:
            image.clip_composite_draw(
                source_x, 0, 362, source_height, 0, 'h',
                self.x, self.y, 65, 120
            )
        else:
            image.clip_draw(
                source_x, 0, 362, source_height,
                self.x, self.y, 65, 120
            )

        if self.state != 'death':
            self.draw_health_bar()

    def draw_health_bar(self):
        bar_width = 48
        bar_height = 3
        left = self.x - bar_width / 2
        bottom = self.y + 35

        draw_rectangle(
            left, bottom, left + bar_width, bottom + bar_height,
            180, 35, 35, 255, True
        )
        if self.health > 0:
            fill_width = bar_width * self.health / 3
            draw_rectangle(
                left, bottom, left + fill_width, bottom + bar_height,
                45, 210, 60, 255, True
            )

    def hit_by(self, character):
        if self.state in ('death', 'dead'):
            return False

        distance_x = self.x - character.x
        if (
            distance_x * character.dir <= 0
            or abs(distance_x) > 85
            or abs(self.y - character.y) > 80
        ):
            return False

        self.health -= 1
        self.state = 'death' if self.health == 0 else 'hurt'
        self.frame = 0
        self.animation_time = 0
        return True

    def check_character_contact(self, character):
        if self.state in ('death', 'dead'):
            self.character_touching = False
            return False

        touching = (
            abs(self.x - character.x) <= CHARACTER_HALF_WIDTH + 65 / 2
            and abs(self.y - character.y) <= CHARACTER_HALF_HEIGHT + 120 / 2
        )
        entered_contact = touching and not self.character_touching
        self.character_touching = touching
        return entered_contact

    def update(self, character):
        if self.state == 'dead':
            return

        if self.state in ('hurt', 'death'):
            self.animation_time += 0.01
            if self.animation_time >= 0.12:
                self.frame += 1
                self.animation_time = 0
                frame_count = 6 if self.state == 'death' else 4
                if self.frame >= frame_count:
                    self.state = 'dead' if self.state == 'death' else 'idle'
                    self.frame = 0
            return

        distance_x = character.x - self.x
        absolute_distance = abs(distance_x)
        next_state = (
            'walk'
            if absolute_distance <= self.detection_distance
            and absolute_distance > self.stop_distance
            else 'idle'
        )

        if absolute_distance <= self.detection_distance and distance_x != 0:
            self.direction = 1 if distance_x > 0 else -1

        if next_state != self.state:
            self.state = next_state
            self.frame = 0
            self.animation_time = 0

        if self.state == 'walk':
            self.x += self.speed * self.direction
            self.x = max(self.left_bound, min(self.right_bound, self.x))

        self.animation_time += 0.01
        frame_delay = 0.12 if self.state == 'walk' else 0.15
        if self.animation_time >= frame_delay:
            self.frame = (self.frame + 1) % 4
            self.animation_time = 0
