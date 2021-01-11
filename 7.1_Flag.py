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

arcade.draw_lrtb_rectangle_outline(20, 514, 280, 20, (0, 0, 0), 1)

for y in range(156, 280, 28):
    for x in range(30, 218, 33):
        arcade.draw_polygon_filled(((x, y), (x + 4, y), (x + 6, y + 4), (x + 7, y), (x + 12, y), (x + 8, y - 2), (x + 10, y - 6), (x + 6, y - 4), (x + 2, y - 6), ( x + 3, y - 2)), (255, 255, 255))

for y in range(170, 270, 28):
    for x in range(46, 204, 33):
        arcade.draw_polygon_filled(((x, y), (x + 4, y), (x + 6, y + 4), (x + 7, y), (x + 12, y), (x + 8, y - 2), (x + 10, y - 6), (x + 6, y - 4), (x + 2, y - 6), ( x + 3, y - 2)), (255, 255, 255))

arcade.finish_render()
arcade.run()
