import arcade
def star(star_x,star_y,second):
    for i in range(5):
        for i in range(6):
            arcade.draw_text("*", star_x, star_y, arcade.color.BLACK, 20)
            star_x += 32.76
        if second == 1:
            star_x
        else:
            star_y -= 28.08
            star_x = 15.38


arcade.open_window(494,260,"The Stars and Stripes")
arcade.set_background_color((255,255,255))
arcade.start_render()
star(15.38,230,0)
star(32.76,215.96,1)
arcade.finish_render()
arcade.run()