import pygame as pg # type: ignore
import time
import random
pg.font.init()

WIDTH, HEIGHT = 1000, 800
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Source Life")
# BG = pg.image.load("bg.jpeg")
# 0,0 is top left

#Source Tracker
source = 0
font = pg.font.SysFont("comicsans", 25)
text_surface = 0
clock = pg.time.Clock()
def draw():
#     # SCREEN.blit(BG,())
   
    pg.display.update()


def main():
    run = True
    alpha = 0
    ticks = pg.time.get_ticks()/1000
    source_score_text =0
    end_time = 0
    source_score_text = font.render("Source available: " + str(source), True, (255,255,255))
    score_x, score_y = WIDTH/2 - source_score_text.get_width()/2,10
 
    while run:
        clock.tick(60)
        ticks = pg.time.get_ticks()/1000
        
        SCREEN.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == pg.KEYDOWN:
                if(event.key == pg.K_SPACE):
                    print(" Space Down")
                    source_score_text = font.render("Source available: " + str(source), True, (255,255,255))
                    SCREEN.blit(source_score_text, (score_x, score_y))
                    end_time = ticks + 5  
                    alpha = 255     
        if source_score_text and alpha > 0: 
            source_score_text.set_alpha(alpha)
            alpha = max(alpha-4,0)
            print(alpha)
            SCREEN.blit(source_score_text, (score_x, score_y))

        draw()

    pg.quit()

if __name__ == "__main__":
    main()