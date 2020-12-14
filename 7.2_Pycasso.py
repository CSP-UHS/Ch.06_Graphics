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
arcade.open_window(500, 500, "Ian N")
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()

arcade.draw_circle_filled(475, 475, 50, arcade.color.SUNGLOW)       #Sun

arcade.draw_circle_filled(50, 450, 25, arcade.color.WHITE)      #Cloud 1
arcade.draw_circle_filled(70, 460, 25, arcade.color.WHITE)
arcade.draw_circle_filled(80, 450, 25, arcade.color.WHITE)

arcade.draw_circle_filled(175, 470, 25, arcade.color.WHITE)         #Cloud 2
arcade.draw_circle_filled(190, 450, 25, arcade.color.WHITE)
arcade.draw_circle_filled(210, 470, 25, arcade.color.WHITE)

arcade.draw_circle_filled(375, 400, 25, arcade.color.WHITE)         #Cloud 3
arcade.draw_circle_filled(350, 420, 25, arcade.color.WHITE)

arcade.draw_rectangle_filled(250, 150, 500, 300, arcade.color.GREEN)        #Grass

arcade.draw_rectangle_filled(250, 250, 300, 200, arcade.color.WHITE)        #House

arcade.draw_triangle_filled(250, 470, 50, 340, 450, 340, arcade.color.RED)      #Roof

arcade.draw_rectangle_filled(250, 212, 65, 125, arcade.color.MIDNIGHT_BLUE)     #Door
arcade.draw_circle_filled(230, 212, 5, arcade.color.SILVER_CHALICE)

arcade.draw_rectangle_outline(160, 250, 50, 50, arcade.color.BLACK)             #Window
arcade.draw_rectangle_filled(160, 250, 49, 49, arcade.color.LIGHT_CYAN)
arcade.draw_line(135, 250, 185, 250, arcade.color.BLACK)
arcade.draw_line(160, 275, 160, 225, arcade.color.BLACK)

arcade.draw_rectangle_outline(340, 250, 50, 50, arcade.color.BLACK)         #Window
arcade.draw_rectangle_filled(340, 250, 49, 49, arcade.color.LIGHT_CYAN)
arcade.draw_line(315, 250, 365, 250, arcade.color.BLACK)
arcade.draw_line(340, 275, 340, 225, arcade.color.BLACK)

arcade.draw_rectangle_filled(250, 50, 80, 200, arcade.color.GRAY)      #Path

for fence in range(4, 500, 12):                                                         #Fence
    arcade.draw_rectangle_filled(fence, 50, 10, 100, arcade.color.SADDLE_BROWN)
arcade.draw_rectangle_filled(250, 75, 500, 10, arcade.color.SADDLE_BROWN)
arcade.draw_rectangle_filled(250, 25, 500, 10, arcade.color.SADDLE_BROWN)

arcade.finish_render()
arcade.run()
