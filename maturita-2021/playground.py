class Playground:
    array = [[]]
    rectangles = []
    canvas = None
    size_x, size_x_px, size_y, size_y_px = 10, 10, 10, 10
    tile_size_x, tile_size_y = 10, 10

    def Reset(self):
        self.array = [
            ["empty" for x in range(self.size_x)] for y in range(self.size_y)]

    def Refresh(self):
        self.size_x_px = self.canvas.winfo_reqwidth()
        self.size_y_px = self.canvas.winfo_reqheight()
        self.tile_size_x = self.size_x_px/len(self.array)
        self.tile_size_y = self.size_y_px/len(self.array[0])

        for rectangle in self.rectangles:
            self.canvas.delete(rectangle)

        self.rectangles = []

        for x in range(len(self.array)):
            for y in range(len(self.array[x])):
                self.rectangles.append(self.canvas.create_rectangle(
                    x*40,
                    y*40,
                    x*40+40,
                    y*40+40,
                    fill="orange" if self.array[x][y] == "filled" else "gray"))

    def Fill(self, x, y):
        # fill rectangle on coordinates
        self.array[x][y] = "filled"
        self.Refresh()

    def Erase(self, x, y):
        # erase rectangle on coordinates
        self.array[x][y] = "empty"
        self.Refresh()

    # print rectangles in canvas

    def __init__(self, canvas, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.canvas = canvas

        self.Reset()
        self.Refresh()
