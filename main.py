"""
1. Decide on the task to be done.
2. Set the timer to 25 minutes.
3. Work on task until timer ends.
4. Take 5 minute break.
5. Repeat 1-4 4 times.
6. Take 15-30 minute break.
"""
import tkinter
import math


class PomodoroTimer:
    COLORS = {
        "RED": "D83A56",
        "PINK": "FF616D",
        "YELLOW": "FFEAC9",
        "GREEN": "66DE93"
    }
    CHECKMARK = "✔"
    WORK_TIME = 15
    SHORT_BREAK = 5
    LONG_BREAK = 20

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
        self.timer_text = self.canvas.create_text(
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
            command=self.start_timer,
            highlightthickness=0
        )
        self.start_button.grid(row=2, column=0)

        # Create reset button
        self.reset_button = tkinter.Button(
            text="Reset",
            fg=f"#{self.COLORS['RED']}",
            command=self.reset_timer,
            highlightthickness=0
        )
        self.reset_button.grid(row=2, column=2)

        # Create rep checkmarks
        self.checkmark_text = tkinter.Label(
            text="",
            fg=f"#{self.COLORS['GREEN']}",
            bg=f"#{self.COLORS['YELLOW']}",
            font=("Courier", 24, "bold")
        )
        self.checkmark_text.grid(row=3, column=1)

        self.stage_num = 0
        self.timer = None
        self.work_stages = [0, 2, 4, 6]
        self.short_break_stages = [1, 3, 5]

    def reset_timer(self):
        # Cancel timer
        self.window.after_cancel(self.timer)

        # Reset stage text
        self.stage_text.config(text="Timer")

        # Reset timer text
        self.canvas.itemconfig(self.timer_text, text="00:00")

        # Reset checkmark text
        self.checkmark_text.config(text="")

        # Reset stage tracker
        self.stage_num = 0

    def start_timer(self):
        """Determines which stage we are in.

        Called at app start and when self.stage_num has changed. Calls self.count_down using the new stage
        duration and name.
        """
        if self.stage_num in self.work_stages:
            self.count_down(int(0.1 * 60), "Work ", self.COLORS['RED'])
        elif self.stage_num in self.short_break_stages:
            self.count_down(int(0.1 * 60), "Break", self.COLORS['PINK'])
        else:
            self.count_down(int(0.1 * 60), "Break", self.COLORS['GREEN'])

    def count_down(self, count, stage_name, stage_color):
        """Updates timer and label display, then handles timer continuation/expiration."""
        # Convert timer value in seconds to mm:ss format for display
        timer_minutes = math.floor(count / 60)
        timer_seconds = count % 60
        if timer_seconds < 10:
            timer_seconds = f"0{timer_seconds}"
        timer_value = f"{timer_minutes}:{timer_seconds}"
        self.canvas.itemconfig(self.timer_text, text=timer_value)

        # Set stage label to current stage name
        self.stage_text.config(text=stage_name, fg=f"#{stage_color}")

        # Continue timer or handle end of stage if timer has expired.
        if count > 0:
            # Update every 1000ms
            self.timer = self.window.after(1000, self.count_down, count - 1, stage_name, stage_color)
        else:
            # Counter reached zero

            # Increment stage number
            self.stage_num += 1

            # Once we have completed all stages, reset our timer.
            if self.stage_num == 8:
                self.reset_timer()

            # After stages 0, 2, 4, & 6, we add a checkmark
            checkmark_stages = [1, 3, 5, 7]
            check_text = self.checkmark_text.cget("text")
            if self.stage_num in checkmark_stages:
                check_text = check_text + self.CHECKMARK
            self.checkmark_text.config(text=check_text)
            print(check_text)

            # Start next stage
            self.start_timer()


def main():
    # Create app
    app = PomodoroTimer()

    # Run app
    app.window.mainloop()


if __name__ == "__main__":
    main()
