from pico2d import load_image


class UI:
    HEART_COUNT = 5
    HEART_SIZE = 72
    HEART_SPACING = 8
    PANEL_WIDTH = 390
    PANEL_HEIGHT = 130
    PANEL_LEFT_MARGIN = -70
    PANEL_TOP_MARGIN = 20
    PINK_SLOT_X_RATIO = 0.32
    PINK_SLOT_Y_RATIO = 0.50
    PINK_IMAGE_SIZE = 90
    BLUE_SLOT_X_RATIO = 0.50
    BLUE_IMAGE_WIDTH = 78
    BLUE_IMAGE_HEIGHT = 80
    BLUE_X_OFFSET = 2
    BLUE_Y_OFFSET = -3
    RIGHT_MARGIN = 20
    TOP_MARGIN = 20
    SCREEN_WIDTH = 1100
    SCREEN_HEIGHT = 670

    def __init__(self):
        self.panel_image = load_image('UI/UI.png')
        self.pink_image = load_image('UI/Pink.png')
        self.blue_image = load_image('UI/Blue.png')
        self.full_heart_image = load_image('UI/Heart_01.png')
        self.empty_heart_image = load_image('UI/Heart_02.png')
        self.lost_hearts = 0
        self.was_hurt = False

    def update(self, is_hurt):
        if is_hurt and not self.was_hurt:
            self.lost_hearts = min(self.HEART_COUNT, self.lost_hearts + 1)
        self.was_hurt = is_hurt

    def draw(self):
        panel_x = self.PANEL_LEFT_MARGIN + self.PANEL_WIDTH / 2
        panel_y = (
            self.SCREEN_HEIGHT
            - self.PANEL_TOP_MARGIN
            - self.PANEL_HEIGHT / 2
        )
        self.panel_image.draw(
            panel_x,
            panel_y,
            self.PANEL_WIDTH,
            self.PANEL_HEIGHT,
        )
        panel_left = panel_x - self.PANEL_WIDTH / 2
        panel_top = self.SCREEN_HEIGHT - self.PANEL_TOP_MARGIN
        pink_x = (
            panel_left + self.PANEL_WIDTH * self.PINK_SLOT_X_RATIO
        )
        pink_y = (
            panel_top - self.PANEL_HEIGHT * self.PINK_SLOT_Y_RATIO
        )
        self.pink_image.draw(
            pink_x,
            pink_y,
            self.PINK_IMAGE_SIZE,
            self.PINK_IMAGE_SIZE,
        )
        blue_x = (
            panel_left
            + self.PANEL_WIDTH * self.BLUE_SLOT_X_RATIO
            + self.BLUE_X_OFFSET
        )
        self.blue_image.draw(
            blue_x,
            pink_y + self.BLUE_Y_OFFSET,
            self.BLUE_IMAGE_WIDTH,
            self.BLUE_IMAGE_HEIGHT,
        )

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
