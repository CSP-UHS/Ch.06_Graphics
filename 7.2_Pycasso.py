'''
PYCASSO PROJECT
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
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''

import arcade
arcade.open_window(500, 500, "Bawi Thawng")
arcade.set_background_color(arcade.color.GREEN_YELLOW)
arcade.start_render()
for loo in range(0, 500, 20):
    arcade.draw_line(0, 20+loo, 500, 20+loo, (100, 100, 100))
for loo in range(0, 500, 20):
    arcade.draw_line(20+loo, 0, 20+loo, 500, (0, 0, 0))
# left
point_list = ((230, 285),
              (230, 460),
              (225, 460),
              (140, 325))
arcade.draw_polygon_filled(point_list, (200, 156, 34))

# right
point_list = ((270, 285),
              (270, 460),
              (275, 460),
              (360, 325))
arcade.draw_polygon_filled(point_list, (200, 156, 34))
# right part
point_list = ((350, 290),
              (350, 350),
              (360, 370),
              (380, 370),
              (390, 350),
              (387, 300),
              (370, 290))
arcade.draw_polygon_filled(point_list, (60, 40, 90))
# big disk = main body upper
arcade.draw_arc_filled(250, 250, 250, 250, (0, 0, 255), 10, 172)
# big disk = main lower body
arcade.draw_arc_filled(250, 250, 250, 250, (0, 0, 255), 10, 172, 180)

arcade.draw_xywh_rectangle_filled(230, 285, 40, 110, (90, 90, 40))
# right
point_list = ((290, 240),
              (290, 260),
              (358, 266),
              (358, 234))
arcade.draw_polygon_filled(point_list, (2, 2, 2))
point_list = ((358, 266),
              (358, 234),
              (370, 236),
              (370, 264))
arcade.draw_polygon_filled(point_list, (30, 40, 80))

# left
point_list = ((220, 240),
              (220, 260),
              (142, 266),
              (142, 234))
arcade.draw_polygon_filled(point_list, (2, 2, 2))
point_list = ((142, 266),
              (142, 234),
              (130, 236),
              (130, 264))
arcade.draw_polygon_filled(point_list, (30, 40, 80))

arcade.draw_rectangle_filled(325, 295, 25, 90, (60, 40, 90), 65)

# small arc on the lower
arcade.draw_arc_filled(250, 250, 280, 250, (40, 50, 30), 45, 137, 180)
# lower small circle
arcade.draw_circle_filled(210, 170, 13, (70, 60, 40))
arcade.draw_circle_filled(220, 200, 13, (70, 60, 40))
arcade.draw_circle_filled(250, 160, 13, (70, 60, 40))
arcade.draw_circle_filled(250, 190, 13, (70, 60, 40))
arcade.draw_circle_filled(290, 170, 13, (70, 60, 40))
arcade.draw_circle_filled(280, 200, 13, (70, 60, 40))

# upper small circle
arcade.draw_circle_filled(210, 410, 10, (20, 30, 20))
arcade.draw_circle_filled(196, 380, 10, (20, 30, 20))
arcade.draw_circle_filled(285, 410, 10, (20, 30, 20))
arcade.draw_circle_filled(299, 380, 10, (20, 30, 20))

# middle small circle
arcade.draw_circle_filled()
arcade.draw_circle_filled(250, 250, 40, (0, 255, 0))

arcade.finish_render()
arcade.run()


