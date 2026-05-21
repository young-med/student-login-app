# student_login.py
# Clean student login UI using Tkinter

import tkinter as tk
from tkinter import messagebox


# -----------------------------
# Dummy student credentials
# -----------------------------
STUDENT_DATA = {
    "student01": "pass123",
    "student02": "welcome",
    "admin": "admin123"
}


class StudentLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SRC STUDENT PORTAL")
        self.root.geometry("420x500")
        self.root.configure(bg="#f4f6f8")
        self.root.resizable(False, False)

        # Main Frame
        self.main_frame = tk.Frame(
            root,
            bg="white",
            bd=0,
            relief="flat"
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center",
                              width=340, height=380)

        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="Student Portal",
            font=("Segoe UI", 22, "bold"),
            bg="white",
            fg="#1f2937"
        )
        self.title_label.pack(pady=(35, 10))

        # Subtitle
        self.subtitle = tk.Label(
            self.main_frame,
            text="Login to continue",
            font=("Segoe UI", 10),
            bg="white",
            fg="#6b7280"
        )
        self.subtitle.pack(pady=(0, 25))

        # Username Label
        self.user_label = tk.Label(
            self.main_frame,
            text="Username",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#374151"
        )
        self.user_label.pack(anchor="w", padx=30)

        # Username Entry
        self.username_entry = tk.Entry(
            self.main_frame,
            font=("Segoe UI", 11),
            bd=1,
            relief="solid"
        )
        self.username_entry.pack(padx=30, pady=(5, 20), fill="x", ipady=8)

        # Password Label
        self.pass_label = tk.Label(
            self.main_frame,
            text="Password",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#374151"
        )
        self.pass_label.pack(anchor="w", padx=30)

        # Password Entry
        self.password_entry = tk.Entry(
            self.main_frame,
            font=("Segoe UI", 11),
            bd=1,
            relief="solid",
            show="*"
        )
        self.password_entry.pack(padx=30, pady=(5, 25), fill="x", ipady=8)

        # Login Button
        self.login_button = tk.Button(
            self.main_frame,
            text="LOGIN",
            font=("Segoe UI", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=self.login
        )
        self.login_button.pack(padx=30, fill="x", ipady=10)

        # Footer
        self.footer = tk.Label(
            self.main_frame,
            text="© Student Management System",
            font=("Segoe UI", 8),
            bg="white",
            fg="#9ca3af"
        )
        self.footer.pack(side="bottom", pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in STUDENT_DATA and STUDENT_DATA[username] == password:
            messagebox.showinfo(
                "Login Successful",
                f"Welcome, {username}!"
            )
        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentLoginApp(root)
    root.mainloop()