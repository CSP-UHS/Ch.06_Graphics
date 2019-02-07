import arcade
x_offset = 0
arcade.open_window(500,500,"Andre")
arcade.set_background_color((arcade.color.BLACK))
arcade.start_render()

for x_offset in range(0,610,20):
    arcade.draw_circle_filled(100, 80, 10, arcade.color.PEACH)
    arcade.draw_circle_filled(95, 80, 3, arcade.color.GRAY)
    arcade.draw_circle_filled(105, 80, 3, arcade.color.GRAY)
    arcade.draw_rectangle_filled(0 + x_offset, 60, 10, 30, arcade.color.WHITE)
    arcade.draw_rectangle_filled(300, 67, 600, 5, arcade.color.WHITE)
    arcade.draw_rectangle_filled(300, 52, 600, 5, arcade.color.WHITE)
    point_list = ((-5+x_offset, 75),
                  (5+x_offset, 75),
                  (0+x_offset, 80))
    arcade.draw_polygon_filled(point_list, arcade.color.WHITE)
    arcade.draw_text("Ted Bundy RPG", 125, 350, arcade.color.RED, 25)
    arcade.draw_line(95, 77, 95, 50, arcade.color.RED, 2)
    arcade.draw_line(105, 77, 105, 20, arcade.color.RED, 2)
    arcade.draw_ellipse_filled(105, 20, 30, 15, arcade.color.RED)
    arcade.draw_line(301, 18, 349, 15, arcade.color.RED, 8)
    arcade.draw_line(300,20, 350, 20, arcade.color.PEACH,10)


arcade.finish_render()

arcade.run()