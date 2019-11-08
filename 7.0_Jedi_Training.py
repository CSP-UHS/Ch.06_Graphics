#Sign your name:____Emma Moritz_____

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(600,600, "Star Wars Art")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

for x_offset in range(0,580,22):
    arcade.draw_line(0+x_offset,0,0+x_offset,600,arcade.color.BLACK,1)
for y_offset in range(0,580,22):
    arcade.draw_line(0,0+y_offset,600,0+y_offset,arcade.color.BLACK,1)
arcade.draw_lrtb_rectangle_filled(20,560,20,60,arcade.color.BLUSH)

arcade.finish_render()
arcade.run()
