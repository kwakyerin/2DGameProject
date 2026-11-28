from pico2d import*
from transform_effect import transform_effect
from effect import Effect, FireEffect, FireAttackEffect, BubbleEffect
from Pink import Pink
from Blue import Blue
from Yellow import Yellow
from stage_01 import stage_01
from stage_01_1 import stage_01_1
from stage_02 import stage_02
from stage_02_1 import stage_02_1
from stage_03 import stage_03
from eventmap import eventmap
from bossmap import bossmap
from monster_01 import monster_01
from UI import UI

SCREEN_WIDTH = 1100
SCREEN_EDGE = 25
TRANSFORM_COOLDOWN = 11.0
STAGES = (stage_01, stage_01_1, stage_02, stage_02_1, stage_03, eventmap, bossmap)
START_STAGE = stage_01

#월드 구성하는 객체들 초기화
def reset_world():
    global running, character, transformeffect, treat_effect
    global fire_effect, fire_attack_effect, bubble_effect
    global ui
    global stage1,stage_index,monster,attack_hit,transform_cooldown_until

    running=True
    stage_index=STAGES.index(START_STAGE)
    stage1=STAGES[stage_index]()
    character=Pink()
    monster=monster_01()
    attack_hit=False
    transform_cooldown_until=0
    transformeffect=transform_effect(character.x,character.y)
    treat_effect=Effect()
    fire_effect=FireEffect()
    fire_attack_effect=FireAttackEffect()
    bubble_effect=BubbleEffect()
    ui=UI()
    pass

#게임 상태 업데이트
def update_world():
    global stage1,stage_index,attack_hit

    previous_x = character.x
    previous_y = character.y
    character.update()
    if stage_index == 0:
        monster.update(character)
        if character.is_attack and not attack_hit:
            attack_hit = monster.hit_by(character)

    if character.x >= SCREEN_WIDTH - SCREEN_EDGE:
        if stage_index < len(STAGES) - 1:
            stage_index += 1
            stage1 = STAGES[stage_index]()
            character.x = SCREEN_EDGE
            previous_x = character.x
        else:
            character.x = SCREEN_WIDTH - SCREEN_EDGE
            previous_x = character.x
    elif character.x <= SCREEN_EDGE:
        if stage_index > 0:
            stage_index -= 1
            stage1 = STAGES[stage_index]()
            character.x = SCREEN_WIDTH - SCREEN_EDGE
            previous_x = character.x
        else:
            character.x = SCREEN_EDGE
            previous_x = character.x

    stage1.resolve_character_collision(character, previous_x, previous_y)

    if stage_index == 0:
        stage1.update_leaves()
    elif stage_index == 1:
        stage1.update_leaves()
    elif stage_index == 2:
        stage1.update_rain()
    elif stage_index == 4:
        stage1.update_asteroids(character)

    hurt = getattr(character, 'hurt', None)
    if (
        stage_index == 0
        and monster.check_character_contact(character)
        and callable(hurt)
    ):
        hurt()
    ui.update(character.is_hurt)

    transformeffect.x=character.x
    transformeffect.y=character.y
    
    transformeffect.update()
    treat_effect.update(character.x, character.y)
    fire_effect.update(character.x, character.y)
    fire_attack_effect.update()
    bubble_effect.update(character.x, character.y)
    pass

#화면에 그리기
def render_world():
    clear_canvas()
    stage1.draw()
    if stage_index == 0:
        monster.draw()
    transformeffect.draw()
    treat_effect.draw()
    fire_effect.draw()
    character.draw()
    fire_attack_effect.draw()
    bubble_effect.draw()
    if stage_index == 2:
        stage1.draw_white_flash()
    ui.draw()
    update_canvas()

#캐릭터를 바꿀 때 현재 플레이 상태 유지
def transform_character(character_class):
    global character

    previous_character = character
    character = character_class()
    for attribute in (
        'x', 'y', 'frame', 'speed', 'dir', 'on_ground', 'vy',
        'gravity', 'jump_power', 'is_attack', 'animation_time'
    ):
        setattr(character, attribute, getattr(previous_character, attribute))
    transformeffect.start()

    # 현재 스테이지가 색깔 타일 맵일 때만 적용
    if isinstance(stage1, eventmap):

        if character_class == Pink:
            stage1.change_color(1)

        elif character_class == Blue:
            stage1.change_color(2)

        elif character_class == Yellow:
            stage1.change_color(3)

    transformeffect.start()

#컨트롤 관리
def handle_events():
    global running, character, attack_hit, transform_cooldown_until

    event_list = get_events()

    for event in event_list:
        if event.type == SDL_QUIT:
            running = False

        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running=False
            elif event.key==SDLK_a:
                character.dir=-1
                character.speed=4
                character.frame=0
                character.is_attack=False
            elif event.key==SDLK_d:
                character.dir=1
                character.speed=4
                character.frame=0
                character.is_attack=False
            elif event.key==SDLK_j:
                if isinstance(character, Yellow) and fire_effect.is_active:
                    fire_attack_effect.start(
                        character.x, character.y, character.dir
                    )
                    character.is_attack = False
                    character.frame = 0
                    character.animation_time = 0
                    character.speed = 0
                else:
                    was_attacking = character.is_attack
                    character.attack()
                    if not was_attacking and character.is_attack:
                        attack_hit = False
                    character.speed=0
            elif event.key==SDLK_w:
                character.jump()
            elif event.key in (SDLK_1, SDLK_2, SDLK_3):
                now = get_time()
                if now >= transform_cooldown_until:
                    if event.key==SDLK_1:
                        transform_character(Pink)
                    elif event.key==SDLK_2:
                        transform_character(Blue)
                    else:
                        transform_character(Yellow)
                    transform_cooldown_until = now + TRANSFORM_COOLDOWN
            elif event.key==SDLK_k:
                if isinstance(character, Yellow):
                    fire_effect.start(character.x, character.y)
                elif isinstance(character, Blue):
                    bubble_effect.start(character.x, character.y)
                else:
                    treat_effect.start(character.x, character.y)

        elif event.type==SDL_KEYUP:
            if event.key==SDLK_a and character.dir==-1:
                character.speed=0
                character.frame=0
            elif event.key==SDLK_d and character.dir==1:
                character.speed=0
                character.frame=0


open_canvas(SCREEN_WIDTH,650)

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()