from pico2d import load_image


class UI:
    HEART_COUNT = 5
    HEART_SIZE = 72
    HEART_SPACING = 8
    RIGHT_MARGIN = 20
    TOP_MARGIN = 20
    SCREEN_WIDTH = 1100
    SCREEN_HEIGHT = 650

    def __init__(self):
        self.full_heart_image = load_image('UI/Heart_01.png')
        self.empty_heart_image = load_image('UI/Heart_02.png')
        self.lost_hearts = 0
        self.was_hurt = False

    def update(self, is_hurt):
        if is_hurt and not self.was_hurt:
            self.lost_hearts = min(self.HEART_COUNT, self.lost_hearts + 1)
        self.was_hurt = is_hurt

    def draw(self):
        y = self.SCREEN_HEIGHT - self.TOP_MARGIN - self.HEART_SIZE / 2
        leftmost_x = (
            self.SCREEN_WIDTH
            - self.RIGHT_MARGIN
            - self.HEART_SIZE / 2
            - (self.HEART_COUNT - 1) * (
                self.HEART_SIZE + self.HEART_SPACING
            )
        )
        for index in range(self.HEART_COUNT):
            x = leftmost_x + index * (self.HEART_SIZE + self.HEART_SPACING)
            image = (
                self.empty_heart_image
                if index < self.lost_hearts
                else self.full_heart_image
            )
            image.draw(x, y, self.HEART_SIZE, self.HEART_SIZE)
