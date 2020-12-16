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
arcade.open_window(500,300,"Jacob Walters")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_line(210,230,210,255,arcade.color.BLACK,6)
arcade.draw_rectangle_filled(210,245,570,10,arcade.color.BLACK)

point_list=((475,160),(410,170),(410,160),(330,165),(330,40),(340,70),(470,145))
arcade.draw_polygon_filled(point_list,arcade.color.ARMY_GREEN)
arcade.draw_line(412,168,385,200,arcade.color.ARMY_GREEN,3)
arcade.draw_line(385,200,325,210,arcade.color.ARMY_GREEN,3)
arcade.draw_line(327,210,330,160,arcade.color.ARMY_GREEN,5)
arcade.draw_line(327,210,255,210,arcade.color.ARMY_GREEN,3)
point_list2=((332,43),(130,50),(0,60),(0,130),(130,135),(130,195),(257,211),(257,175),(330,160))
arcade.draw_polygon_filled(point_list2,arcade.color.ARMY_GREEN)
point_list3=((185,230),(240,230),(240,170),(165,170),(165,210))
arcade.draw_polygon_filled(point_list3,arcade.color.ARMY_GREEN)

for xoffset in range(0,280,140):
    arcade.draw_line(160+xoffset,10,160+xoffset,60,arcade.color.BLACK,8)
arcade.draw_line(120,12,340,12,arcade.color.BLACK,8)


arcade.finish_render()
arcade.run()
