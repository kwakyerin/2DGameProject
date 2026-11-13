from pico2d import*
from transform_effect import transform_effect
from Pink import Pink
from Blue import Blue
from Yellow import Yellow
from stage_01 import stage_01

#월드 구성하는 객체들 초기화
def reset_world():
    global running,character,transformeffect,stage1

    running=True
    stage1=stage_01()
    character=Pink()
    transformeffect=transform_effect(character.x,character.y)
    pass

#게임 상태 업데이트
def update_world():
    previous_y = character.y
    character.update()
    stage1.resolve_character_collision(character, previous_y)

    transformeffect.x=character.x
    transformeffect.y=character.y
    
    transformeffect.update()
    pass

#화면에 그리기
def render_world():
    clear_canvas()
    stage1.draw()
    transformeffect.draw()
    character.draw()
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

#컨트롤 관리
def handle_events():
    global running, character

    event_list = get_events()

    for event in event_list:
        if event.type == SDL_QUIT:
            running = False

        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running=False
            elif event.key==SDLK_a:
                character.dir=-1
                character.speed=3
                character.frame=0
                character.is_attack=False
            elif event.key==SDLK_d:
                character.dir=1
                character.speed=3
                character.frame=0
                character.is_attack=False
            elif event.key==SDLK_j:
                character.attack()
                character.speed=0
            elif event.key==SDLK_w:
                character.jump()
            elif event.key==SDLK_1:
                transform_character(Pink)
            elif event.key==SDLK_2:
                transform_character(Blue)
            elif event.key==SDLK_3:
                transform_character(Yellow)

        elif event.type==SDL_KEYUP:
            if event.key==SDLK_a and character.dir==-1:
                character.speed=0
                character.frame=0
            elif event.key==SDLK_d and character.dir==1:
                character.speed=0
                character.frame=0


open_canvas(1100,650)

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()