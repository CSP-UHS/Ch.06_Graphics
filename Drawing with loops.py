import arcade

arcade.open_window(600,600,"Test")
arcade.start_render()
#fence posts
for x_offset in range(0,610,20):
    arcade.draw_rectangle_filled(0+x_offset,60,10,30,arcade.color.WHITE)
#rails
arcade.draw_rectangle_filled(300, 67, 600, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(300, 52, 600, 5, arcade.color.WHITE)
arcade.finish_render()
arcade.run()