from pico2d import*

open_canvas()

running=True

#초기화
def reset_world():
    pass

#게임 상태 업데이트
def update_world():
    pass

#화면에 그리기
def render_world():
    pass

#컨트롤 관리(현재는 esc키만 연결)
def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

while running:
    clear_canvas()
    handle_events()
    update_canvas()
    delay(0.01)

close_canvas()