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

arcade.open_window(700,400, "Nellie Leaverton")
arcade.start_render()
###############################################################
###############################################################
arcade.draw_lrtb_rectangle_filled(0,700,400,240, arcade.color.BOSTON_UNIVERSITY_RED) #TOP RED
arcade.draw_lrtb_rectangle_filled(0, 700, 240, 0, arcade.color.BLUEBONNET) #BOTTOM BLUE
### #1 YELLOW
a = 279
b = 303
c = 270
d = 249

my_list=()
###### for the loop
# for i in range(2):
#     my_list = (
#         (0,a),
#         (120, b),
#         (120, c),
#         (0, d)
#         )
#     arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
#     a = a - 20
#     b = b - 20
#     c = c - 20
#     d = d - 20
############

my_list = (
    (0,a),
    (120, b),
    (120, c),
    (0, d)
    )
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
### #2
my_list = (
    (120, 270),
    (350, 200),
    (350, 233),
    (120, 303)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
### #3
my_list = (
    (350, 233),
    (580, 303),
    (580, 270),
    (350, 200)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
### #4
my_list = (
    (580, 304),
    (700, 280),
    (700, 249),
    (580, 270)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)

######STAR#######

my_list = (   ### Bottom point
    (340, 190),
    (360, 190),
    (350, 120)
)
arcade.draw_polygon_filled(my_list, arcade.color.BLACK)

## Second bottom left
my_list = (   ###  secpmd Bottom point
    (320, 201),
    (340, 190),
    (300, 180)
)
arcade.draw_polygon_filled(my_list, arcade.color.BLACK)

## third bp
my_list = (   ### third bp
    (320, 230),
    (320, 201),
    (270, 215)
)
arcade.draw_polygon_filled(my_list, arcade.color.BLACK)
## left top
my_list = (   ### left top point
    (340, 240),
    (320, 230),
    (310, 260)
)
arcade.draw_polygon_filled(my_list, arcade.color.BLACK)


### top
my_list = (   ### top point
    (360, 240),
    (340, 240),
    (350, 320)
)
arcade.draw_polygon_filled(my_list, arcade.color.BLACK)

## left of top point
my_list = (   ### top left point
    (380, 230),
    (360, 240),
    (390, 260)
)
arcade.draw_polygon_filled(my_list, arcade.color.BLACK)

## left 2 tp
my_list = (   ### Bottom point
    (380, 200),
    (380, 230),
    (430, 215)
)
arcade.draw_polygon_filled(my_list, arcade.color.BLACK)

## left of bp

my_list = (   ### Bottom point
    (360, 190),
    (380, 200),
    (390, 180)
)
arcade.draw_polygon_filled(my_list, arcade.color.BLACK)



################################################################
################################################################
arcade.finish_render()

arcade.run()