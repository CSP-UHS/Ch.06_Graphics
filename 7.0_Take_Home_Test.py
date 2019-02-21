'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade
x = 0 #Var for gridlines
y = 20     #\|/
arcade.open_window(500,400,"Pac-Man") #Creates Resolution
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
for i in range(25): #Makes Grid
    arcade.draw_line(x,0,x,400,arcade.color.BLACK,1)
    arcade.draw_line(0,y,500,y,arcade.color.BLACK,1)
    y += 20
    x += 20
arcade.draw_rectangle_filled(50,370,60,20,(arcade.color.PHLOX))
arcade.draw_text("I love you. I know.",20,160,(arcade.color.BLUSH),20)
arcade.draw_circle_filled(250,200,40,(arcade.color.WISTERIA))
arcade.draw_ellipse_filled(100,100,60,20,(arcade.color.AMBER))
arcade.draw_line(80,20,120,60,(arcade.color.BLUE),1)
point_list = ((180,245))
arcade.draw_polygon_filled(point_list,(arcade.color.YELLOW),1)
arcade.finish_render()
arcade.run()