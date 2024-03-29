"""
try_drawing.py: Example using the Drawing class to flood fill an image
"""
from FloodFill.colours import Colours
from FloodFill.drawing import Drawing


drawing = Drawing.from_png(r"images\test.png")
drawing.show()

drawing.fill(123, 147, Colours.BLUE)
drawing.show()

drawing.fill(0, 0, Colours.GREEN)
drawing.show()
