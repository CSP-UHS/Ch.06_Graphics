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
arcade.open_window(500,500,"Rowdy Alexander")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
arcade.draw_line(100,250,125,325,arcade.color.SILVER,4)
arcade.draw_line(350,250,375,325,arcade.color.SILVER,4)
arcade.draw_line(125,325,200,325,arcade.color.SILVER,4)
arcade.draw_line(200,325,200,345,arcade.color.SILVER,4)
arcade.draw_line(275,250,350,250,arcade.color.SILVER,4)
arcade.draw_line(275,325,275,345,arcade.color.SILVER,4)
arcade.draw_line(375,325,275,325,arcade.color.SILVER,4)
arcade.draw_line(200,345,275,345,arcade.color.SILVER,4)
arcade.draw_line(100,250,200,250,arcade.color.SILVER,4)
arcade.draw_line(200,250,200,230,arcade.color.SILVER,4)
arcade.draw_line(275,250,275,230,arcade.color.SILVER,4)
arcade.draw_line(200,230,275,230,arcade.color.SILVER,4)
for x in range(25):
    x+=25
    arcade.draw_line(x,0,x,500,arcade.color.WHITE,3)
for x in range(25):
        x += 450
        arcade.draw_line(x, 0, x, 500, arcade.color.WHITE, 3)
arcade.finish_render()

arcade.run()