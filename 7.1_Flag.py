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
arcade.open_window(494, 260, 'The Stars and Stripes')
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range (7): # #draws the stripes
    arcade.draw_rectangle_filled(494/2, (260/26)+40*i, 494, 260/13, (191, 10, 48))
arcade.draw_lrtb_rectangle_filled(0, 197.6, 260, 120, (0, 40, 104))  # #draws the blue rectangle
for y in range (5):     # #draws the larger rectangle of stars
    for x in range(6):
        arcade.draw_text("*", 16.38+(32.76*x), 260-18.04-28.08*y, arcade.color.WHITE, 16, align="center", width=100,
                         anchor_y="center", anchor_x="center")
for y in range (4):     # #draws the smaller rectangle of stars
    for x in range (5):
        arcade.draw_text("*", 32.76+(32.76*x), 260-32.08-28.0*y, arcade.color.WHITE, 16, align="center", width=100,
                         anchor_y="center", anchor_x="center")
arcade.finish_render()
arcade.run()