from pico2d import*
from Pink import Pink
from Blue import Blue
from Yellow import Yellow

#월드 구성하는 객체들 초기화
def reset_world():
    global running,character
    running=True
    character=Pink()
    pass

#게임 상태 업데이트
def update_world():
    character.update()
    pass

#화면에 그리기
def render_world():
    clear_canvas()
    character.draw()
    update_canvas()

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
                character=Pink()
            elif event.key==SDLK_2:
                character=Blue()
            elif event.key==SDLK_3:
                character=Yellow()

        elif event.type==SDL_KEYUP:
            if event.key==SDLK_a and character.dir==-1:
                character.speed=0
                character.frame=0
            elif event.key==SDLK_d and character.dir==1:
                character.speed=0
                character.frame=0


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()