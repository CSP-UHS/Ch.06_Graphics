import arcade
arcade.open_window(425,585, "Eddie Agic")
arcade.set_background_color((200,200,200))
arcade.start_render()
arcade.draw_rectangle_filled(107.5,55,205,100,arcade.color.WHITE)
arcade.draw_rectangle_filled(265,55,100,100,arcade.color.WHITE)
for x_offset in range(55,266,105):
    arcade.draw_rectangle_filled(x_offset,160,100,100,arcade.color.WHITE)
for x_offset in range(55, 371, 105):
    arcade.draw_rectangle_filled(x_offset,265,100,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x_offset,370,100,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x_offset,475,100,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x_offset,555,100,50,arcade.color.WHITE)
arcade.draw_rectangle_filled(370,107.5,100,205,arcade.color.WHITE)

arcade.draw_text("F16",75,535,arcade.color.GRAY,10)
arcade.draw_text("F17",180,535,arcade.color.GRAY,10)
arcade.draw_text("F18",285,535,arcade.color.GRAY,10)
arcade.draw_text("F19",390,535,arcade.color.GRAY,10)
arcade.draw_text("clear",33.3,470,arcade.color.GRAY,15)
arcade.draw_text(".",259,45,arcade.color.GRAY,25)
arcade.draw_text("=",150,465,arcade.color.GRAY,20)
arcade.draw_text("/",260,465,arcade.color.GRAY,20)
arcade.draw_text("*",362.5,455,arcade.color.GRAY,25)
arcade.draw_text("7",45,360,arcade.color.GRAY,25)
arcade.draw_text("8",150,360,arcade.color.GRAY,25)
arcade.draw_text("9",255,360,arcade.color.GRAY,25)
arcade.draw_text("4",45,255,arcade.color.GRAY,25)
arcade.draw_text("5",150,255,arcade.color.GRAY,25)
arcade.draw_text("6",255,255,arcade.color.GRAY,25)
arcade.draw_text("1",45,150,arcade.color.GRAY,25)
arcade.draw_text("2",150,150,arcade.color.GRAY,25)
arcade.draw_text("3",255,150,arcade.color.GRAY,25)
arcade.draw_text("0",95,45,arcade.color.GRAY,25)
arcade.draw_text("-",362.5,360,arcade.color.GRAY,25)
arcade.draw_text("+",357.5,255,arcade.color.GRAY,25)
arcade.draw_text("enter",365,15,arcade.color.GRAY,15)
arcade.finish_render()
arcade.run()











