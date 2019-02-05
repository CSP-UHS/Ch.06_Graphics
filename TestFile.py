import arcade
arcade.open_window(500,500,"Andre")
arcade.set_background_color((0,0,90))

arcade.start_render()
arcade.draw_rectangle_filled(250, 250, 50, 50, arcade.color.CARMINE_PINK)

arcade.finish_render()

arcade.run()