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
y = 260
y1 = y
y2 = (y-(0.054*y)-20)
x = 1.9*y
arcade.open_window(494, y, "The Stars and Stripes")
arcade.start_render()
for i in range(7):
    arcade.draw_rectangle_filled(x/2, y1-10, x, 20, arcade.color.RED)
    arcade.draw_rectangle_filled(x/2, (y1-20)-10, x, 20, arcade.color.WHITE)
    y1 -= 40
arcade.draw_rectangle_filled(0+((0.76*y)/2), y-(((7*y)/13)/2), 0.76*y, (7*y)/13, arcade.color.BLUE)
for i in range(5):
    x2 = ((0.063*y)-10)
    for l in range(6):
        arcade.draw_text("*", x2, y2, arcade.color.WHITE, 20)
        arcade.draw_text("*", x2+(0.063*y), y2-(y-(0.054*y)), arcade.color.WHITE, 20)
        x2 += 2*(0.063*y)
    y2 -= 20
arcade.finish_render()
arcade.run()