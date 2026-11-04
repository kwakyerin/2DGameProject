from pico2d import*

open_canvas()

running=True

#esc키 연결
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