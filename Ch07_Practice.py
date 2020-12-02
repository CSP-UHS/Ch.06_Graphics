import arcade
arcade.openwindow(600, 600,"Jedi Drawing")
arcade.set_background_color((255,0,0))
arcade.start_render()

#Drawing Commands
for xoffset in range(20,620,30):
    arcade.draw_rectangle_filled(0+xoffset,20,10,30(255,255,255))
arcade.draw_rectangle_filled(300,25,600,3(255,255,255))
arcade.draw_rectangle_filled(300,13,600,3(255,255,255))

point_list=((300,300),(400,200),(200,200))
arcade.draw_polygon_outline(pont_list,(255,255,0),3)

arcade.draw_text("Hello World",100,500,arcade.color.PINK,10,400,"center")

sith=arcade.load_texture("python.png")
arcade.draw_texture_rectangle(300,300,sith.width,sith.height,sith)


arcade.finish_render()
arcade.run()