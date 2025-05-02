import tkinter as tk
from tkinter import ttk

class MarathonPaceCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Marathon Timer")
        master.config(bg="#E0F2F7")

        # --- Styling ---
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.primary_color = "#4CAF50"
        self.secondary_color = "#E0F2F7"
        self.text_color = "#333333"
        self.warning_color = "#FF9800"
        self.faster_color = "#1976D2"
        self.slower_color = "#D32F2F"
        self.on_track_color = "#009688"

        self.style.configure('TLabel', font=('Segoe UI', 14), background=self.secondary_color, foreground=self.text_color)
        self.style.configure('Large.TLabel', font=('Segoe UI', 24, 'bold'), background=self.secondary_color, foreground=self.primary_color, anchor='center')
        self.style.configure('TEntry', font=('Segoe UI', 14), width=10)
        self.style.configure('Time.TEntry', font=('Segoe UI', 14), width=6)
        self.style.configure('TButton', font=('Segoe UI', 14, 'bold'), padding=12, background=self.primary_color, foreground="white")
        self.style.map('TButton',
                       background=[('active', self.primary_color), ('pressed', self.primary_color)],
                       foreground=[('active', 'white'), ('pressed', 'white')])
        self.style.configure('ResultTitle.TLabel', font=('Segoe UI', 18, 'bold'), background=self.secondary_color, foreground=self.text_color, anchor='center')
        self.style.configure('ResultValue.TLabel', font=('Segoe UI', 16), background=self.secondary_color, foreground=self.text_color, anchor='center')
        self.style.configure('Comparison.TLabel', font=('Segoe UI', 16, 'italic'), background=self.secondary_color, anchor='center')
        self.style.configure('TLabelframe', font=('Segoe UI', 14, 'bold'), background=self.secondary_color, foreground=self.text_color)
        self.style.configure('TLabelframe.Label', font=('Segoe UI', 14, 'bold'), background=self.secondary_color, foreground=self.text_color)
        self.style.configure('ButtonFrame.TFrame', background=self.secondary_color)

        # --- Welcome Message ---
        welcome_label = ttk.Label(master, text="Welcome to Marathon Pace Calculator", style='Large.TLabel', padding=20)
        welcome_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # --- Input Frame ---
        input_frame = ttk.LabelFrame(master, text="Enter Race Details", padding=15)
        input_frame.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)

        # Distance Input
        distance_label = ttk.Label(input_frame, text="Distance (km):")
        distance_label.grid(row=0, column=0, padx=10, pady=8, sticky="ew")
        self.distance_entry = ttk.Entry(input_frame)
        self.distance_entry.grid(row=0, column=1, padx=10, pady=8, sticky="ew")
        self.distance_entry.focus()

        # Expected Time Input (Hours and Minutes)
        time_label = ttk.Label(input_frame, text="Expected Time (H:M):")
        time_label.grid(row=1, column=0, padx=10, pady=8, sticky="ew")
        self.hours_entry = ttk.Entry(input_frame, style='Time.TEntry', width=5)
        self.hours_entry.grid(row=1, column=1, padx=(10, 5), pady=8, sticky="w")
        ttk.Label(input_frame, text="H").grid(row=1, column=1, padx=(65, 0), pady=8, sticky="w")
        self.minutes_entry = ttk.Entry(input_frame, style='Time.TEntry', width=5)
        self.minutes_entry.grid(row=1, column=1, padx=(110, 5), pady=8, sticky="w")
        ttk.Label(input_frame, text="M").grid(row=1, column=1, padx=(165, 0), pady=8, sticky="w")

        # Pace Input
        pace_label = ttk.Label(input_frame, text="Pace (min/km):")
        pace_label.grid(row=2, column=0, padx=10, pady=8, sticky="ew")
        self.pace_entry = ttk.Entry(input_frame)
        self.pace_entry.grid(row=2, column=1, padx=10, pady=8, sticky="ew")

        # --- Button Frame ---
        button_frame = ttk.Frame(master, padding=(20, 0, 20, 20), style='ButtonFrame.TFrame')
        button_frame.grid(row=2, column=0, sticky="ew")
        button_frame.columnconfigure(0, weight=1)

        self.calculate_button = ttk.Button(button_frame, text="Calculate", command=self.calculate_results) # Single calculate button
        self.calculate_button.grid(row=0, column=0, sticky="ew")

        # --- Results Frame ---
        self.results_frame = ttk.LabelFrame(master, text="Race Results", padding=15)
        self.results_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.results_frame.columnconfigure(0, weight=1)
        self.results_frame.columnconfigure(1, weight=1)

        self.time_result_label = ttk.Label(self.results_frame, text="", style='ResultValue.TLabel')
        self.time_result_label.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        ttk.Label(self.results_frame, text="Estimated Time:", style='ResultTitle.TLabel').grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.pace_result_label = ttk.Label(self.results_frame, text="", style='ResultValue.TLabel')
        self.pace_result_label.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        ttk.Label(self.results_frame, text="Pace (min/km):", style='ResultTitle.TLabel').grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.speed_result_label = ttk.Label(self.results_frame, text="", style='ResultValue.TLabel')
        self.speed_result_label.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        ttk.Label(self.results_frame, text="Speed (km/hr):", style='ResultTitle.TLabel').grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.comparison_label = ttk.Label(self.results_frame, text="", style='Comparison.TLabel')
        self.comparison_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Bind Enter key
        master.bind('<Return>', lambda event: self.calculate_results())

    def calculate_results(self):
        distance_str = self.distance_entry.get()
        hours_str = self.hours_entry.get()
        minutes_str = self.minutes_entry.get()
        pace_str = self.pace_entry.get()

        distance = float(distance_str) if distance_str else None
        hours = int(hours_str) if hours_str else 0
        minutes = int(minutes_str) if minutes_str else 0
        pace = float(pace_str) if pace_str else None

        self.time_result_label.config(text="")
        self.pace_result_label.config(text="")
        self.speed_result_label.config(text="")
        self.comparison_label.config(text="")

        if distance is not None:
            if hours > 0 or minutes > 0:
                total_minutes = (hours * 60) + minutes
                if total_minutes <= 0:
                    self.comparison_label.config(text="El tiempo esperado debe ser mayor que cero.", foreground=self.warning_color)
                    return
                pace_decimal = total_minutes / distance
                pace_minutes = int(pace_decimal)
                pace_seconds = int((pace_decimal - pace_minutes) * 60)
                speed_km_hr = distance / (total_minutes / 60)

                self.pace_result_label.config(text=f"{pace_minutes} min {pace_seconds} por km", foreground=self.text_color)
                self.speed_result_label.config(text=f"{speed_km_hr:.2f} km/hr", foreground=self.text_color)

                if pace is not None:
                    if pace_decimal < pace:
                        self.comparison_label.config(text="Más rápido que tu objetivo!", foreground=self.faster_color)
                    elif pace_decimal > pace:
                        self.comparison_label.config(text="Más lento que tu objetivo.", foreground=self.slower_color)
                    else:
                        self.comparison_label.config(text="Al ritmo de tu objetivo!", foreground=self.on_track_color)

            elif pace is not None:
                if pace <= 0:
                    self.comparison_label.config(text="El ritmo debe ser mayor que cero.", foreground=self.warning_color)
                    return
                total_minutes = distance * pace
                result_hours = int(total_minutes // 60)
                result_minutes = int(total_minutes % 60)
                speed_km_hr = 60 / pace if pace > 0 else 0

                self.time_result_label.config(text=f"{result_hours} h {result_minutes} min", foreground=self.text_color)
                self.speed_result_label.config(text=f"{speed_km_hr:.2f} km/hr", foreground=self.text_color)

            else:
                self.comparison_label.config(text="Por favor, introduce el tiempo esperado o el ritmo.", foreground=self.warning_color)

        elif pace is not None and hours > 0 or minutes > 0:
            total_minutes = (hours * 60) + minutes
            if total_minutes <= 0:
                self.comparison_label.config(text="El tiempo esperado debe ser mayor que cero.", foreground=self.warning_color)
                return
            calculated_distance = total_minutes / pace
            speed_km_hr = 60 / pace if pace > 0 else 0
            self.distance_entry.insert(0, f"{calculated_distance:.2f}")
            self.speed_result_label.config(text=f"{speed_km_hr:.2f} km/hr", foreground=self.text_color)


        else:
            self.comparison_label.config(text="Por favor, introduce la distancia y el tiempo esperado o el ritmo.", foreground=self.warning_color)


if __name__ == "__main__":
    root = tk.Tk()
    app = MarathonPaceCalculator(root)
    root.mainloop()