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
arcade.open_window(494,260,"flag")
arcade.set_background_color((255, 255, 255))
redy =0
stary=0
arcade.start_render()
for i in range(7):                                                               #red lines
    arcade.draw_lrtb_rectangle_filled(0, 494, 20+redy, 0+redy, (200,0,0))
    redy+= 40
arcade.draw_lrtb_rectangle_filled(0, 197.6, 260, 120, (0,0,128))                #blue rectangle
for i in range(1,10):                                                           #stars
    if i%2==0:
        arcade.draw_text("*   *   *   *   *", 24.752, 233.952-stary, (255,255,255) , 20.246)
    else:
        arcade.draw_text("*   *   *   *   *   *", 8.822, 233.952 - stary, (255, 255, 255), 20.246)
    stary+=14.04
arcade.finish_render()
arcade.run()