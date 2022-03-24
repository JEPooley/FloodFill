from FloodFill.drawing import Drawing
from FloodFill.colours import Colours


drawing = Drawing.from_png(r"images\test.png")
drawing.show()

drawing.fill(123, 147, Colours.BLUE)
drawing.show()

drawing.fill(0, 0, Colours.GREEN)
drawing.show()