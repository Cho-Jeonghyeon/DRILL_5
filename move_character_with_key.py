from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dirx, diry
    global motion
    # 300 숨쉬는 모션 (우) /200 숨쉬는 모션 (좌)
    # 100 달리는 모션 (우) /0 달리는 모션 (좌)
    global remember

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
                motion = 100
            elif event.key == SDLK_LEFT:
                dirx -= 1
                motion = 0
            elif event.key == SDLK_UP:
                diry += 1
                if(remember == 1):
                    motion = 100
                elif(remember == 0):
                    motion = 0
            elif event.key == SDLK_DOWN:
                diry -= 1
                if (remember == 1):
                    motion = 100
                elif (remember == 0):
                    motion = 0
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
                motion = 300
                remember = 1
            elif event.key == SDLK_LEFT:
                dirx += 1
                motion = 200
                remember = 0
            elif event.key == SDLK_UP:
                diry -= 1
                if (remember == 1):
                    motion = 300
                elif (remember == 0):
                    motion = 200
            elif event.key == SDLK_DOWN:
                diry += 1
                if (remember == 1):
                    motion = 300
                elif (remember == 0):
                    motion = 200

running = True
x = 800 // 2
y= 90
frame = 0
dirx = 0
diry = 0
motion = 300
remember = 3  #0:왼쪽, 1:오른쪽
while running:
    clear_canvas()
    ground.draw(400, 300)
    character.clip_draw(frame * 100, motion, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 10
    y += diry * 10
    delay(0.07)



close_canvas()

#character.clip_draw(frame * 100, 300, 100, 100, x, 90) 숨쉬는 모션 (우)
#character.clip_draw(frame * 100, 200, 100, 100, x, 90) 숨쉬는 모션 (좌)
#character.clip_draw(frame * 100, 100, 100, 100, x, 90) 달리는 모션 (우)
#character.clip_draw(frame * 100, 0, 100, 100, x, 90) 달리는 모션 (좌)