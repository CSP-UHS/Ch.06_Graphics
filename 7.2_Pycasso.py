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

arcade.open_window(600, 600, "Gerardo Lopez")
arcade.set_background_color((40, 166, 44))
arcade.start_render()
# tracks
for x_offset in range(0, 610, 20):
    arcade.draw_rectangle_filled(0 + x_offset, 60, 10, 60, arcade.color.BROWN)

# rails
arcade.draw_rectangle_filled(300, 72, 600, 5, arcade.color.SILVER)
arcade.draw_rectangle_filled(300, 47, 600, 5, arcade.color.SILVER)

# train
arcade.draw_triangle_filled(180, 60, 200, 88, 200, 32, arcade.color.BRICK_RED)
arcade.draw_lrtb_rectangle_filled(200, 350, 88, 32, arcade.color.GRAY)
arcade.draw_circle_filled(220, 60, 15, arcade.color.SILVER)
arcade.draw_circle_filled(220, 60, 10, arcade.color.BLACK)
arcade.draw_arc_filled(260, 60, 80, 20, arcade.color.SMOKE, 0, 360)
arcade.draw_arc_outline(260, 60, 80, 20, arcade.color.BLACK, 0, 360)

# trees
arcade.draw_circle_filled(80, 230, 30, arcade.color.GREEN) #top circle
arcade.draw_circle_filled(80, 195, 30, arcade.color.GREEN) #bottom circle
arcade.draw_circle_filled(60, 210, 30, arcade.color.GREEN) #left circle
arcade.draw_circle_filled(100, 210, 30, arcade.color.GREEN) #right circle

arcade.draw_circle_filled(180, 330, 30, arcade.color.GREEN)
arcade.draw_circle_filled(180, 295, 30, arcade.color.GREEN)
arcade.draw_circle_filled(160, 310, 30, arcade.color.GREEN)
arcade.draw_circle_filled(200, 310, 30, arcade.color.GREEN)

arcade.draw_circle_filled(380, 530, 30, arcade.color.GREEN)
arcade.draw_circle_filled(380, 495, 30, arcade.color.GREEN)
arcade.draw_circle_filled(360, 510, 30, arcade.color.GREEN)
arcade.draw_circle_filled(400, 510, 30, arcade.color.GREEN)

arcade.draw_circle_filled(480, 230, 30, arcade.color.GREEN)
arcade.draw_circle_filled(480, 195, 30, arcade.color.GREEN)
arcade.draw_circle_filled(460, 210, 30, arcade.color.GREEN)
arcade.draw_circle_filled(500, 210, 30, arcade.color.GREEN)

arcade.draw_circle_filled(80, 530, 30, arcade.color.GREEN)
arcade.draw_circle_filled(80, 495, 30, arcade.color.GREEN)
arcade.draw_circle_filled(60, 510, 30, arcade.color.GREEN)
arcade.draw_circle_filled(100, 510, 30, arcade.color.GREEN)

arcade.draw_circle_filled(400, 340, 30, arcade.color.GREEN)
arcade.draw_circle_filled(400, 305, 30, arcade.color.GREEN)
arcade.draw_circle_filled(380, 320, 30, arcade.color.GREEN)
arcade.draw_circle_filled(420, 320, 30, arcade.color.GREEN)

arcade.draw_rectangle_filled(600,580, 250, 600, arcade.color.DIRT, 335)
arcade.draw_rectangle_filled(600,580, 200, 600, arcade.color.OCEAN_BOAT_BLUE, 335)




arcade.draw_text("Gerardo Lopez", 490, 5, arcade.color.BLACK, 12, 110)

arcade.finish_render()
arcade.run()
