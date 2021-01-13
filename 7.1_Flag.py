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
y_off = 0
arcade.open_window(494,260,"The Stars and Stripes")
arcade.set_background_color((191, 10, 48))
arcade.start_render()

for y_off in range(0,220,40):
    arcade.draw_lrtb_rectangle_filled(0, 494, (240 - y_off), (220 - y_off), arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(0, 198, 260, 140, (0, 40, 104))
for i in range(0,6,1):
    arcade.draw_text("*", 16, 100, arcade.color.WHITE, 20)


arcade.finish_render()

arcade.run()