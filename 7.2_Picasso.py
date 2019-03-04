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
circle_x = 0
arcade.open_window(500,500,"Picasso Project") #Creates the window
arcade.set_background_color(arcade.color.SKY_BLUE) #Makes background color sky color
arcade.start_render()
arcade.draw_circle_filled(300,400,100,arcade.color.SUNGLOW)

for i in range(6): #Generates Clouds
    y = random.randrange(200, 450)
    x = random.randrange(1, 501)
    for i in range(random.randrange(4,8)):
        arcade.draw_circle_filled(x,y,30,arcade.color.LIGHT_GRAY)
        x += 30

for i in range(1): #Generates the grass
    for i in range(25):
        arcade.draw_circle_filled(circle_x,25,25,arcade.color.GO_GREEN)
        circle_x += 25

arcade.draw_rectangle_filled(250,0,500,50,arcade.color.GO_GREEN)
arcade.finish_render()
arcade.run()