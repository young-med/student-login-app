import tkinter as tk
from tkinter import messagebox

class Hospital_loginApp:
    def __init__(self, root):

        self.root = root

        self.root.title("HOSPITAL LOGIN")
        self.root.geometry("320x450")
        self.root.configure(bg="blue")
        self.root.resizable(False, False)

        # mainframe
        self.main_frame = tk.Frame(
            root,
            bg="white",
            bd=0,
            relief="solid"
        )

        self.main_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=350,
            height=580
        )

        # title
        self.title_label = tk.Label(
            self.main_frame,
            text="Hospital Portal",
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#1f2937"
        )

        self.title_label.pack(pady=(35, 10))

        # subtitle
        self.subtitle = tk.Label(
            self.main_frame,
            text="Login to continue",
            font=("Segoe UI", 10),
            bg="white",
            fg="#6b7280"
        )

        self.subtitle.pack(pady=(0, 25))

        # username
        self.user_label = tk.Label(
            self.main_frame,
            text="Username",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#374151"
        )

        self.user_label.pack(anchor="w", padx=30)

        # username entry
        self.username_entry = tk.Entry(
            self.main_frame,
            font=("Arial", 11),
            bd=1,
            relief="solid"
        )

        self.username_entry.pack(
            padx=30,
            pady=(5, 20),
            fill="x",
            ipady=8
        )

        # Password Label
        self.pass_label = tk.Label(
            self.main_frame,
            text="Password",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#443751"
        )

        self.pass_label.pack(anchor="w", padx=30)

        # Password Entry
        self.password_entry = tk.Entry(
            self.main_frame,
            font=("Arial", 11),
            bd=1,
            relief="solid",
            show="*"
        )

        self.password_entry.pack(
            padx=30,
            pady=(5, 25),
            fill="x",
            ipady=8
        )

        # Login Button
        self.login_button = tk.Button(
            self.main_frame,
            text="LOGIN",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=self.login
        )

        self.login_button.pack(
            padx=30,
            fill="x",
            ipady=10
        )

        # Footer
        self.footer = tk.Label(
            self.main_frame,
            text="© Hospital Login Page",
            font=("Arial", 8),
            bg="white",
            fg="#9ca3af"
        )

        self.footer.pack(side="bottom", pady=20)

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username !="" and password !="":
            messagebox.showinfo(
                "Success",
                "Login Successful"
            )
        else:
            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = Hospital_loginApp(root)
    root.mainloop()