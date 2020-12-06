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
arcade.set_background_color((191, 10, 48))
arcade.start_render()
for stripey in range(30,280,40):
    arcade.draw_rectangle_filled(247,stripey,494,20,arcade.color.WHITE)
arcade.draw_rectangle_filled(99,190,198,140,(0,40,104))
for yone in range(115,265,28):
    for starone in range(11,199,33):
        arcade.draw_text("*",starone,yone,arcade.color.WHITE,20)
for ytwo in range(130,265,28):
    for startwo in range(27,166,33):
        arcade.draw_text("*",startwo,ytwo,arcade.color.WHITE,20)
arcade.finish_render()
arcade.run()