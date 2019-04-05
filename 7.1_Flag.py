import arcade
arcade.open_window(494,260,"The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for y_offset in range(0,260,40):
    arcade.draw_rectangle_filled(247,10+y_offset,494,20,((191,10,48)))
arcade.draw_rectangle_filled(98.8,195,197.6,150,((0,40,104)))
for star_offset1 in range(0,130,28):
    arcade.draw_text("*   *   *   *   *   *",16.38,231.92-star_offset1,arcade.color.WHITE,20)
for star_offset2 in range(0,85,28):
    arcade.draw_text("*   *   *   *   *",32.76,217.92-star_offset2,arcade.color.WHITE,20)
arcade.finish_render()
arcade.run()