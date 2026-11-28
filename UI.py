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
        self.heart_image = load_image('UI/Heart_01.png')

    def draw(self):
        y = self.SCREEN_HEIGHT - self.TOP_MARGIN - self.HEART_SIZE / 2
        rightmost_x = (
            self.SCREEN_WIDTH - self.RIGHT_MARGIN - self.HEART_SIZE / 2
        )
        for index in range(self.HEART_COUNT):
            x = rightmost_x - index * (
                self.HEART_SIZE + self.HEART_SPACING
            )
            self.heart_image.draw(
                x, y, self.HEART_SIZE, self.HEART_SIZE
            )
