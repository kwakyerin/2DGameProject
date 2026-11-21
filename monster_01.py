from pico2d import load_image


class monster_01:
    def __init__(self):
        self.idle_image = load_image('monster/Green_Slime/Green_Slime_Idle.png')
        self.walk_image = load_image('monster/Green_Slime/Green_Slime_Walk.png')
        self.hurt_image = load_image('monster/Green_Slime/Green_Slime_Hurt.png')
        self.x = 500
        self.y = 55
        self.state = 'idle'
        self.frame = 0
        self.animation_time = 0
        self.detection_distance = 250
        self.stop_distance = 60
        self.speed = 1.5
        self.direction = 1
        self.left_bound = 60
        self.right_bound = 1040

    def draw(self):
        if self.state == 'walk':
            image = self.walk_image
            source_x = 341 + self.frame * 362
            source_height = 682
        elif self.state == 'hurt':
            image = self.hurt_image
            source_x = 318 + self.frame * 362
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

    def hit_by(self, character):
        distance_x = self.x - character.x
        if (
            distance_x * character.dir <= 0
            or abs(distance_x) > 85
            or abs(self.y - character.y) > 80
        ):
            return False

        self.state = 'hurt'
        self.frame = 0
        self.animation_time = 0
        return True

    def update(self, character):
        if self.state == 'hurt':
            self.animation_time += 0.01
            if self.animation_time >= 0.12:
                self.frame += 1
                self.animation_time = 0
                if self.frame >= 4:
                    self.state = 'idle'
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
