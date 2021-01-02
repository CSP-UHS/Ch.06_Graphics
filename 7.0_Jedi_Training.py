#Sign your name: Geni Williams

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500, 400,"Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

#grid
for i in range(0, 501, 20):
    arcade.draw_line(i, 0, i, 400, arcade.color.BLACK, 2)
    arcade.draw_line(0, i, 500, i, arcade.color.BLACK, 2)

#pink rectangles
arcade.draw_rectangle_filled(50,370,60,20, arcade.color.PHLOX)
arcade.draw_rectangle_filled(200,260,20,40, arcade.color.BLUSH, 45)

#circles
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)
arcade.draw_ellipse_filled(100,100,118,40,arcade.color.AMBER)

#line & words
arcade.draw_line(80,20,120,60,arcade.color.BLUE, 2)
arcade.draw_text("I love you. I know.",20,155, arcade.color.BRICK_RED,20)

#pacman & dot
arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330)
arcade.draw_point(460,10,arcade.color.RED,10)


arcade.finish_render()
arcade.run()