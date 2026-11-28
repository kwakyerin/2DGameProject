import random
from pico2d import get_time, load_image
from collision import check_platform_collision

class stage_01_1:
    LEAF_FRAMES = (
        (37, 233, 453, 341),
        (562, 247, 486, 318),
        (1139, 239, 464, 360),
        (1666, 269, 442, 252),
    )
    LEAF_MIN_SPAWN_INTERVAL = 0.55
    LEAF_MAX_SPAWN_INTERVAL = 1.2
    LEAF_SPAWN_Y = 700
    LEAF_FALL_SPEED_RANGE = (70, 100)
    LEAF_DRIFT_SPEED_RANGE = (25, 45)
    LEAF_SIZE_RANGE = (30, 48)

    def __init__(self):
        self.background=load_image('background/Stage_01_2.png')
        self.leaf_image=load_image('Effect/Leaf_02.png')
        self.leaves=[]
        now = get_time()
        self.last_leaf_update_at = now
        self.next_leaf_spawn_at = now + random.uniform(
            self.LEAF_MIN_SPAWN_INTERVAL,
            self.LEAF_MAX_SPAWN_INTERVAL,
        )
        self.Tile_01=load_image('Map_01/DGreen_Grass/Tile_04.png')
        self.Tile_02=load_image('Map_01/DGreen_Grass/Tile_01.png')
        self.Tile_03=load_image('Map_01/DGreen_Grass/Tile_02.png')
        self.platforms = [
            {
            'image': self.Tile_01,
            'x': 550, 'y': 0, 'width': 1250, 'height': 367,
            'collision_width': 1250, 'collision_height': 100,
            'collision_offset_x': 0, 'collision_offset_y': -150,
            },
            {
            'image': self.Tile_02,
            'x': 550, 'y': 150, 'width': 400, 'height': 200,
            'collision_width': 180, 'collision_height': 50,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
            'image': self.Tile_03,
            'x': 220, 'y': 250, 'width': 400, 'height': 200,
            'collision_width': 320, 'collision_height': 60,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
            'image': self.Tile_03,
            'x': 900, 'y': 250, 'width': 400, 'height': 200,
            'collision_width': 320, 'collision_height': 60,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
            'image': self.Tile_02,
            'x': 500, 'y': 400, 'width': 400, 'height': 200,
            'collision_width': 180, 'collision_height': 50,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
            'image': self.Tile_02,
            'x': 800, 'y': 480, 'width': 400, 'height': 200,
            'collision_width': 180, 'collision_height': 50,
            'collision_offset_x': 0, 'collision_offset_y': -70,
            }

        ]

    def _get_platform_collision_box(self, platform):
        x = platform['x'] + platform['collision_offset_x']
        width = platform['collision_width']
        top = (
            platform['y'] + platform['height'] / 2
            + platform['collision_offset_y']
        )
        height = platform['collision_height']

        left = x - width / 2
        right = x + width / 2
        bottom = top - height
        return left, bottom, right, top

    def draw(self):
        self.background.draw(550, 325, 1100, 650)

        for platform in self.platforms:
            platform['image'].draw(
                platform['x'], platform['y'],
                platform['width'], platform['height']
            )

        for leaf in self.leaves:
            frame_left, frame_bottom, frame_width, frame_height = (
                self.LEAF_FRAMES[leaf['frame']]
            )
            draw_width = leaf['size']
            draw_height = draw_width * frame_height / frame_width
            self.leaf_image.clip_composite_draw(
                frame_left,
                frame_bottom,
                frame_width,
                frame_height,
                leaf['angle'],
                leaf['flip'],
                leaf['x'],
                leaf['y'],
                draw_width,
                draw_height,
            )

    def update_leaves(self):
        now = get_time()
        elapsed = now - self.last_leaf_update_at
        self.last_leaf_update_at = now

        while now >= self.next_leaf_spawn_at:
            self.leaves.append({
                'x': random.uniform(0, 1100),
                'y': self.LEAF_SPAWN_Y,
                'frame': random.randrange(len(self.LEAF_FRAMES)),
                'fall_speed': random.uniform(*self.LEAF_FALL_SPEED_RANGE),
                'drift_speed': random.uniform(
                    *self.LEAF_DRIFT_SPEED_RANGE
                ),
                'angle': random.uniform(0, 6.283185307179586),
                'rotation_speed': random.choice((-1, 1)) * random.uniform(
                    0.3, 0.7
                ),
                'flip': random.choice(('', 'h')),
                'size': random.uniform(*self.LEAF_SIZE_RANGE),
            })
            self.next_leaf_spawn_at += random.uniform(
                self.LEAF_MIN_SPAWN_INTERVAL,
                self.LEAF_MAX_SPAWN_INTERVAL,
            )

        for leaf in self.leaves:
            leaf['x'] -= leaf['drift_speed'] * elapsed
            leaf['y'] -= leaf['fall_speed'] * elapsed
            leaf['angle'] += leaf['rotation_speed'] * elapsed

        self.leaves = [
            leaf for leaf in self.leaves
            if leaf['y'] > -leaf['size']
            and -leaf['size'] < leaf['x'] < 1100 + leaf['size']
        ]

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_x, previous_y):
                break
