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
After you have showed your picture to your instructor, screenshot your picture,
name it firstname_lastname.jpg and use the submit button to e-mail it to your instructor
'''
import arcade,random
x = 250
y = 250
curve = 5
scale = 25
color = 84
curve_2 = 8
arcade.open_window(500,500,"Picasso Project") #Creates the window
arcade.set_background_color(arcade.color.MAGENTA_HAZE)
arcade.start_render()
arcade.draw_circle_filled(250,260,200,arcade.color.BURNT_ORANGE,)
for i in range(5):
    for i in range(20):
        arcade.draw_circle_filled(x,y,scale,(color,48,1))
        x += curve_2
        y += curve
        curve += .5
        scale -= 1
        color += 9
    x = 250
    y = 250
    color = 50
    curve = 5
    curve_2 -= 4
    scale = 25
arcade.finish_render()
arcade.run()