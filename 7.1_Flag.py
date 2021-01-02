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
arcade.open_window(494,260,"The Stars and Stripes")
arcade.set_background_color((255,255,255))
arcade.start_render()
#stripes
for stripe in range(7):
    arcade.draw_rectangle_filled(247, 10+(20*(stripe*2)), 494, 20, (191,10,48))

arcade.draw_rectangle_filled(90, 200, 197.6, 140, (0,40,104))

#stars
for star in range(0, 5, 1):
    for star2 in range(0, 6, 1):
        arcade.draw_text("*", 7.38+(16.38*star2*2), 230-(14.03*star*2), arcade.color.WHITE, 20)
for star in range(0, 4, 1):
    for star2 in range(0, 5, 1):
        arcade.draw_text("*", 27.76+(16.38*star2*2), 211.92-(14.03*star*2), arcade.color.WHITE, 20)

arcade.finish_render()
arcade.run()