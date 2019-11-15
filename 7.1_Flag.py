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
A=260
B=A*1.9
y=0
arcade.open_window(B, A, "American Flag")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for y_offset in range(0,260,7):
    arcade.draw_lrtb_rectangle_filled(0, B, y+20, y,(191,10,48))
    y+=40
arcade.draw_lrtb_rectangle_filled(0, 197.6, 260, 120,(0,40,104))
for.....
arcade.draw_text("*",16.38,260-14.04,(255,255,255),12)

arcade.finish_render()
arcade.run()