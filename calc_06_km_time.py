import tkinter as tk
from tkinter import ttk

class MarathonPaceCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Marathon Timer")

        # Styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TLabel', font=('Segoe UI', 12))
        self.style.configure('TEntry', font=('Segoe UI', 12))
        self.style.configure('Large.TLabel', font=('Segoe UI', 20, 'bold'), anchor='center') # For the welcome message
        self.style.configure('Time.TEntry', font=('Segoe UI', 12), width=12) # Increased width for hours
        self.style.configure('Small.TEntry', font=('Segoe UI', 12), width=8) # For other inputs
        self.style.configure('TButton', font=('Segoe UI', 12), padding=10)
        self.style.configure('Result.TLabel', font=('Segoe UI', 14, 'bold'))
        self.style.configure('Comparison.TLabel', font=('Segoe UI', 12))

        # --- Welcome Message ---
        welcome_label = ttk.Label(master, text="Welcome to Marathon Pace Calculator", style='Large.TLabel', padding=10)
        welcome_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # --- Input Frame ---
        input_frame = ttk.LabelFrame(master, text="Enter Race Details", padding=15)
        input_frame.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)

        # Distance Input
        self.distance_label = ttk.Label(input_frame, text="Distance (km):")
        self.distance_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.distance_entry = ttk.Entry(input_frame, style='Small.TEntry')
        self.distance_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.distance_entry.focus()

        # Expected Time Input (Hours and Minutes)
        time_label = ttk.Label(input_frame, text="Expected Time (H:M):")
        time_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.hours_entry = ttk.Entry(input_frame, style='Time.TEntry')
        self.hours_entry.grid(row=1, column=1, padx=(5, 2), pady=5, sticky="w")
        self.minutes_entry = ttk.Entry(input_frame, style='Small.TEntry')
        self.minutes_entry.grid(row=1, column=1, padx=(100, 5), pady=5, sticky="w") # Adjusted padx
        ttk.Label(input_frame, text="H").grid(row=1, column=1, padx=(75, 0), pady=5, sticky="w")
        ttk.Label(input_frame, text="M").grid(row=1, column=1, padx=(155, 0), pady=5, sticky="w")

        # Target Pace Input
        self.target_pace_label = ttk.Label(input_frame, text="Target Pace (min/km):")
        self.target_pace_label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.target_pace_entry = ttk.Entry(input_frame, style='Small.TEntry')
        self.target_pace_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # --- Button Frame ---
        button_frame = ttk.Frame(master, padding=(20, 0, 20, 20))
        button_frame.grid(row=2, column=0, sticky="ew") # Moved down due to welcome message
        button_frame.columnconfigure(0, weight=1)

        self.calculate_button = ttk.Button(button_frame, text="Calculate Pace", command=self.calculate_pace)
        self.calculate_button.grid(row=0, column=0, sticky="ew")

        # --- Results Frame ---
        results_frame = ttk.LabelFrame(master, text="Race Results", padding=15)
        results_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew") # Moved down
        results_frame.columnconfigure(0, weight=1)

        self.result_label = ttk.Label(results_frame, text="", style='Result.TLabel', anchor='center')
        self.result_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.comparison_label = ttk.Label(results_frame, text="", style='Comparison.TLabel', anchor='center')
        self.comparison_label.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Bind Enter key
        master.bind('<Return>', lambda event: self.calculate_button.invoke())

    def calculate_pace(self):
        try:
            distance = float(self.distance_entry.get())
            hours = int(self.hours_entry.get()) if self.hours_entry.get() else 0
            minutes = int(self.minutes_entry.get()) if self.minutes_entry.get() else 0
            target_pace = float(self.target_pace_entry.get()) if self.target_pace_entry.get() else None

            total_minutes = (hours * 60) + minutes
            if total_minutes <= 0:
                self.result_label.config(text="Expected time must be greater than zero.")
                self.comparison_label.config(text="")
                return

            pace_min_km = total_minutes / distance
            speed_km_hr = distance / (total_minutes / 60)

            result_text = (
                f"Pace (min/km): {pace_min_km:.2f}\n"
                f"Speed (km/hr): {speed_km_hr:.2f}"
            )
            self.result_label.config(text=result_text)

            if target_pace is not None:
                if pace_min_km < target_pace:
                    self.comparison_label.config(text="Faster than your target pace!", foreground="green")
                elif pace_min_km > target_pace:
                    self.comparison_label.config(text="Slower than your target pace.", foreground="red")
                else:
                    self.comparison_label.config(text="On track with your target pace!", foreground="blue")
            else:
                self.comparison_label.config(text="")

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numbers for distance and target pace, and integers for time.")
            self.comparison_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarathonPaceCalculator(root)
    root.mainloop()