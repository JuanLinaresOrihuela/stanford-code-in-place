from graphics import Canvas # type: ignore

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    canvas.create_rectangle(
		CENTER_X - THIS_BIG / 2,  # Put half of the square to the left of CENTER_X
		CENTER_Y - THIS_BIG / 2,  # Put half of the square above CENTER_Y
		CENTER_X + THIS_BIG / 2,  # Put half of the square to the right of CENTER_X
		CENTER_Y + THIS_BIG / 2   # Put half of the square below CENTER_Y
	)

if __name__ == '__main__':
    main()