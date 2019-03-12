'''
PICASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
After you have showed your picture to your instructor, screenshot your picture,
name it firstname_lastname.jpg and use the submit button to e-mail it to your instructor
'''
x = 305
import arcade
arcade.open_window(700, 300, "Train Tracks")
arcade.set_background_color((135, 206, 250))  # Sky Blue

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 700, 65, 0, arcade.color.GHOST_WHITE)  # Ground

arcade.draw_lrtb_rectangle_filled(0, 700, 75, 65, arcade.color.GRAY)  # Tracks
for x_offset in range(0, 700, 30):
    arcade.draw_rectangle_filled(0 + x_offset, 60, 20, 10, arcade.color.BROWN_NOSE)

arcade.draw_lrtb_rectangle_filled(205, 360, 117, 100, arcade.color.GRAY)  # Main Body
arcade.draw_lrtb_rectangle_filled(205, 550, 207, 117, arcade.color.BLACK)
arcade.draw_ellipse_filled(550, 162, 15, 45, arcade.color.BLACK)
while x <= 550:
    arcade.draw_rectangle_filled(x, 162, 4, 90, arcade.color.GOLD)
    x += 81
arcade.draw_lrtb_rectangle_filled(425, 560, 118, 90, arcade.color.GRAY)
arcade.draw_lrtb_rectangle_filled(500, 540, 247, 207, arcade.color.BLACK)
point_list = ((520, 200), (485, 270,), (555, 270))
arcade.draw_polygon_filled(point_list, arcade.color.BLACK)

arcade.draw_circle_outline(350, 117, 40, arcade.color.BROWN_NOSE, 5)  # Wheels
arcade.draw_circle_outline(250, 117, 40, arcade.color.BROWN_NOSE, 5)
for wheel_spokes in range(0, 180, 30):
    arcade.draw_rectangle_filled(350, 117, 5, 80, arcade.color.BROWN_NOSE, 8 + wheel_spokes)
for wheel_spokes in range(0, 180, 30):
    arcade.draw_rectangle_filled(250, 117, 5, 80, arcade.color.BROWN_NOSE, 8 + wheel_spokes)
arcade.draw_circle_filled(450, 95, 20, arcade.color.BROWN_NOSE)
arcade.draw_circle_filled(550, 95, 20, arcade.color.BROWN_NOSE)

arcade.draw_circle_filled(346, 147, 8, arcade.color.GRAY)  # Wheel Bar
arcade.draw_circle_filled(246, 147, 8, arcade.color.GRAY)
arcade.draw_lrtb_rectangle_filled(246, 346, 153, 143, arcade.color.GRAY)
arcade.draw_lrtb_rectangle_filled(453, 471, 118, 108, arcade.color.GRAY)
arcade.draw_lrtb_rectangle_filled(470, 530, 130, 95, arcade.color.GOLD)
arcade.draw_ellipse_filled(530, 112.5, 5, 17.5, arcade.color.GOLD)
arcade.draw_rectangle_filled(400, 130, 120, 10, arcade.color.GRAY, -18)
arcade.draw_circle_filled(453, 113, 8, arcade.color.GRAY)

arcade.draw_lrtb_rectangle_filled(205, 305, 247, 160, arcade.color.LIGHT_BROWN)  # Conductors Box

arcade.finish_render()
arcade.run()
