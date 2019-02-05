import arcade
arcade.open_window(500,500,"Andre")
arcade.set_background_color((0,0,90))

arcade.start_render()
arcade.draw_rectangle_filled(250, 250, 50, 50, arcade.color.CARMINE_PINK)
arcade.draw_text("The tramp",250,400,arcade.color.RED,20)

arcade.finish_render()

arcade.run()