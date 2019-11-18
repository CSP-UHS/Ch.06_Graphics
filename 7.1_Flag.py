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

import arcade #Setup and White Background
arcade.open_window(494,260, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for y in range(10,251,40): #Red Stripes
    arcade.draw_rectangle_filled(247, y, 494,20, (191, 10, 48))

arcade.draw_rectangle_filled(99, 190, 198, 140, (0, 40, 104)) #Top Left Blue Box

TextHeight=  #White Stars
for StarRows in range(9):
    if StarRows%2==0:
        arcade.draw_text("*  *  *  *  *  *", 15, TextHeight, arcade.color.RADICAL_RED)

arcade.finish_render() #More Arcade Setup
arcade.run()

