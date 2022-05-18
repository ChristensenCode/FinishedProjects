import tkinter as tk


class ClassJustForTesting:
    def __init__(self) -> None:
        print("might be nothing")
        self.variable_value = 10

    def first_method(self):
        return 12


class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self["background"] = self["activebackground"]

    def on_leave(self, e):
        self["background"] = self.defaultBackground


class PrimaryWindow:
    def __init__(self, master=None):
        self.master = master
        self.keylog = []

        entered_value = tk.Label(master, text="Calculator Input", font=("Arial", 16))
        entered_value.grid(column=0, row=0, columnspan=2, sticky="EW")

        self.entered_value_text = tk.StringVar()
        self.entered_value_text.set("")
        self.entered_value = tk.Label(master, text=self.entered_value_text.get())
        self.entered_value.grid(column=0, row=1, columnspan=2, sticky="EW")

        keypad_frame = tk.Frame(master)
        keypad_frame.grid(column=0, row=2, sticky="N")
        self.generate_number_buttons(keypad_frame)

        # Section adds the mathematical operation buttons.
        math_operation_frame = tk.Frame(master)
        math_operation_frame.grid(column=1, row=2, sticky="N")
        self.generate_operation_buttons(math_operation_frame)

        self.equal_button_text = "="
        equal_button = HoverButton(
            math_operation_frame,
            text=self.equal_button_text,
            command=self.evaluate_expression,
            width=10,
            activebackground="grey",
        )
        equal_button.grid(column=4, row=0, rowspan=4, sticky="NS", padx=2, pady=2)

        self.clear_button_text = "CE"
        clear_button = HoverButton(
            math_operation_frame,
            text=self.clear_button_text,
            command=self.clear_expression,
            width=10,
            activebackground="grey",
        )
        clear_button.grid(column=5, row=0, rowspan=4, sticky="NS", padx=2, pady=2)

    def generate_number_buttons(self, frame):
        self.zero_button_text = "0"
        zero_button = HoverButton(
            frame,
            text=self.zero_button_text,
            command=lambda *args: self.update_calculator_input("0"),
            height=5,
            background="white",
            activebackground="grey",
            relief="flat",
        )
        zero_button.grid(column=0, row=3, columnspan=3, sticky="WE", padx=2, pady=2)

        button_text = 1
        for row in reversed(range(3)):
            for column in range(3):
                number_button = HoverButton(
                    frame,
                    text=str(button_text),
                    command=lambda button_text=button_text: self.update_calculator_input(
                        str(button_text)
                    ),
                    width=10,
                    height=5,
                    relief="flat",
                    background="white",
                    foreground="black",
                    activebackground="grey",
                )
                number_button.grid(column=column, row=row, padx=2, pady=2)
                button_text += 1

    def generate_operation_buttons(self, frame):
        math_operation_symbols = [" / ", " x ", " - ", " + "]

        for index, math_operation_symbol in enumerate(math_operation_symbols):
            plus_button = HoverButton(
                frame,
                text=math_operation_symbol,
                command=lambda math_operation_symbol=math_operation_symbol: self.update_calculator_input(
                    math_operation_symbol
                ),
                width=10,
                height=5,
                activebackground="grey",
            )
            plus_button.grid(column=3, row=index, padx=2, pady=2)

    def update_calculator_input(self, button_number):
        math_operations = (" + ", " - ", " x ", " / ")

        if button_number == "*":
            button_number = " x "

        if (
            self.entered_value_text.get().endswith(math_operations)
            and button_number in math_operations
        ):
            return

        new_text = self.entered_value_text.get() + button_number
        self.entered_value_text.set(new_text)
        if len(
            self.entered_value_text.get()
        ) == 3 and self.entered_value_text.get().startswith(math_operations):
            self.entered_value_text.set("")
            return
        if button_number == " x ":
            button_number = "*"
        self.keylog.append(button_number)
        self.entered_value["text"] = self.entered_value_text.get()

    def evaluate_expression(self):
        combined_key_log = "".join(self.keylog).replace(" ", "")
        if combined_key_log.endswith(("/", "*", "+", "-")):
            return
        answer = eval("".join(self.keylog))

        self.print_output(answer)

    def print_output(self, converted_values):
        self.entered_value_text.set(converted_values)
        self.entered_value["text"] = self.entered_value_text.get()
        self.entered_value_text.set(str(converted_values))
        self.keylog = [str(converted_values)]

    def clear_expression(self):
        self.entered_value_text.set("")
        self.entered_value["text"] = self.entered_value_text.get()
        self.keylog.clear()


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("500x500")
    PrimaryWindow(master=window)
    window.mainloop()
    # x = ClassJustForTesting()
