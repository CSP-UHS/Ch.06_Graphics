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
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''

import arcade
arcade.open_window(500,250,"")
arcade.set_background_color((255, 255, 255))
arcade.start_render()
wheelx=0

arcade.draw_lrtb_rectangle_filled(65, 430, 90, 70, (105,125,55))        #frame
arcade.draw_lrtb_rectangle_filled(100, 200, 150, 90, (105,125,55))      #hood
arcade.draw_lrtb_rectangle_filled(105, 130, 155, 150, (105,125,55))     #thingy on hood
arcade.draw_lrtb_rectangle_filled(95, 100, 145, 120, (150,150,150))     #head light
arcade.draw_lrtb_rectangle_filled(200, 300, 100, 90, (105,125,55))      #door
arcade.draw_lrtb_rectangle_filled(300, 420, 150, 90, (105,125,55))      #trunk
point_list = ((265, 100),                                               #door angle
              (300, 100),
              (300, 150))
arcade.draw_polygon_filled(point_list, (105,125,55))
point_list = ((194, 150),                                               #windsheild
              (200, 150),
              (210, 200),
              (204, 201))
arcade.draw_polygon_filled(point_list, (0,0,0))

for i in range(2):                                                       #wheels
    if i == 1:
        wheelx=250
    arcade.draw_circle_filled(115+wheelx, 60, 45, (0, 0, 0))




arcade.finish_render()
arcade.run()


