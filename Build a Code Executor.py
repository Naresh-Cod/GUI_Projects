import tkinter as tk
import threading

def run_script():
    user_code = script_entry.get("1.0", "end-1c")
    try:
        def execute_code():
            # Redirect standard output to capture print statements
            import sys
            from io import StringIO
            original_stdout = sys.stdout
            sys.stdout = StringIO()

            try:
                exec(user_code)
            except Exception as e:
                print(str(e))

            # Get the captured output and display it in the result_text widget
            captured_output = sys.stdout.getvalue()
            result_text.config(state="normal")
            result_text.delete("1.0", "end")  # Clear previous content
            result_text.insert("1.0", captured_output)
            result_text.config(state="disabled")

            # Restore the original stdout
            sys.stdout = original_stdout

        thread = threading.Thread(target=execute_code)
        thread.start()

    except Exception as e:
        result_text.config(state="normal")
        result_text.delete("1.0", "end")  # Clear previous content
        result_text.insert("1.0", str(e))
        result_text.config(state="disabled")

root = tk.Tk()
root.title("Python Script Runner")
root.geometry("700x600")

# Set the background color to black and text color to white
root.configure(bg="black")
script_entry = tk.Text(root, height=10, width=85, bg="black", fg="white", font=("Helvetica", 16))
script_entry.pack()

run_button = tk.Button(root, text="Run Script", command=run_script, bg="black", fg="white", font=("Helvetica", 16))
run_button.pack()

result_text = tk.Text(root, height=20, width=85, bg="black", fg="white", font=("Helvetica", 16))
result_text.pack()
result_text.config(state="disabled")  # Make the result_text widget read-only

root.mainloop()
