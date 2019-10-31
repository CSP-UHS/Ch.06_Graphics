#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK,ALMOND,PHLOX,BLUSH,RED,BLUE, WISTERIA,AMBER,
BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
y= 0
x=0

arcade.open_window(500,400, "Hello")

arcade.set_background_color(arcade.color.ALMOND) #set backround color

arcade.start_render()
#draw in here

#fence posts
for x_offset in range(0,610,20):
    arcade.draw_rectangle_filled(0+x_offset, 60, 1, 700, arcade.color.BLACK)
for i in range(25):
    arcade.draw_line(0, y, 600, y, arcade.color.BLACK)
    y+=20

arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX)

arcade.draw_rectangle_filled(460, 10, 5, 5, arcade.color.RED)

arcade.draw_line(120,60,80,20, arcade.color.BLUE)

arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)

arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20)

arcade.draw_ellipse_filled(100, 100, 60, 20, arcade.color.AMBER)

arcade.draw_rectangle_filled(200, 300, 40, 20, arcade.color.BLUSH, 45)




#draw in here
arcade.finish_render()

arcade.run()
