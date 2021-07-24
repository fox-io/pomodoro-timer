"""
1. Decide on the task to be done.
2. Set the timer to 25 minutes.
3. Work on task until timer ends.
4. Take 5 minute break.
5. Repeat 1-4 4 times.
6. Take 15-30 minute break.
"""
import time
import tkinter


class PomodoroTimer:
    COLORS = {
        "RED": "D83A56",
        "PINK": "FF616D",
        "YELLOW": "FFEAC9",
        "GREEN": "66DE93"
    }
    CHECKMARK = "✔"

    def __init__(self):
        # Create window
        self.window = tkinter.Tk()
        self.window.title("Pomodoro Timer")
        self.window.config(
            padx=100,
            pady=50,
            bg=f"#{self.COLORS['YELLOW']}"
        )

        # Create Tomato image with timer text.
        self.canvas = tkinter.Canvas(
            width=200,
            height=224,
            bg=f"#{self.COLORS['YELLOW']}",
            highlightthickness=0
        )
        self.tomato_image = tkinter.PhotoImage(file="./tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_image)
        self.canvas.create_text(
            103,
            130,
            text="00:00",
            fill="white",
            font=("Courier", 28, "bold")
        )
        self.canvas.grid(row=1, column=1)

        # Create stage text
        self.stage_text = tkinter.Label(
            text="Timer",
            fg=f"#{self.COLORS['GREEN']}",
            bg=f"#{self.COLORS['YELLOW']}",
            font=("Courier", 34, "bold")
        )
        self.stage_text.grid(row=0, column=1)

        # Create start button
        self.start_button = tkinter.Button(
            text="Start",
            fg=f"#{self.COLORS['RED']}",
        )
        self.start_button.grid(row=2, column=0)

        # Create reset button
        self.reset_button = tkinter.Button(
            text="Reset",
            fg=f"#{self.COLORS['RED']}",
        )
        self.reset_button.grid(row=2, column=2)

        # Create rep checkmarks
        self.checkmark_text = tkinter.Label(
            text=f"{self.CHECKMARK}",
            fg=f"#{self.COLORS['GREEN']}",
            bg=f"#{self.COLORS['YELLOW']}",
            font=("Courier", 24, "bold")
        )
        self.checkmark_text.grid(row=3, column=1)


# def start_timer(minutes, label):
#     seconds = minutes * 60
#     while seconds > 0:
#         print(f"{label} for {minutes} minutes. {seconds}")
#         time.sleep(1)
#         seconds -= 1


def main():
    # Create app
    app = PomodoroTimer()

    # Run app
    app.window.mainloop()
    # for round_num in range(1, 4):
    #     start_timer(25, "Work")
    #     start_timer(5, "Break")
    # start_timer(15, "Break")


if __name__ == "__main__":
    main()
