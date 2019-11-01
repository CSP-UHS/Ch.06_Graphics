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
y= 0
arcade.open_window(494,260, "The Stars and Stripes")

arcade.set_background_color(arcade.color.WHITE) #set backround color

arcade.start_render()
#Draw in here
for i in range(25):
    arcade.draw_rectangle_filled(y, 0, 10, 20, arcade.color.RED)
    y+=20
#draw in here
arcade.finish_render()

arcade.run()
