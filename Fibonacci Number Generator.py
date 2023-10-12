import tkinter as tk

def generate_fibonacci_numbers():
    n = int(entry.get())
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    while len(fibonacci_sequence) < n:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)

    result_label.config(text=f"Fibonacci Sequence: {', '.join(map(str, fibonacci_sequence))}")

app = tk.Tk()
app.title("Fibonacci Number Generator")

label = tk.Label(app, text="Enter the number of Fibonacci numbers to generate:", font=("Helvetica", 16))
label.pack()

entry = tk.Entry(app, font=("Helvetica", 16))
entry.pack()

generate_button = tk.Button(app, text="Generate", command=generate_fibonacci_numbers, font=("Helvetica", 16))
generate_button.pack()

result_label = tk.Label(app, text="", font=("Helvetica", 16))
result_label.pack()

app.mainloop()
