from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir
    global motion
    # 300 숨쉬는 모션 (우) 200 숨쉬는 모션 (좌) 100 달리는 모션 (우) 0 달리는 모션 (좌)

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                motion = 100
            elif event.key == SDLK_LEFT:
                dir -= 1
                motion = 0
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                motion = 300
            elif event.key == SDLK_LEFT:
                dir += 1
                motion = 200


running = True
x = 800 // 2
frame = 0
dir = 0
motion = 300

while running:
    clear_canvas()
    ground.draw(400, 300)
    character.clip_draw(frame * 100, motion, 100, 100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 10
    delay(0.07)



close_canvas()

#character.clip_draw(frame * 100, 300, 100, 100, x, 90) 숨쉬는 모션 (우)
#character.clip_draw(frame * 100, 200, 100, 100, x, 90) 숨쉬는 모션 (좌)
#character.clip_draw(frame * 100, 100, 100, 100, x, 90) 달리는 모션 (우)
#character.clip_draw(frame * 100, 0, 100, 100, x, 90) 달리는 모션 (좌)