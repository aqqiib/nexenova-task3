import tkinter as tk
import random

def generate_otp():
    otp = str(random.randint(100000, 999999))
    return otp

def verify_otp():
    user_input = otp_entry.get()
    if user_input == otp:
        status_label.config(text="OTP Verified!", fg="green")
    else:
        status_label.config(text="OTP Incorrect!", fg="red")

def generate_and_send_otp():
    global otp
    otp = generate_otp()
    status_label.config(text="OTP Sent! Please check your phone/email.", fg="blue")

# Create the main application window
app = tk.Tk()
app.title("OTP Verification")

# Generate OTP button
generate_otp_button = tk.Button(app, text="Generate OTP", command=generate_and_send_otp)
generate_otp_button.pack(pady=10)

# OTP entry field
otp_entry = tk.Entry(app, show='*')  # Show '*' to hide the entered OTP
otp_entry.pack(pady=5)

# Verify OTP button
verify_button = tk.Button(app, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=10)

# Status label to show verification status
status_label = tk.Label(app, text="", fg="black")
status_label.pack(pady=5)

# Run the Tkinter main loop
app.mainloop()
