import arcade

arcade.open_window(600,600, "Star Wars Art")
arcade.set_background_color(arcade.color.STAR_COMMAND_BLUE)
arcade.start_render()
arcade.draw_rectangle_filled(300, 300, 100, 100, arcade.color.BLUSH)
arcade.draw_point(300, 300, arcade.color.BLUE_SAPPHIRE, 10)
arcade.draw_line(300, 400, 300, 200, arcade.color.BLACK, 2)
arcade.draw_circle_outline(300, 300, 200, arcade.color.WISTERIA, 3)
arcade.draw_circle_filled(300, 300, 3, arcade.color.WISTERIA)
arcade.draw_ellipse_filled(300, 100, 30, 15, arcade.color.AMBER)
point_list = ((0, 300),
              (300, 600),
              (600, 300),
              (300, 0))
arcade.draw_polygon_outline(point_list, arcade.color.SPANISH_VIOLET, 3)
point_list = ((300, 600),
              (310, 550),
              (290, 550))
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)
arcade.draw_text("never YEET never", 10, 10, arcade.color.YELLOW, 20)
arcade.finish_render()
arcade.run()