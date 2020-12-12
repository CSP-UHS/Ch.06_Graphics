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
#This code draws the Powerschool login window

import arcade
arcade.open_window(600,625,"Ryan Mullins")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

#gradient
arcade.draw_rectangle_filled(300,250,500,350,(245,245,245))

#mainbox
arcade.draw_lrtb_rectangle_filled(55,545,420,80,arcade.color.WHITE)

#bluebox
arcade.draw_lrtb_rectangle_filled(55,545,465,420,(0,66,124))

#studentparent
arcade.draw_text("Student and Parent Sign In",65,365,(45,45,45),15)

#sis
arcade.draw_text("PowerSchool SIS",95,435,arcade.color.WHITE,10)

#signinacc
arcade.draw_line(55,320,545,320,arcade.color.LIGHT_GRAY,1)
arcade.draw_lrtb_rectangle_outline(65,125,350,320,arcade.color.LIGHT_GRAY,1)
arcade.draw_line(65,320,125,320,arcade.color.WHITE,2)
arcade.draw_text("Sign In",75,330,arcade.color.BLACK,10)
arcade.draw_lrtb_rectangle_outline(126,236,350,320,arcade.color.LIGHT_GRAY,1)
arcade.draw_text("Create Account",136,330,arcade.color.BLACK,10)

#threebox
arcade.draw_lrtb_rectangle_filled(65,535,290,250,(245,245,245))
arcade.draw_lrtb_rectangle_filled(65,535,210,170,(245,245,245))
arcade.draw_text("Select Language",75,265,arcade.color.BLACK,10)
arcade.draw_text("Username",75,225,arcade.color.BLACK,10)
arcade.draw_text("Password",75,185,arcade.color.BLACK,10)

#input
for yoffset in range(0,81,40):
    arcade.draw_lrtb_rectangle_outline(315,530,205+yoffset,175+yoffset,(215,215,215))
    arcade.draw_lrtb_rectangle_filled(316,529,204+yoffset,176+yoffset,arcade.color.WHITE)
arcade.draw_lrtb_rectangle_outline(515,529,284,256,(205,205,205))
arcade.draw_lrtb_rectangle_filled(516,528,283,257,(235,235,235))
arcade.draw_line(519,271,522,268,(50,50,50),1)
arcade.draw_line(522,268,525,271,(50,50,50),1)
arcade.draw_text("English",325,263,arcade.color.BLACK,10)
arcade.draw_text("mullinsrya",325,223,arcade.color.BLACK,10)
for dot in range(0,57,6):
    arcade.draw_circle_filled(327+dot,190,2.5,arcade.color.BLACK)

#misc
arcade.draw_text("Forgot Username or Password?",205,145,(0,102,165),10)
arcade.draw_lrtb_rectangle_filled(490,535,105,90,(0,102,165))
arcade.draw_text("Sign In",493,91,arcade.color.WHITE,10)
icon = arcade.load_texture("powericon.png")
arcade.draw_texture_rectangle(77,444,icon.width/1.25,icon.height/1.25,icon)


arcade.finish_render()
arcade.run()



