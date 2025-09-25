from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here


running = True
x = 800 // 2
frame = 0

while running:
    clear_canvas()
    ground.draw(400, 300)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.1)



close_canvas()

