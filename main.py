from pico2d import*


#월드 구성하는 객체들 초기화
def reset_world():
    global running
    running=True
    pass

#게임 상태 업데이트
def update_world():
    pass

#화면에 그리기
def render_world():
    clear_canvas()
    #여기 사이에 객체추가
    update_canvas()

#컨트롤 관리(현재는 esc키만 연결)
def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

close_canvas()