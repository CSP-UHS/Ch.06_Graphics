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
arcade.open_window(500,400,"Jedi Training")
arcade.set_background_color(arcade.color.CHESTNUT)
arcade.start_render()

dot_list = ((340, 80),
              (100, 200),
              (360, 380),
            (340, 80))
arcade.draw_polygon_filled(dot_list, arcade.color.CYBER_YELLOW)


point_list = ((320, 20),
              (80, 160),
              (120, 200),
              (341, 78),
              (320, 20))
arcade.draw_polygon_filled(point_list, arcade.color.CHOCOLATE)
#
arcade.draw_circle_filled(100, 180, 27, arcade.color.CHOCOLATE)
arcade.draw_circle_filled(205, 200, 30, arcade.color.FIREBRICK)
arcade.draw_circle_filled(200, 200, 30, arcade.color.FIRE_ENGINE_RED)
arcade.draw_circle_filled(305, 280, 30, arcade.color.FIREBRICK)
arcade.draw_circle_filled(300, 280, 30, arcade.color.FIRE_ENGINE_RED)
arcade.draw_circle_filled(305, 160, 30, arcade.color.FIREBRICK)
arcade.draw_circle_filled(300, 160, 30, arcade.color.FIRE_ENGINE_RED)

for x_offset in range(0,400,20):
    arcade.draw_text("pizza", 10, 0+x_offset, arcade.color.CHAMPAGNE, 20)



arcade.draw_arc_filled(330.5, 49, 27, 27,
                       arcade.color.CHROME_YELLOW, 73, 255, 1)



arcade.finish_render()
arcade.run()





arcade.finish_render()
arcade.run()





