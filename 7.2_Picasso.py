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


import arcade #Setup Arcade
arcade.open_window(1280,720, "Danny Halstead")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_text("BMW Logo",500,650,arcade.color.PURPLE_MOUNTAIN_MAJESTY,20,220,"left","Ariel", False,False,"left","baseline" ,0)

arcade.draw_circle_filled(640,360,250,arcade.color.GRAY) #BMW Logo
arcade.draw_circle_filled(640,360,240,arcade.color.BLACK)
arcade.draw_circle_filled(640,360,150,arcade.color.GRAY)
arcade.draw_circle_filled(640,360,140,arcade.color.WHITE)

arcade.draw_arc_filled(640,360,140,140,arcade.color.BLUE,0,90,0)
arcade.draw_arc_filled(640,360,140,140,arcade.color.BLUE,0,90,180)

arcade.finish_render() #Run Arcade
arcade.run()


