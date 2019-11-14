import arcade

arcade.open_window(500,400, "Nellie Leaverton")

arcade.set_background_color(arcade.color.WHITE) #set backround color

arcade.start_render()
###############
arcade.draw_circle_filled(240,200, 190, arcade.color.BLACK)

arcade.draw_circle_outline(240,200, 130, arcade.color.ALABAMA_CRIMSON,3)

my_list = ((220, 200),
           (160, 300),
           (320, 300),
           (260, 200),
           (320, 100),
           (160, 100))
arcade.draw_polygon_filled(my_list, arcade.color.ALABAMA_CRIMSON)
###############
arcade.finish_render()

arcade.run()
