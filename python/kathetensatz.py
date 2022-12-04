from manim import *
import numpy as np

# PARAMETERS
r = 2
angle = np.pi*2/5
rt = 3

# colours
colour_tri = "#5be800"
colour_quad = "#0777ba"

common_kwargs = {"fill_opacity": 0.5}

class Kathetensatz(Scene):
    def construct(self):
        # Parameters
        pa = np.array([-r, 0, 0])
        pb = np.array([r, 0, 0])
        pc = np.array([r*np.cos(angle), r*np.sin(angle), 0])
        a = np.sqrt((pc[0]-pb[0])**2 + pc[1]**2)
        triangle = Polygon(pa, pb, pc, color=colour_tri, **common_kwargs)
        self.add(triangle)

        t_tracker = ValueTracker(0)
        p1 = pb
        p2 = pb + a*np.array([np.cos(angle/2), np.sin(angle/2), 0])
        p3_0 = p2 + pc - pb
        p4_0 = pc
        square = Polygon(p1, p2, p3_0, p4_0, color=colour_quad, **common_kwargs)
        self.add(square)

        # a^2
        text_a2 = MathTex("a^2").shift(square.get_center())
        self.add(text_a2)
        text_eq = MathTex("a^2", "=", "pc").shift(1.5*r*UP)
        # animation updater
        self.play(text_a2.animate.move_to(text_eq.get_part_by_tex("a^2").get_center()))
        square.add_updater(
            lambda x: x.become(Polygon(p1, p2, p3_0 + (pa - pc)*t_tracker.get_value(), p4_0 + (pa - pc)*t_tracker.get_value(), color=colour_quad, **common_kwargs))
        )
        self.play(t_tracker.animate.increment_value(1), run_time=rt)

        angle_tracker = ValueTracker(0)
        p4 = pa
        p3 = p4 + p2-p1
        p3d = p3 - p1
        square.add_updater(
            lambda x: x.become(Polygon(pb, pb + a*np.array([np.cos(angle/2 + angle_tracker.get_value()), np.sin(angle/2 + angle_tracker.get_value()), 0]),
                                p1 + np.array([p3d[0]*np.cos(angle_tracker.get_value())-p3d[1]*np.sin(angle_tracker.get_value()),
                                 p3d[0]*np.sin(angle_tracker.get_value())+p3d[1]*np.cos(angle_tracker.get_value()),0]),
                                pb + 2*r*np.array([-np.cos(angle_tracker.get_value()), -np.sin(angle_tracker.get_value()), 0]),
                                color=colour_quad, **common_kwargs))
        )
        self.play(angle_tracker.animate.increment_value(np.pi/2), run_time=rt)
        

        p2 = pc
        p3 = pc + np.array([0, -2*r, 0])
        p4 = p1 + np.array([0, -2*r, 0])

        s_tracker = ValueTracker(0)
        square.add_updater(
            lambda x: x.become(Polygon(p1, p2*np.array([1, 1-s_tracker.get_value(), 1]), p2*np.array([1, 1-s_tracker.get_value(), 1])-np.array([0, 2*r, 0]), p4,
                                color=colour_quad, **common_kwargs))
        )
        self.play(s_tracker.animate.increment_value(1), run_time=rt)
        text_pc = MathTex("pc").shift(square.get_center())
        self.play(FadeIn(text_pc), FadeIn(text_eq))