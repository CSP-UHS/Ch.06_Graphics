'''
PICASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times.
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program.
If you have 5 lines that draw a robot, group them together with blank lines above and below.
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
import math
arcade.open_window(500,250,"")
arcade.set_background_color((255, 255, 255))
arcade.start_render()
wheelx=0
arcx=0
for i in range(2):                                                       #leaf springs
    if i == 1:
       arcx+=250
    arcade.draw_arc_outline(115+arcx,75,55,20,(0, 0, 0), 180, 360, 3, 0)
arcade.draw_line(190, 110, 212, 140, (0,0,0), 5)                            #stering colum
arcade.draw_line(212, 140, 223, 155, (0,0,0), 3)                                #small stering part
arcade.draw_circle_filled(223, 155, 3, (0,0,0))                         #circle on steeing wheel
arcade.draw_line(208, 166, 238, 144, (0,0,0), 3)                        #steering wheel
arcade.draw_lrtb_rectangle_filled(55, 430, 90, 70, (105,125,55))        #frame
arcade.draw_lrtb_rectangle_filled(85, 200, 150, 90, (105,125,55))      #hood
arcade.draw_lrtb_rectangle_filled(100, 125, 155, 150, (105,125,55))     #thingy on hood
arcade.draw_lrtb_rectangle_filled(80, 85, 145, 120, (150,150,150))     #head light
arcade.draw_lrtb_rectangle_filled(200, 300, 100, 90, (105,125,55))      #door
arcade.draw_lrtb_rectangle_filled(300, 420, 150, 90, (105,125,55))      #trunk
arcade.draw_line(180, 70, 180, 62, (70,70,70), 5)               #exuast
arcade.draw_circle_filled(180, 62, 2.5, (70,70,70))             #exuast bend
arcade.draw_line(180, 62, 280, 62, (70,70,70), 5)               #exuast pipe
arcade.draw_line(230, 62, 260, 62, (70,70,70), 10)              #cat
arcade.draw_circle_filled(280, 62, 2.5, (0,0,0))                #final exuast hole
arcade.draw_line(225, 70, 225, 64.5, (0,0,0), 3)                #exaut atchments
arcade.draw_line(265, 70, 265, 64.5, (0,0,0), 3)                #exaut atchments
arcade.draw_circle_filled(400, 115, 10, (180,180,180))              #gas cap
arcade.draw_circle_filled(400, 115, 9, (80,80,80))
arcade.draw_lrtb_rectangle_filled(394, 406, 117, 113, (180,180,180))
point_list = ((265, 100),                                               #door angle
              (300, 100),
              (300, 150))
arcade.draw_polygon_filled(point_list, (105,125,55))
point_list = ((194, 150),                                               #windsheild
              (200, 150),
              (210, 200),
              (204, 201))
arcade.draw_polygon_filled(point_list, (0,0,0))
point_list = ((420, 105),                                               #spare
              (430, 100),
              (440, 100),
              (450, 105),
              (450, 180),
              (440, 185),
              (430, 185),
              (420, 180))
arcade.draw_polygon_filled(point_list, (0,0,0))
point_list = ((305, 150),                                               #seat
              (320, 150),
              (324, 168),
              (321, 170),
              (310, 170))
arcade.draw_polygon_filled(point_list, (0,0,0))
for i in range(2):                                                       #wheels
    if i == 1:
       wheelx=250
    arcade.draw_circle_filled(115+wheelx, 60, 45, (0, 0, 0))
radious = 15                                                         #lug nuts
centerx= 115
centery= 60
on_draw= float((6*(math.pi))/5)
for i in range(2):
    for i in range(5):
        xpoint = radious * math.sin(on_draw) + centerx
        ypoint = radious * math.cos(on_draw) + centery
        arcade.draw_circle_filled(xpoint, ypoint, 3, (150, 150, 150))
        on_draw+= float((6*(math.pi))/5)
    centerx+=250
                        #knobs on tires
centerx = 115
knobradious = 45
knoboutsideradious = 47
on_draw = float(((math.pi)) / 5)
on_draw2 = float(((math.pi)) / 5)
for i in range(2):
    for i in range(10):
        knobxpoint = knobradious * math.sin(on_draw)-2 + centerx
        print(knobxpoint)
        knobypoint = knobradious * math.cos(on_draw) + centery
        print(knobypoint)
        knobxpoint2 = knobradious * math.sin(on_draw2)+2 + centerx
        print(knobxpoint2)
        knobypoint2 = knobradious * math.cos(on_draw) + centery
        print(knobypoint2)
        knobxpoint3 = knoboutsideradious * math.sin(on_draw2)+2 + centerx
        print(knobxpoint3)
        knobypoint3 = knoboutsideradious * math.cos(on_draw) + centery
        print(knobypoint3)
        knobxpoint4 = knoboutsideradious * math.sin(on_draw)-2 + centerx
        print(knobxpoint4)
        knobypoint4 = knoboutsideradious * math.cos(on_draw) + centery
        print(knobypoint4)
        #arcade.draw_circle_filled(xpoint, ypoint, 3, (150, 150, 150))
        point_list = ((knobxpoint, knobypoint),
                      (knobxpoint2, knobypoint2),
                      (knobxpoint3, knobypoint3),
                      (knobxpoint4, knobypoint4))

        arcade.draw_polygon_filled(point_list, (0, 0, 0))
        on_draw += float(((math.pi)) / 5)
    centerx += 250

arcade.finish_render()
arcade.run()