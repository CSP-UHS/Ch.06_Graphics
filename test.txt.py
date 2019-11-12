import arcade

arcade.open_window(500,400, "Nellie Leaverton")

arcade.set_background_color(arcade.color.WHITE) #set backround color

arcade.start_render()
#######
arcade.draw_rectangle_outline(250,200,50,60, arcade.color.BLACK)
arcade.draw_rectangle_filled(250, 200, 50, 60, arcade.color.LIGHT_PINK)

arcade.draw_arc_outline(235, 220, 7, 30,arcade.color.BLACK, 210, 330)

arcade.draw_arc_outline(260, 220, 7, 30,arcade.color.BLACK, 210, 330)

arcade.draw_line(230, 220, 230, 222, arcade.color.BLACK, 2) #eye left bottom
arcade.draw_line(230, 230, 230, 222, arcade.color.BLACK, 2) #eye left top

arcade.draw_line(250, 240, 240, 222, arcade.color.BLACK, 2)



########
arcade.finish_render()

arcade.run()

