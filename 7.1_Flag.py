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
redline_y = 250
star_y = 230
star_x = 15.38
arcade.open_window(494,260,"The Stars and Stripes")
arcade.set_background_color((255,255,255))
arcade.start_render()
for i in range(7):
    arcade.draw_rectangle_filled(247, redline_y, 494, 20, (191,10,48))
    redline_y -= 40
arcade.draw_rectangle_filled(98.8,190,197.6,140,(0,40,104))
for i in range(5):
    for i in range(6):
        arcade.draw_text("*", star_x, star_y, arcade.color.WHITE, 20)
        star_x += 30.76
    star_y -= 28.08
    star_x = 15.38
star_y = 215.96
star_x = 30.76
for i in range(4):
    for i in range(5):
        arcade.draw_text("*", star_x, star_y, arcade.color.WHITE, 20)
        star_x += 30.76
    star_x = 30.76
    star_y -= 28.08
arcade.finish_render()
arcade.run()