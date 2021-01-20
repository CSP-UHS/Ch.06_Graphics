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
arcade.open_window(450,800,"Daniel Mitchell Pycasso")
arcade.set_background_color((0,0,0))
arcade.start_render()

#draw body
arcade.draw_circle_filled(40,750,30,arcade.color.COOL_GREY,127)
arcade.draw_circle_filled(410,750,30,arcade.color.COOL_GREY,127)
arcade.draw_circle_filled(40,50,30,arcade.color.COOL_GREY,127)
arcade.draw_circle_filled(410,50,30,arcade.color.COOL_GREY,127)
arcade.draw_lrtb_rectangle_filled(10, 440, 750, 55,arcade.color.COOL_GREY)
arcade.draw_lrtb_rectangle_filled(40, 410, 780, 20,arcade.color.COOL_GREY)
arcade.draw_lrtb_rectangle_filled(35, 415, 735, 485,arcade.color.BLACK)

for b_off in range(0,350,70): #draw Fbuttons
    #arcade.draw_lrtb_rectangle_filled(45, 85, 475, 455, arcade.color.WHITE_SMOKE)
    arcade.draw_rectangle_filled((80+ (b_off)), 460, 45, 15, arcade.color.WHITE_SMOKE)

for m_off in range(0,200,40):  #draws the buttons to the left of the dpad
    for b_off in range(0,150,70):
        arcade.draw_rectangle_filled((80 + (b_off)), (420-(m_off)), 45, 26, arcade.color.WHITE_SMOKE)

for r_off in range(0 ,360 ,90):
    arcade.draw_arc_filled(340, 400, 70, 70, arcade.color.WHITE_SMOKE, (45 + (r_off)), (135 + (r_off)))

arcade.finish_render()

arcade.run()