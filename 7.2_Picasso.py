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
arcade.open_window(400,400,"Steelers Logo")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

#diamonds

arcade.draw_polygon_filled([(200,220),(260,280),(200,340),(140,280)],(255,182,18)) #yellow
arcade.draw_circle_filled(260,220,62.5,arcade.color.WHITE)
arcade.draw_circle_filled(140,220,62.5,arcade.color.WHITE)
arcade.draw_circle_filled(140,340,62.5,arcade.color.WHITE)
arcade.draw_circle_filled(260,340,62.5,arcade.color.WHITE)

arcade.draw_polygon_filled([(200,60),(260,120),(200,180),(140,120)],(0,48,135)) #blue
arcade.draw_circle_filled(260,180,62.5,arcade.color.WHITE)
arcade.draw_circle_filled(140,180,62.5,arcade.color.WHITE)
arcade.draw_circle_filled(140,60,62.5,arcade.color.WHITE)
arcade.draw_circle_filled(260,60,62.5,arcade.color.WHITE)

arcade.draw_polygon_filled([(280,140),(340,200),(280,260),(220,200)],(198,12,48)) #red
arcade.draw_circle_filled(340,140,62.5,arcade.color.WHITE)
arcade.draw_circle_filled(340,260,62.5,arcade.color.WHITE)

arcade.draw_circle_outline(220,260,62.5,arcade.color.WHITE)
arcade.draw_arc_filled(220,260,62.5,62.5,arcade.color.WHITE,270,360)
arcade.draw_arc_filled(220,140,62.5,62.5,arcade.color.WHITE,0,90)

#foundation
arcade.draw_circle_outline(200,200,160,(16,24,32),10)
arcade.draw_circle_outline(200,200,150,(165,172,175),40)
arcade.draw_text("Steelers",80,190,(16,24,32),25,2000,"left",'Impact')

#gridlines

for x_offset in range(0,400,20):
    arcade.draw_line(0+x_offset,0,0+x_offset,400,(16,24,32),1)

for y_offset in range(0,400,20):
    arcade.draw_line(0,0+y_offset,400,0+y_offset,(16,24,32),1)

arcade.finish_render()
arcade.run()

