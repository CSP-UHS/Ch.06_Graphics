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
import random
arcade.open_window(500, 550, "Alex Mears")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
color_list = (arcade.color.WHITE, arcade.color.RED, arcade.color.BLUE, arcade.color.ORANGE, arcade.color.GREEN,
              arcade.color.YELLOW)

x = 255     # Drawing lower right cubes
y = 253
y1 = y
a = 65
b = 70
c = 36
for l in range(4):
    for i in range(3):
        square_list = ((x, y1), (x + a, y1 + c), (x + a, (y1 + c) - b), (x, y1 - b))
        arcade.draw_polygon_filled(square_list, random.choice(color_list))
        x += a + 9
        y1 += c + 5
    y1 = y
    x = 255
    y -= b + 10

x = 245     # Drawing lower left cubes
y = 253
y1 = y
a = -65
b = 70
c = 36
for l in range(4):
    for i in range(3):
        square_list = ((x, y1), (x + a, y1 + c), (x + a, (y1 + c) - b), (x, y1 - b))
        arcade.draw_polygon_filled(square_list, random.choice(color_list))
        x += a - 9
        y1 += c + 5
    y1 = y
    x = 245
    y -= b + 10

x = 200
y = 115
x1 = 250
y1 = 260
for l in range(3):
    x2 = x1
    y2 = y1
    for i in range(3):
        top_box = ((x2, y2), (x2 - x / 3, y2 + y / 3), (x2, y2 + 2 * y / 3), (x2 + x / 3, y2 + y / 3))
        arcade.draw_polygon_filled(top_box, random.choice(color_list))
        x2 += 75
        y2 += 43
    x1 -= 75
    y1 += 42

arcade.draw_text("Ted copied me", 5, 0, arcade.color.WHITE, 24, 500)

arcade.finish_render()
arcade.run()