'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Typed: Noah Mable

Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"ch7")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
linexincrement=0
lineyincrement=0
for i in range(26):                                                                      #xlines
    arcade.draw_line(linexincrement, 0, linexincrement, 400, arcade.color.BLACK, 1)
    linexincrement+=20
for i in range(20):                                                                     #ylines
    arcade.draw_line(0, lineyincrement, 500, lineyincrement, arcade.color.BLACK, 1)
    lineyincrement+= 20
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE, 1)                                 #blue line
arcade.draw_rectangle_filled(460, 10, 5, 5, arcade.color.RED)                                #square
arcade.draw_ellipse_filled(100, 100, 60, 20, arcade.color.AMBER)                            #ellipse
arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BLUSH, 20)                    #text
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)                             #circle
arcade.draw_lrtb_rectangle_filled(20, 80, 380, 360, arcade.color.PHLOX)                     #rectangle
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, 45)                      #rotated rectangle
arcade.draw_arc_filled(400, 320, 60, 60, arcade.color.YELLOW, 30, 330, 0)
arcade.finish_render()
arcade.run()