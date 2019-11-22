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
arcade.open_window(500,400, "Julie Pham")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
#grid
for x_offset in range(0,610,20):
    arcade.draw_rectangle_filled(0+x_offset,60,1,800,arcade.color.BLACK)
for y_offset in range(0,610,20):
    arcade.draw_rectangle_filled(300, 0+y_offset, 800, 1, arcade.color.BLACK)
#neck line 1
arcade.draw_line(500,320,343,290,arcade.color.BLACK,1)
#neck line 2
arcade.draw_line(500,280,357,250,arcade.color.BLACK,1)
#left nostril
arcade.draw_circle_outline(300,240,5,arcade.color.BLACK,1)
#right nostril
arcade.draw_circle_outline(340,240,5,arcade.color.BLACK,1)
#nose
arcade.draw_ellipse_outline(320,240,40,25,arcade.color.BLACK,1)
#head
arcade.draw_arc_outline(320,280,27,30,arcade.color.BLACK,-40, 220)
#1
arcade.draw_arc_outline(380,287,20,15,arcade.color.BLACK,150,420)
#2
arcade.draw_arc_outline(430,265,20,20,arcade.color.BLACK,18,190)
#3
# arcade.draw_ellipse_outline(450,307,25,15,arcade.color.BLACK)
arcade.draw_arc_outline(450,307,25,15,arcade.color.BLACK,40, 190)
arcade.finish_render()
arcade.run()
