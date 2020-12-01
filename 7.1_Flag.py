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
arcade.start_render()
for i in range(7):
    arcade.draw_rectangle_filled(247, 10+(20*(i*2)), 494, 20, (191, 13, 62))    # I got these colors off the internet
    arcade.draw_rectangle_filled(247, 30+(20*(i*2)), 494, 20, (255, 255, 255))  # they are not the same ones provided
arcade.draw_rectangle_filled(98.8, 190, 197.6, 140, (10, 49, 97))               # I could convert them if I had to
for i in range(0, 5, 1):                                                        # but I don't want to
    for l in range(0, 6, 1):
        arcade.draw_text("*", 11.38+(16.38*l*2), 225.96-(14.03*i*2), arcade.color.WHITE, 20)
for i in range(0, 4, 1):
    for l in range(0, 5, 1):
        arcade.draw_text("*", 27.76+(16.38*l*2), 211.92-(14.03*i*2), arcade.color.WHITE, 20)
arcade.finish_render()
arcade.run()