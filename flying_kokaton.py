import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    flip_bg_img = pg.transform.flip(bg_img, True, False)
    kokaton_fry_img = pg.image.load("fig/3.png")#こうかとんのsurfaceを生成
    kokaton_fry_img = pg.transform.flip(kokaton_fry_img, True, False)#画像を左右反転
    kk_rct = kokaton_fry_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed() #押されてるキーを受け取る

        x = -1
        y = 0
        if key_lst[pg.K_UP]:
            y -= 1
        if key_lst[pg.K_DOWN]:
            y += 1
        if key_lst[pg.K_LEFT]:
            x -= 1
        if key_lst[pg.K_RIGHT]:
            x += 2

        kk_rct.move_ip((x, y))

        #print(key_lst[pg.K_UP]) #押されてるときTrue

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])#screen surfaceに背景画像を張りつける
        screen.blit(flip_bg_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(flip_bg_img, [-x+4800, 0])
        #screen.blit(kokaton_fry_img, [300, 200])
        screen.blit(kokaton_fry_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()