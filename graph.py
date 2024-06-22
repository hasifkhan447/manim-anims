#!/usr/bin/env python3
from manim import *

class TLabelExample(Scene):
    def construct(self):

        axes = Axes(x_range=[0, 10,1], y_range=[0, 1, 0.1], x_length=10, y_length=7,
                    axis_config={
                        "include_numbers":True,
                        "font_size" : 24,
                    })
        func = axes.plot(lambda x: 20 if (x==0) else 1/x, color=YELLOW)

        rects = axes.get_riemann_rectangles(
            func,
            x_range=[1,9],
            dx=1,
            fill_opacity=0.5,
            color=(RED_C,RED_B,RED_A),
            input_sample_type="left"
        )

        area = axes.get_area(
            func,
            x_range=(1,9),
            color=(GOLD_B),
            opacity=0.5
        )

        one = [-3, 0, 0]
        two = [0, -0.2, 0]

        harmonics = MathTex(r"f(n) = \frac{1}{n}").to_edge(UR).shift(one)
        outline = MathTex(r"f(x) = \frac{1}{x}").to_edge(UR).shift(two)

        harmonics_sum = MathTex(r"\sum_{n=1}^{N} \frac{1}{n}").to_edge(UR).shift(one)
        outline_acc = MathTex(r"\int_{1}^N \frac{1}{x} dx").to_edge(UR).shift(two)

        halfway_point = MathTex(r"\int_{1}^N \frac{1}{x} dx \leq \sum_{n=1}^N \frac{1}{n}").to_edge(UR).shift([-1, 0, 0])
        limit_point = MathTex(r"\lim_{N \to \infty} \int_{1}^N \frac{1}{x} dx \leq \lim_{N \to \infty}  \sum_{n=1}^N \frac{1}{n}").to_edge(UR)
        reduction_point = MathTex(r"\infty \leq \sum_{n=1}^\infty \frac{1}{n}").to_edge(UR)
        final_point = MathTex(r"\sum_{n=1}^\infty \frac{1}{n} = \infty").to_edge(UR).shift([-1,0,0])

        self.add(axes)

        #Bring in the harmonic series
        self.play(FadeIn(harmonics))
        self.wait(0.5)
        self.play(Write(rects)) #Add text for harmonic series
        self.play(TransformMatchingTex(harmonics, harmonics_sum))

        #Bring in the outline
        self.play(FadeIn(outline))
        self.wait(0.5)
        self.play(Write(func)) #Add text for 1/x

        #Remove harmonic series and display area
        self.play(FadeOut(rects))
        self.play(DrawBorderThenFill(area))
        self.wait(0.5)
        self.play(TransformMatchingTex(outline, outline_acc)) #Turn it into an integral

        self.wait(0.5)

        #Remove the sum, while transforming into an integral
        self.play(FadeOut(harmonics_sum))
        self.play(FadeIn(rects))
        self.play(rects.animate.fade(0.3))
        self.play(TransformMatchingTex(outline_acc, halfway_point))
        self.wait(0.6)
        self.play(TransformMatchingTex(halfway_point, limit_point))
        self.wait(0.6)
        self.play(TransformMatchingTex(limit_point, reduction_point))
        self.wait(0.6)
        self.play(TransformMatchingTex(reduction_point, final_point))
        self.wait(1)
