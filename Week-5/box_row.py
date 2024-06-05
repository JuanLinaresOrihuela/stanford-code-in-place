from graphics import Canvas # type: ignore

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for row in range(N_BOXES):
        for col in range(N_BOXES):
            left_x = col * BOX_SIZE
            top_y = row * BOX_SIZE
            right_x = left_x + BOX_SIZE
            bottom_y = top_y + BOX_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "white", "black")

    canvas.mainloop()
    
if __name__ == '__main__':
    main()
