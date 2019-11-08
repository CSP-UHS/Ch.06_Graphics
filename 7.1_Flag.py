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
y = 10
x = 10
z = 10
w = 10
n = 10
l = 10
p = 25
m = 10

arcade.open_window(494,260, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range(7):
    arcade.draw_rectangle_filled(300, y, 600, 19.994, arcade.color.RED)
    y+=39.988
arcade.draw_rectangle_filled(99, 200, 197.6, 160, arcade.color.BLUE)
##############################
3#############################
# for i in range(4):
#     for i in range(6):
#         arcade.draw_text("*", x,230, arcade.color.WHITE,20)
#         x+=32
#     for i in range(5):
#         arcade.draw_text("*", p,220, arcade.color.WHITE,20)
#         p+=32.5


# for i in range(6):
#     arcade.draw_text("*", z,205, arcade.color.WHITE,20)
#     z+=32
#
# for i in range(6):
#     arcade.draw_text("*", w,180, arcade.color.WHITE,20)
#     w+=32
#
# for i in range(6):
#     arcade.draw_text("*", n,140, arcade.color.WHITE,20)
#     n+=32
#
# for i in range(6):
#     arcade.draw_text("*",l,125, arcade.color.WHITE,20)
#     l+=32

arcade.finish_render()
arcade.run()