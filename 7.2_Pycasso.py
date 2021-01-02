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
bird_count = 0
arcade.open_window(800,600, "Geni Williams Pycasso")
arcade.set_background_color((173, 216, 230))
screen_width = 800
screen_height = 600
arcade.start_render()

#draws sea & lighthouse
arcade.draw_rectangle_filled(screen_width / 2, screen_height / 6, screen_width - 1, screen_height / 3, (52, 143, 171))
arcade.draw_rectangle_filled(100, 0, 150, 800, arcade.color.ASH_GREY)
arcade.draw_rectangle_filled(100, 100, 50, 50, arcade.color.BLACK)
arcade.draw_rectangle_filled(100, 300, 50, 50, arcade.color.BLACK)
arcade.draw_rectangle_filled(100, 400, 200, 50, arcade.color.ASH_GREY)
arcade.draw_triangle_filled(30, 425, 170, 425, 105, 525, arcade.color.AMERICAN_ROSE)
arcade.draw_circle_filled(105,525,10, (247, 244, 213))



#draws birds
def draw_bird(x, y):
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 20, y, 20, 20, arcade.color.BLACK, 90, 180)

while bird_count < 5:
    #random x & y on screen
    x = random.randrange(0, screen_width)
    y = random.randrange(screen_height / 3, screen_height - 20)
    draw_bird(x,y)
    bird_count += 1


arcade.finish_render()
arcade.run()