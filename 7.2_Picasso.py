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
import arcade;x=50;w=33.3;i=0;y=44
arcade.open_window(500,500,"Kenny Flory");arcade.set_background_color(arcade.color.BLACK);arcade.start_render()
#Moon
arcade.draw_circle_filled(250,425,50,arcade.color.ASH_GREY)
arcade.draw_circle_filled(250,390,15,arcade.color.BATTLESHIP_GREY)
#Buildings
arcade.draw_rectangle_outline(50,175,100,350,arcade.color.WHITE)
arcade.draw_triangle_outline(0,350,50,450,100,350,arcade.color.WHITE)
arcade.draw_line(0,350,100,350,arcade.color.BLACK)
arcade.draw_rectangle_outline(150,75,100,150,arcade.color.WHITE)
arcade.draw_rectangle_outline(250,125,100,250,arcade.color.WHITE)
arcade.draw_rectangle_outline(400,150,200,300,arcade.color.WHITE)
#doors
for i in range(3):
    arcade.draw_rectangle_filled(x,10,15,20,arcade.color.WOOD_BROWN)
    x+=100
arcade.finish_render();arcade.run()