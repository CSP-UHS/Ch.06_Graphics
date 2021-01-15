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

arcade.open_window(400, 700, "Joe Schmidt")
arcade.set_background_color((255, 255, 255))
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 400, 350, 0, (10, 10, 10))     # splits screen into dark and light halves

for i in range(2):
    # arcade.draw_triangle_filled(0, 350, 200, 696, 400, 350, arcade.color.BLACK)
    arcade.draw_triangle_filled(200 * i, 350, 100 + 200 * i, 523, 200 * (i + 1), 350, (254, 222, 0))
    arcade.draw_triangle_outline(200 * i, 350, 100 + 200 * i, 523, 200 * (i + 1), 350, (0, 0, 0), 2)
    arcade.draw_triangle_filled(200 * i, 350, 100 + 200 * i, 177, 200 * (i + 1), 350, (0, 0, 0))
for i in range(-1, 2, 2):
    arcade.draw_triangle_filled(100, 350 + 173 * i, 200, 350 + 346 * i, 300, 350 + 173 * i, (127 * (i + 1), 111 * (i + 1), 0))
arcade.draw_triangle_outline(100, 523, 200, 696, 300, 523, (0, 0, 0), 2)

for y in range(-1, 2, 2):
    for x in range(-1, 2, 2):
        arcade.draw_polygon_filled(((200, 350 + 110 * y), (200 + 87 * x, 350 + 202 * y), (200 + 90 * x, 350 + 200 * y),
                                    (200 + 90 * x, 350 + 180 * y), (200 + 85 * x, 350 + 150 * y)), (50 + 100 * (1 + y),
                                                                            50 + 100 * (1 + y), 50 + 100 * (1 + y)))
        arcade.draw_polygon_outline(((200, 350 + 110 * y), (200 + 87 * x, 350 + 202 * y), (200 + 90 * x, 350 + 200 * y),
                                    (200 + 90 * x, 350 + 180 * y), (200 + 85 * x, 350 + 150 * y)), (0, 0, 0))
        arcade.draw_polygon_filled(((200, 350 + 110 * y), (200 + 45 * x, 350 + 80 * y), (200 + 15 * x, 350 + 55 * y)),
                                   (50 + 100 * (1 + y), 50 + 100 * (1 + y), 50 + 100 * (1 + y)))
        arcade.draw_polygon_outline(((200, 350 + 110 * y), (200 + 45 * x, 350 + 80 * y), (200 + 15 * x, 350 + 55 * y)),
                                   (0, 0, 0))

arcade.draw_circle_filled(200, 460, 30, (100, 200, 230))            # navi
arcade.draw_circle_filled(200, 460, 25, arcade.color.BABY_BLUE)
arcade.draw_circle_filled(200, 460, 20, arcade.color.LIGHT_BLUE)


arcade.draw_circle_filled(200, 240, 30, arcade.color.RED_DEVIL)     # dark navi
arcade.draw_circle_filled(200, 240, 25, (155, 0, 0))
arcade.draw_circle_filled(200, 240, 20, (175, 0, 0))

arcade.finish_render()
arcade.run()
