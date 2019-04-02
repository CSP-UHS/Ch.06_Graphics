import arcade
arcade.open_window(494,260,"flag")
arcade.set_background_color((255, 255, 255))
redy =0
stary=0
arcade.start_render()
for i in range(7):                                                               #red lines
    arcade.draw_lrtb_rectangle_filled(0, 494, 20+redy, 0+redy, (200,0,0))
    redy+= 40
arcade.draw_lrtb_rectangle_filled(0, 197.6, 260, 120, (0, 0, 128))           #blue rectangle
for i in range(5): #stars
    arcade.draw_text("*   *   *   *   *   *", 8.822, 233 - stary, (255, 255, 255), 20.246)
    arcade.draw_text("*   *   *   *   *", 24.752, 233-14.04 - stary, (255, 255, 255), 20.246)
    stary += 14.04*2
arcade.finish_render()
arcade.run()


