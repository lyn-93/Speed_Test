import subprocess
import tkinter as tk
from tkinter import ttk

# Convert bytes/sec to Mbps
def bytes_to_mbps(bytes_per_sec):
    return (bytes_per_sec * 8) / 1_000_000

# Perform speed test
def perform_speed_test():
    test_url = "https://github.com/lyn-93/Speed_Test/blob/main/test_File.txt"  # Test file URL
    download_command = [
        "curl", "-s", "-w", 
        "Download Speed: %{speed_download} bytes/sec\\n", 
        "-o", "/dev/null", 
        test_url
    ]
    try:
        # Run the download speed test
        result = subprocess.run(download_command, capture_output=True, text=True)
        output = result.stdout
        speed_bytes = float(output.split(":")[1].strip().split()[0])
        speed_mbps = bytes_to_mbps(speed_bytes)
        
        # Update GUI labels
        download_label.config(text=f"Download Speed: {speed_mbps:.2f} Mbps")
    except Exception as e:
        download_label.config(text=f"Error: {e}")

# Create Tkinter Window
root = tk.Tk()
root.title("Internet Speed Tester")
root.geometry("400x200")

# Add Widgets
title_label = tk.Label(root, text="Internet Speed Tester", font=("Arial", 16))
title_label.pack(pady=10)

download_label = tk.Label(root, text="Download Speed: Not Tested", font=("Arial", 12))
download_label.pack(pady=5)

start_button = ttk.Button(root, text="Start Test", command=perform_speed_test)
start_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
