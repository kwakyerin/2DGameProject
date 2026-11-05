from pico2d import*
from Pink import Pink

#월드 구성하는 객체들 초기화
def reset_world():
    global running,pink
    running=True
    pink=Pink()
    pass

#게임 상태 업데이트
def update_world():
    pink.update()
    pass

#화면에 그리기
def render_world():
    clear_canvas()
    pink.draw()
    update_canvas()

#컨트롤 관리(현재는 esc키만 연결)
def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False

        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running=False
            elif event.key==SDLK_a:
                pink.dir=-1
                pink.speed=3
                pink.frame=0
            elif event.key==SDLK_d:
                pink.dir=1
                pink.speed=3
                pink.frame=0

        elif event.type==SDL_KEYUP:
            if event.key==SDLK_a and pink.dir==-1:
                pink.speed=0
                pink.frame=0
            elif event.key==SDLK_d and pink.dir==1:
                pink.speed=0   
                pink.frame=0                


open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()