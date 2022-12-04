# run with --renderer=opengl
# - this uses a different rendering engine
# check for example:
# https://www.youtube.com/watch?v=KeXBLPC1tns&ab_channel=BenjaminHackl

from manim import *
from manim.opengl import *

class Test(Scene):
    def construct(self):
        text = Tex("Hello $\pi$")
        self.play(FadeIn(text))
        self.play(self.camera.animate.set_euler_angles(theta=-10*DEGREES))
        # this opens an ipython terminal
        # there you can try animations interactively.
        self.interactive_embed()