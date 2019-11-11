import arcade

arcade.open_window(500,400, "Nellie Leaverton")

arcade.set_background_color(arcade.color.WHITE) #set backround color

arcade.start_render()
#######
# arcade.draw_ellipse_outline(250,200,50,60, arcade.color.BLACK)
# arcade.draw_ellipse_filled(250, 200, 50, 60, arcade.color.LIGHT_PINK)
#
# arcade.draw_arc_outline(220, 220, 7, 30,arcade.color.BLACK, 210, 330)
#
# arcade.draw_arc_outline(280, 220, 7, 30,arcade.color.BLACK, 210, 330)

########
arcade.finish_render()

arcade.run()

