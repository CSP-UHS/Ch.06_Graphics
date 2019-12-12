'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 191,10,48 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
import arcade
arcade.open_window(494,260,"the stars and stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for y in range(10,251,40):
    arcade.draw_rectangle_filled(247,y,494,20,(191,10,48))
arcade.draw_rectangle_filled(99,190,198,140,(0,40,104))

#variables
y=235


for star in range(9):
    if star % 2 == 0:

        arcade.draw_text("*   *   *   *   *   *",15,y, arcade.color.WHITE,20)
    else:
        arcade.draw_text("*   *   *   *   *",30,y, arcade.color.WHITE,20)
    y-=15

arcade.finish_render()
arcade.run()

