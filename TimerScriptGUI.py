import tkinter as tk

class TimerApp:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.pause = True
        self.file_path = "insert_path_here\\Time.txt"
        self.timer_label = None
        self.timer_id = None

        self.window = tk.Tk()
        self.window.title("Timer")
        self.window.geometry("1000x750")

        self.timer_label = tk.Label(self.window, text="00:00:00", font=("Arial", 150))
        self.timer_label.pack()

        interface = tk.Frame(self.window)
        interface.pack(side=tk.BOTTOM)

        start_button = tk.Button(interface, font = ("Arial", 50), text="START", command=self.start_timer)
        start_button.pack(side=tk.LEFT, padx=50, pady=50)

        pause_button = tk.Button(interface, font = ("Arial", 50), text="PAUSE", command=self.pause_timer)
        pause_button.pack(side=tk.LEFT, padx=50, pady=50)

    def start_timer(self):
        self.pause = False
        self.update_timer()

    def pause_timer(self):
        self.pause = True

    def update_timer(self):
        if not self.pause:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1

            work_time = f"Hours: {self.hours}\nMinutes: {self.minutes}"

            try:
                with open(self.file_path, "w") as file:
                    file.write(work_time)
            except IOError as e:
                print(f"Error writing to file: {e}")

            self.timer_label.config(text=f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
            self.timer_id = self.window.after(1000, self.update_timer)

    def run(self):
        self.window.mainloop()

# Create and run the app
app = TimerApp()
app.run()