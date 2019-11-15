import arcade

arcade.open_window(700,400, "Nellie Leaverton")

arcade.set_background_color(arcade.color.WHITE) #set backround color

arcade.start_render()
###############
arcade.draw_lrtb_rectangle_filled(0,700,400,240, arcade.color.BOSTON_UNIVERSITY_RED) #TOP RED
arcade.draw_lrtb_rectangle_filled(0, 700, 240, 0, arcade.color.BLUEBONNET) #BOTTOM BLUE
my_list = (
    (367.5,208),
    (157.5, 272),
    ()
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
###############
arcade.finish_render()

arcade.run()
