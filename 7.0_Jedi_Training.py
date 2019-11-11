#Sign your name:____Emma Moritz_____

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500, 400, "Star Wars Art")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

for x_offset in range(0,480,20):
    arcade.draw_line(0+x_offset,0,0+x_offset,500,arcade.color.BLACK,1)#fix lines!!!!!!!!
for y_offset in range(0,380,20):
    arcade.draw_line(0,0+y_offset,400,0+y_offset,arcade.color.BLACK,1)
arcade.draw_rectangle_filled(20,480,60,20,arcade.color.PHLOX)


arcade.finish_render()
arcade.run()
#amber=oval yellow=packman Brickred=words and angled rec  wishteria=circle  blue=;line