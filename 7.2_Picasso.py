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
import random
arcade.open_window(500,400, "Julie Pham")
arcade.set_background_color(arcade.color.LIGHT_BLUE)
arcade.start_render()

#neck
arcade.draw_rectangle_filled(420,280,169,47,arcade.color.BURLYWOOD,190)
#antler things
point_list = ((300,300),
              (300,340),
              (320,310),
              (340,340),
              (340,300))
arcade.draw_polygon_filled(point_list,arcade.color.ALLOY_ORANGE)
#antlers
arcade.draw_circle_filled(300,340,10,arcade.color.ALLOY_ORANGE)
arcade.draw_circle_filled(340,340,10,arcade.color.ALLOY_ORANGE)
#head
arcade.draw_ellipse_filled(320,280,27,30,arcade.color.BURLYWOOD)
arcade.draw_ellipse_outline(320,280,27,30,arcade.color.ALLOY_ORANGE)
#nose
arcade.draw_ellipse_filled(320,240,40,25,arcade.color.ALLOY_ORANGE,1)

#left nostril
arcade.draw_circle_filled(300,240,7,arcade.color.BLACK)
#right nostril
arcade.draw_circle_filled(340,240,7,arcade.color.BLACK)

#1
arcade.draw_ellipse_filled(380,287,20,15,arcade.color.ALLOY_ORANGE)
#2
arcade.draw_arc_filled(430,257,20,20,arcade.color.ALLOY_ORANGE,18,190)
#3
arcade.draw_arc_filled(450,310,25,15,arcade.color.ALLOY_ORANGE,200, 380)

#left eye
arcade.draw_point(310,290,arcade.color.BLACK,10)
#second eye
arcade.draw_point(330,290,arcade.color.BLACK,10)

#left ear
point_list = ((280,280),
              (240,300),
              (230,330),
              (280,320),
              (300,300),
              (280,280))
arcade.draw_polygon_filled(point_list,arcade.color.ALLOY_ORANGE)
point_list = ((300,300),
              (280,280),
              (295,280))
arcade.draw_polygon_filled(point_list,arcade.color.ALLOY_ORANGE)

#right ear
dot_list = ((340,300),
            (360,320),
            (400,340),
            (390,300),
            (360,280))
arcade.draw_polygon_filled(dot_list,arcade.color.ALLOY_ORANGE)
dot_list= ((340,300),
           (360,280),
           (345,280))
arcade.draw_polygon_filled(dot_list,arcade.color.ALLOY_ORANGE)
#CHICKEN!!!!!!!!!!
#chicken hair things
arcade.draw_ellipse_filled(100,122,10,50, arcade.color.RED)
arcade.draw_ellipse_filled(90,135,8,30,arcade.color.RED)
arcade.draw_ellipse_filled(110,135,8,30,arcade.color.RED)
#chicken wings
arcade.draw_ellipse_filled(100,100,60,30,arcade.color.EGGSHELL)
#chicken body
arcade.draw_ellipse_filled(100,100,40,50,arcade.color.EGGSHELL,1)
#chicken leg 1
arcade.draw_line(90,50,90,20,arcade.color.BLACK)
#chicken leg 2
arcade.draw_line(110,50,110,20,arcade.color.BLACK)
#chicken belly
arcade.draw_ellipse_filled(100,75,20,25,arcade.color.DUTCH_WHITE)
#chicken eyes
arcade.draw_point(90,125,arcade.color.BLACK,5)
arcade.draw_point(110,125,arcade.color.BLACK,5)
#chicken nose
new_list = ((95,120),
            (105,120),
            (100,115))
arcade.draw_polygon_filled(new_list,arcade.color.AMBER)
#chicken blushes
arcade.draw_circle_filled(85,115,5,arcade.color.BLUSH)
arcade.draw_circle_filled(116,115,5,arcade.color.BLUSH)
#grass
for i in range(0,600,1):
    wave = random.randint(-10,11)
    height = random.randint(10, 30)
    arcade.draw_line(i,0,i+wave,height,(0,128,0))
#sun
arcade.draw_circle_filled(20,400,70,arcade.color.YELLOW)
#clouds

arcade.finish_render()
arcade.run()