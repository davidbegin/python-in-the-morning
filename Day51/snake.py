(
        globals().__setitem__("setvar",lambda k,v:globals().__setitem__(k,v)),
        setvar("pg",__import__("pygame")),
        setvar("random",__import__("random")),
        setvar("sys", __import__("sys")),
        setvar("locals", __import__("pygame.locals")),
        setvar("newfood",lambda:setvar("food",pg.Vector2(random.randint(3, 57)*10,random.randint(3, 57)*10))),newfood(),setvar("snakepos", pg.Vector2(30,30)),setvar("snakedir", pg.Vector2(10,0)),setvar("snakebody", []),setvar("clock", pg.time.Clock()),pg.display.set_caption("snake"),setvar("screen",pg.display.set_mode((600,600))),setvar("x",[0]),[(x.append(0),screen.fill((0,0,0)),pg.draw.rect(screen,(255, 0, 0),pg.Rect(food,(10, 10))),[(pg.draw.rect(screen,(255,255,255),pg.Rect(part,(10,10))))for part in snakebody+[snakepos]],snakebody.append(pg.Vector2(snakepos)),snakebody.remove(snakebody[0]),snakepos.__iadd__(snakedir),(setvar("snakepos", pg.Vector2(30, 30)),setvar("snakedir", pg.Vector2(10, 0)))if(snakepos in snakebody or snakepos.x == -10 or snakepos.x == 600 or snakepos.y == -10 or snakepos.y == 600)else None,(snakebody.append(pg.Vector2(snakepos)),newfood(),)if food == snakepos else None,[((pg.quit(),sys.exit(1))if event.type==locals.QUIT else((((setvar("snakedir",pg.Vector2(0,-10)))if event.key==locals.K_w else None,(setvar("snakedir",pg.Vector2(0,10)))if event.key==locals.K_s else None)if snakedir.x!=0 else((setvar("snakedir",pg.Vector2(-10,0)))if event.key==locals.K_a else None,(setvar("snakedir",pg.Vector2(10,0)))if event.key==locals.K_d else None))if event.type==locals.KEYDOWN else None))for event in pg.event.get()],pg.display.update(),clock.tick(10))for _ in x])


globals().__setitem__("setvar",lambda k,v:globals().__setitem__(k,v)),

setvar("sys", __import__("sys"))
setvar("random", __import__("random"))
setvar("time", __import__("time"))

import








