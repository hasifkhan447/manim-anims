#!/usr/bin/env python3
from manim import *

class TLabelExample(Scene):
    def construct(self):
        # defines the axes and linear function
        axes = Axes(x_range=[0, 10], y_range=[0, 1], x_length=10, y_length=7)
        func = axes.plot(lambda x: 20 if (x==0) else 1/x, color=YELLOW)
        # creates the T_label


        rects = axes.get_riemann_rectangles(
            func,
            x_range=[1,9],
            dx=1,
            color=(RED_B),
            input_sample_type="left"
        )

        rects_small = axes.get_riemann_rectangles(
            func,
            x_range=[1,9],
            dx=1,
            color=(RED_B),
            input_sample_type="right"
        )

        area = axes.get_area(
            func,
            x_range=(1,9),
            color=(RED_B),
            opacity=0.5
        )

        harmonics = MathTex(r"f(n) = \frac{1}{n}").to_edge(UR).shift([-1, 0, 0])
        outline = MathTex(r"f(x) = \frac{1}{x}").to_edge(UR).shift([-1,-1.5,0])

        harmonics_sum = MathTex(r"\sum_{n=1}^{N} \frac{1}{n}").to_edge(UR).shift([-1,0,0])
        outline_acc = MathTex(r"\int_{1}^N \frac{1}{x} dx").to_edge(UR).shift([-1, -1.5, 0])

        halfway_point = MathTex(r"\sum_{n=1}^N \frac{1}{n} \leq \int_{1}^N \frac{1}{x} dx  ").to_edge(UR)

        self.add(axes)

        self.play(FadeIn(harmonics))
        self.wait(0.5)
        self.play(ShowIncreasingSubsets(rects)) #Add text for harmonic series


        self.play(FadeIn(outline))
        self.wait(0.5)
        self.play(Create(func)) #Add text for 1/x

        self.play(FadeOut(rects))
        self.play(Create(area))
        self.wait(0.5)
        self.play(TransformMatchingTex(outline, outline_acc))

        self.play(FadeOut(area))
        self.play(FadeIn(rects))
        self.wait(0.5)
        self.play(TransformMatchingTex(harmonics, harmonics_sum))
        self.play(FadeOut(outline_acc))
        self.wait(0.5)
        self.play(TransformMatchingTex(harmonics_sum, halfway_point))
        self.wait(0.6)

        # Shift rectangles back


        # Add text for integral from 1 to N-1

        # Limits as n goes to infinity
