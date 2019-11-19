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
b = 300
c = 270
d = 249

my_list=()
##### for the loop
# 1
for i in range(2):
    my_list = (
        (0,a),
        (120, b),
        (120, c),
        (0, d)
        )
    arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
    a = a - 30
    b = b - 30
    c = c - 30
    d = d - 30

### #2
x = 270
j = 201
k = 230
m = 300
for i in range(2):
    my_list = (
        (120, x),
        (350, j),
        (350, k),
        (120, m))
    arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
    x = x - 30
    j = j - 30
    k = k - 30
    m = m - 30
# ### #3
n = 230
o = 300
p = 270
q = 202
for i in range(2):
    my_list = (
        (350, n),
        (580, o),
        (580, p),
        (350, q)
    )
    arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
    n = n - 30
    o = o - 30
    p = p - 30
    q = q - 30
### #4
w = 300
v = 280
x = 250
y = 270
for i in range(2):
    my_list = (
        (580, w),
        (700, v),
        (700, x),
        (580, y)
    )
    arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
    w = w - 30
    v = v - 30
    x = x - 30
    y = y - 30
# ## line
e = 279
f = 300
g = 233
h = 280
for i in range (3):
    my_list = (
        (0, e),
        (120, f),
        (350, g),
        (580, f),
        (700, h),
        #back around
        (580, f),
        (350, g),
        (120, f),
    )
    arcade.draw_polygon_outline(my_list, arcade.color.BLACK, 4)
    e = e - 30
    f = f - 30
    g = g - 30
    h = h - 30

######STAR#######
######STAR#######
######STAR#######
######STAR#######
######STAR#######
######STAR#######
######STAR#######

my_list = (   ### Bottom point
    (340, 160),
    (360, 160),
    (350, 90)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)

## Second bottom left
my_list = (   ###  secpmd Bottom point
    (310, 180),
    (340, 160),
    (300, 150)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)

## third bp
my_list = (   ### third bp
    (310, 220),
    (310, 180),
    (250, 200)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
## left top
my_list = (   ### left top point
    (340, 240),
    (310, 220),
    (300, 260)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)


### top
my_list = (   ### top point
    (360, 240),
    (340, 240),
    (350, 320)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)

## left of top point
my_list = (   ### top left point
    (390, 220),
    (360, 240),
    (400, 260)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)

# left 2 tp
my_list = (   ### left 2 bp
    (390, 180),
    (390, 220),
    (450, 200)
)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)

# left of bp
my_list = (
    (360, 160),
    (390, 180),
    (400, 150)
)

arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)

#middle star
my_list =(
    (360, 160),
    (340, 160),
    (310, 180),
    (310, 220),
    (340, 240),
    (360, 240),
    (390, 220),
    (390, 180)

)
arcade.draw_polygon_filled(my_list, arcade.color.UROBILIN)
######STAR#######


my_list =(
    (350, 90),
    (340, 160),
    (300, 150),
    (310, 180),
    (250, 200),
    (310, 220),
    (300, 260),
    (340, 240),
    (350, 320),
    (360, 240),
    (400, 260),
    (390, 220),
    (450, 200),
    (390, 180),
    (400, 150),
    (360, 160)

)
arcade.draw_polygon_outline(my_list, arcade.color.BLACK, 4)
################################################################
################################################################
arcade.finish_render()

arcade.run()