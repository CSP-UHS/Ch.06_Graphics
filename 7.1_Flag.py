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
arcade.open_window(494, 260, "The Stars and Stripes")
arcade.set_background_color((255,255,255))
arcade.start_render()
for y_offset in range(10, 500, 40):
    arcade.draw_rectangle_filled(0, 0 + y_offset, 20, 988, (255, 0, 0), 90)  # Red stripes
arcade.draw_lrtb_rectangle_filled(0, 218, 260, 120, (00, 85, 155))  # Blue rectangle
for stars in range(0, 140, 31):
    arcade.draw_text("*  *  *  *  *  *", 10, 231 - stars, (255, 255, 255), 28)  # Stars
    arcade.draw_text("*  *  *  *  *", 27, 216 - stars, (255, 255, 255), 28)
arcade.finish_render()
arcade.run()
