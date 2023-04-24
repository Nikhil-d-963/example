import tkinter as tk

def add_pipe_after_words(input_string):
    sentences = input_string.split('\n')
    first_sentence_words = sentences[0].split()
    first_sentence_piped = '|'.join(first_sentence_words)
    if len(sentences) > 1:
        output_string = f'|{first_sentence_piped}|{sentences[1].strip()}|'
    else:
        output_string = f'|{first_sentence_piped}|'
    return output_string

def add_pipe_after_words_gui():
    def process_input():
        input_string = input_box.get("1.0", "end-1c")
        output_string = add_pipe_after_words(input_string)
        output_box.delete("1.0", "end")
        output_box.insert("1.0", output_string)

    # Create the GUI
    window = tk.Tk()
    window.title("Add Pipe After Words")

    input_label = tk.Label(window, text="Input String:")
    input_label.pack()

    input_box = tk.Text(window, height=5, width=50)
    input_box.pack()

    output_label = tk.Label(window, text="Output String:")
    output_label.pack()

    output_box = tk.Text(window, height=5, width=50)
    output_box.pack()

    process_button = tk.Button(window, text="Process Input", command=process_input)
    process_button.pack()

    # Start the main event loop
    window.mainloop()

# Call the GUI function to start the program
add_pipe_after_words_gui()
