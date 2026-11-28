import math
import random
from pico2d import get_time, load_image
from collision import check_platform_collision


class stage_01:
    LEAF_COUNT = 20

    def __init__(self):
        self.background=load_image('background/Stage_01.png')
        self.leaf_image=load_image('Effect/Leaf.png')
        self.leaves = [
            self._create_leaf(
                random.uniform(0, 1100),
                random.uniform(0, 650),
            )
            for _ in range(self.LEAF_COUNT)
        ]
        self.last_leaf_update_at = get_time()
        self.tree=load_image('Map_01/Tree/Tree_03.png')
        self.tree_02=load_image('Map_01/Tree/Tree_02.png')
        self.tree_01=load_image('Map_01/Tree/Tree_01.png')
        self.tile_01=load_image('Map_01/Green_Grass/Tile_01.png')
        self.tile_02=load_image('Map_01/Green_Grass/Tile_02.png')
        self.tile_04=load_image('Map_01/Green_Grass/Tile_04.png')
        self.tile_05=load_image('Map_01/Green_Grass/Tile_05.png')
        self.platforms = [
            {
                'image': self.tile_01,
                'x': 550, 'y': 0, 'width': 1250, 'height': 367,
                'collision_width': 1250, 'collision_height': 100,
                'collision_offset_x': 0, 'collision_offset_y': -150,
            },
            {
                'image': self.tile_04,
                'x': 200, 'y': 350, 'width': 400, 'height': 200,
                'collision_width': 290, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
                'image': self.tile_05,
                'x': 480, 'y': 230, 'width': 400, 'height': 200,
                'collision_width': 180, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -70,
            },
            {
                'image': self.tile_02,
                'x': 730, 'y': 450, 'width': 600, 'height': 230,
                'collision_width': 500, 'collision_height': 69,
                'collision_offset_x': 0, 'collision_offset_y': -80,
            },
            {
                'image': self.tile_05,
                'x': 700, 'y': 100, 'width': 400, 'height': 200,
                'collision_width': 180, 'collision_height': 50,
                'collision_offset_x': 0, 'collision_offset_y': -70,
            }
        ]
        pass

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
        self.tree.draw(0, 170, 270, 330)
        self.tree_02.draw(150, 150, 185, 330)
        self.tree_01.draw(1000, 140, 155, 330)

        for platform in self.platforms:
            x = platform['x']
            y = platform['y']
            w = platform['width']
            h = platform['height']

            platform['image'].draw(x, y, w, h)

        for leaf in self.leaves:
            self.leaf_image.clip_composite_draw(
                300, 494, 590, 270,
                leaf['angle'],
                leaf['flip'],
                leaf['x'],
                leaf['y'],
                leaf['width'],
                leaf['height'],
            )

    def _create_leaf(self, x=None, y=None):
        size = random.uniform(35, 55)
        return {
            'x': 1100 + size * 0.5 if x is None else x,
            'y': random.uniform(0, 650) if y is None else y,
            'age': 0,
            'drift_speed': random.uniform(45, 70),
            'fall_speed': random.uniform(25, 50),
            'sway_amplitude': random.uniform(10, 20),
            'sway_frequency': random.uniform(1.5, 2.8),
            'sway_phase': random.uniform(0, math.tau),
            'angle': random.uniform(-0.5, 0.5),
            'rotation_speed': random.uniform(-0.8, 0.8),
            'flip': random.choice(('', 'h')),
            'width': size,
            'height': size * 270 / 590,
        }

    def update_leaves(self):
        now = get_time()
        elapsed = now - self.last_leaf_update_at
        self.last_leaf_update_at = now

        for leaf in self.leaves:
            leaf['age'] += elapsed
            leaf['x'] -= leaf['drift_speed'] * elapsed
            leaf['x'] += (
                math.sin(
                    leaf['age'] * leaf['sway_frequency']
                    + leaf['sway_phase']
                )
                * leaf['sway_amplitude']
                * elapsed
            )
            leaf['y'] -= leaf['fall_speed'] * elapsed
            leaf['angle'] += leaf['rotation_speed'] * elapsed

        self.leaves = [
            leaf for leaf in self.leaves
            if leaf['y'] > -leaf['height']
            and -leaf['width'] < leaf['x'] < 1100 + leaf['width']
        ]
        while len(self.leaves) < self.LEAF_COUNT:
            self.leaves.append(self._create_leaf())

    def resolve_character_collision(self, character, previous_x, previous_y):
        character.on_ground = False

        for platform in self.platforms:
            box = self._get_platform_collision_box(platform)
            if check_platform_collision(character, box, previous_x, previous_y):
                break

    def update(self):
        pass