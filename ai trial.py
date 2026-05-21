import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from tkinter import ttk


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")
        self.root.geometry("900x700")

        # Default drawing settings
        self.pen_color = "black"
        self.pen_size = 5
        self.last_x = None
        self.last_y = None
        self.drawing = False
        self.erase_mode = False

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        # ================= TOOLBAR =================
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        # ---------- Color Buttons ----------
        colors = ["black", "red", "green", "blue", "yellow", "purple"]

        for color in colors:
            btn = tk.Button(
                toolbar,
                bg=color,
                width=2,
                command=lambda c=color: self.set_pen_color(c)
            )
            btn.pack(side=tk.LEFT, padx=2)

        # Custom Color Button
        tk.Button(
            toolbar,
            text="Custom Color",
            command=self.choose_custom_color
        ).pack(side=tk.LEFT, padx=5)

        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(
            side=tk.LEFT,
            fill=tk.Y,
            padx=5
        )

        # ---------- Brush Size ----------
        tk.Label(toolbar, text="Brush Size:").pack(side=tk.LEFT)

        self.size_var = tk.IntVar(value=5)

        size_spin = tk.Spinbox(
            toolbar,
            from_=1,
            to=50,
            textvariable=self.size_var,
            width=5,
            command=self.update_size
        )
        size_spin.pack(side=tk.LEFT, padx=2)

        # Medium button
        tk.Button(
            toolbar,
            text="Medium",
            command=lambda: self.set_pen_size(5)
        ).pack(side=tk.LEFT, padx=5)

        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(
            side=tk.LEFT,
            fill=tk.Y,
            padx=5
        )

        # ---------- Eraser ----------
        self.eraser_btn = tk.Button(
            toolbar,
            text="Erase",
            command=self.toggle_eraser
        )
        self.eraser_btn.pack(side=tk.LEFT, padx=2)

        # ---------- Clear Canvas ----------
        tk.Button(
            toolbar,
            text="Clear All",
            command=self.clear_canvas
        ).pack(side=tk.LEFT, padx=2)

        # ---------- Save Button ----------
        ttk.Button(
            toolbar,
            text="Save",
            command=self.save_drawing
        ).pack(side=tk.LEFT, padx=5)

        # ---------- Status Label ----------
        self.status = tk.Label(
            toolbar,
            text="Pen Color: Black | Pen Size: 5"
        )
        self.status.pack(side=tk.RIGHT, padx=5)

        # Setup canvas
        self.setup_canvas()

    def setup_canvas(self):
        self.canvas = tk.Canvas(
            self.root,
            bg="white",
            cursor="pencil"
        )

        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Mouse Events
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    # ================= DRAWING FUNCTIONS =================

    def set_pen_color(self, color):
        self.pen_color = color
        self.erase_mode = False

        self.eraser_btn.config(text="Erase")

        self.update_status()

    def choose_custom_color(self):
        color = colorchooser.askcolor(title="Choose Pen Color")

        if color[1]:
            self.set_pen_color(color[1])

    def set_pen_size(self, size):
        self.pen_size = size
        self.size_var.set(size)

        self.update_status()

    def update_size(self):
        self.pen_size = self.size_var.get()

        self.update_status()

    def toggle_eraser(self):
        self.erase_mode = not self.erase_mode

        if self.erase_mode:
            self.eraser_btn.config(text="Pen")
        else:
            self.eraser_btn.config(text="Erase")

        self.update_status()

    def update_status(self):
        mode = "Eraser" if self.erase_mode else "Pen"

        self.status.config(
            text=f"{mode} Color: {self.pen_color} | Pen Size: {self.pen_size}"
        )

    def start_draw(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if not self.drawing:
            return

        color = "white" if self.erase_mode else self.pen_color

        self.canvas.create_line(
            self.last_x,
            self.last_y,
            event.x,
            event.y,
            fill=color,
            width=self.pen_size,
            capstyle=tk.ROUND,
            smooth=True
        )

        self.last_x = event.x
        self.last_y = event.y

    def stop_draw(self, event):
        self.drawing = False

    def clear_canvas(self):
        self.canvas.delete("all")

    # ================= SAVE FUNCTION =================

    def save_drawing(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("All files", "*.*")
            ]
        )

        if file_path:
            try:
                # Save canvas as PostScript
                self.canvas.postscript(
                    file="temp.ps",
                    colormode="color"
                )

                # Convert to PNG using Pillow
                from PIL import Image

                img = Image.open("temp.ps")
                img.save(file_path, "png")

                messagebox.showinfo(
                    "Saved",
                    f"Drawing saved successfully:\n{file_path}"
                )

            except ImportError:
                messagebox.showerror(
                    "Error",
                    "Pillow library is required.\n\nInstall it using:\npip install pillow"
                )

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Failed to save image:\n{e}"
                )


# ================= MAIN PROGRAM =================

if __name__ == "__main__":
    root = tk.Tk()

    app = DrawingApp(root)

    root.mainloop()