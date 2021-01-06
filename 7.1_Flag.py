'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''

import arcade

arcade.open_window(534, 300, "American Flag")
arcade.set_background_color((255, 255, 255))
arcade.start_render()

for yoffset in range(0, 260, 40):
    arcade.draw_lrtb_rectangle_filled(20, 514, 40 + yoffset, 20 + yoffset, arcade.color.RED)

arcade.draw_lrtb_rectangle_filled(20, 218, 280, 140, arcade.color.NAVY_BLUE)

# arcade.draw_polygon_filled(((0, 0), (6.4, 0), (6.4, 3.2), (9.6, 3.2), (9.6, 0), (16, 0), (16, -3.2), (12.8, -3.2), ))

arcade.draw_lrtb_rectangle_outline(20, 514, 280, 20, (0, 0, 0), 1)

arcade.draw_polygon_filled(((20, 200), (400, 200), (100, 30), (200, 300), (320, 30)), (0,200,50))
arcade.draw_polygon_outline(((20, 200), (400, 200), (100, 30), (200, 300), (320, 30)), (0,0,0))

arcade.finish_render()
arcade.run()
