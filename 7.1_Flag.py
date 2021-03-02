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
arcade.open_window(494,260, "The Stars and Stripes")
arcade.set_background_color((255,255,255))
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 210, 259, 120, (0, 40, 104))
arcade.draw_lrtb_rectangle_filled(211, 494, 260, 240, (191, 10, 48))
arcade.draw_lrtb_rectangle_filled(211, 494, 220, 200, (191, 10, 48))
arcade.draw_lrtb_rectangle_filled(211, 494, 180, 160, (191, 10, 48))
arcade.draw_lrtb_rectangle_filled(211, 494, 140, 120, (191, 10, 48))
arcade.draw_lrtb_rectangle_filled(0, 494, 100, 80, (191, 10, 48))
arcade.draw_lrtb_rectangle_filled(0, 494, 60, 40, (191, 10, 48))
arcade.draw_lrtb_rectangle_filled(0, 494, 20, 0, (191, 10, 48))
arcade.draw_text("*", 8, 230, arcade.color.WHITE, 20)
rownum=1
for y_offset in range(230, 100,-20):
    if rownum%2==0:
        arcade.draw_text("   *    *    *    *    *", 8, y_offset, arcade.color.WHITE, 20)
    else:
        arcade.draw_text("*    *    *    *    *    *", 8, y_offset, arcade.color.WHITE, 20)
    rownum+=1
arcade.finish_render()
arcade.run()
