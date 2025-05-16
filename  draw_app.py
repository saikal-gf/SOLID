import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Рисовалка")
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack()
        self.last_x, self.last_y = None, None

        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.clear_btn = tk.Button(root, text="Очистить", command=self.clear_canvas)
        self.clear_btn.pack(pady=5)

    def click(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=2)
        self.last_x, self.last_y = x, y

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
