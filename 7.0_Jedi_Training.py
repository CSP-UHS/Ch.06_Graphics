#Sign your name: Julie Pham

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400, "Jedi Training")

arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
'''
all drawing code
'''
#grid
for x_offset in range(0,610,20):
    arcade.draw_rectangle_filled(0+x_offset,60,1,800,arcade.color.BLACK)
for y_offset in range(0,610,20):
    arcade.draw_rectangle_filled(300, 0+y_offset, 800, 1, arcade.color.BLACK)
#purple rectangle
arcade.draw_rectangle_filled(50,370,60,20, arcade.color.PHLOX)
#I love you. I know.
arcade.draw_text("I love you. I know.", 20, 157, arcade.color.BRICK_RED, 23)
#orange oval
arcade.draw_ellipse_filled(100,100,60, 20, arcade.color.AMBER)
#line
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
#wisteria circle
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
#blush rectangle
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, 45)
#pacman
# arcade.draw_ellipse_filled(400, 320, 60, arcade.color.YELLOW, 3)
arcade.draw_arc_filled(400, 320, 60, 60, arcade.color.YELLOW, 30, 325, 0)
#point
arcade.draw_point(460,10,arcade.color.RED,5)
arcade.finish_render()
arcade.run()