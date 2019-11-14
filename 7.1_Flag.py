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
y = 19.994
z = 11
l = 25
n = 11
m = 25
w = 11
b = 25
c = 11
arcade.open_window(494,260, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range(7):
    arcade.draw_lrtb_rectangle_filled(0, 600, y, y-19.994, arcade.color.RED)
    y+=39.988
arcade.draw_lrtb_rectangle_filled(0, 197.6, 260, 120, arcade.color.BLUE)


for i in range(6):
    arcade.draw_text("*", z, 230, arcade.color.WHITE,20)
    z+=32

for i in range(5):
    arcade.draw_text("*", l, 215, arcade.color.WHITE,20)
    l+=32
###################################
###################################  after first 2
# for i in range(6):
#     arcade.draw_text("*", n, 200, arcade.color.WHITE,20)
#     n+=32
#
# for i in range(5):
#     arcade.draw_text("*", m, 185, arcade.color.WHITE,20)
#     m+=32
#
# for i in range(6):
#     arcade.draw_text("*", w, 170, arcade.color.WHITE,20)
#     w+=32
#
# for i in range(5):
#     arcade.draw_text("*", b, 155, arcade.color.WHITE,20)
#     b+=32
#
# for i in range(6):
#     arcade.draw_text("*", c, 140, arcade.color.WHITE,20)
#     c+=32



arcade.finish_render()
arcade.run()

E = 14.04
F = 14.04
H = 16.38