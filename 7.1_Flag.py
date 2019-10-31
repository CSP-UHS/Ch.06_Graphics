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
arcade.open_window(524,260, "The Stars and Stripes")

arcade.set_background_color(arcade.color.WHITE) #set backround color

arcade.start_render()
#Draw in here
for x_offset in range(0,610,20):
    arcade.draw_rectangle_filled(0+x_offset,60,10,30,arcade.color.BF0A30)
#draw in here
arcade.finish_render()

arcade.run()
