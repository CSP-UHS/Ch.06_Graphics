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
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for loo in range(0, 260, 40):
    arcade.draw_line(0, 9+loo, 494, 9+loo, (191, 10, 48), 20)
arcade.draw_rectangle_filled(99, 189, 198, 140, (0, 40, 104))
for star in range(0, 155, 25):
    arcade.draw_text("*", 10, 119+star, (255, 255, 255), 20)
for side in range(0, 90, 24):
    arcade.draw_text("*", 27, 133 + side, (255, 255, 255), 20)
for star in range(0, 155, 25):
    arcade.draw_text("*", 44, 119 + star, (255, 255, 255), 20)
for side in range(0, 90, 24):
    arcade.draw_text("*", 62, 133.4 + side, (255, 255, 255), 20)
for star in range(0, 155, 25):
    arcade.draw_text("*", 78, 119 + star, (255, 255, 255), 20)
for side in range(0, 90, 24):
    arcade.draw_text("*", 95, 133.4 + side, (255, 255, 255), 20)
for star in range(0, 155, 25):
    arcade.draw_text("*", 113, 119 + star, (255, 255, 255), 20)
for side in range(0, 90, 24):
    arcade.draw_text("*", 129, 133.4 + side, (255, 255, 255), 20)
for star in range(0, 155, 25):
    arcade.draw_text("*", 146, 119 + star, (255, 255, 255), 20)
for side in range(0, 90, 24):
    arcade.draw_text("*", 163, 133.4 + side, (255, 255, 255), 20)
for star in range(0, 155, 25):
    arcade.draw_text("*", 180, 119 + star, (255, 255, 255), 20)
arcade.finish_render()
arcade.run()
