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
import arcade;starsx=8.19;starsy=14.04;stars=0;row=6
arcade.open_window(494,260,"The Stars and Stripes");arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for y_offset in range(0,494,40):
    arcade.draw_rectangle_filled(247,10+y_offset,494,20,(191,10,48))
arcade.draw_rectangle_filled(98.8,190,197.6,140,(00,20,68))
for x_offset in range(9):
    if stars%2==1:
        starsx=24.57;row-=2
    for b in range(row):
        arcade.draw_text("*", starsx, starsy+105.95, arcade.color.WHITE,20);starsx+=32.76
    starsy+=14.04;starsx=8.19;stars+=1;row+=1
arcade.finish_render();arcade.run()
