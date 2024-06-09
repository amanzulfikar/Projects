from tkinter import *

class Operations(object):
   
    def display(self):
        
        root = Tk()

        first_number_label = Label(root, text='First Number')
        first_number_label.grid(sticky=E, padx=5, pady=5, row=0, column=0)

        first_number_entry = Entry(root, width=10)
        first_number_entry.grid(padx=5, pady=5, row=0, column=1)

        second_number_label = Label(root, text='Second Number')
        second_number_label.grid(sticky=E, padx=5, pady=5, row=1, column=0)

        second_number_entry = Entry(root, width=10)
        second_number_entry.grid(padx=5, pady=5, row=1, column=1)

        def do_operation(operation):
            first_number_text = first_number_entry.get()
            first_number = float(first_number_text)

            second_number_text = second_number_entry.get()
            second_number = float(second_number_text)
            
            if operation == 'add':
                result = first_number + second_number
            elif operation == 'subtract':
                result = first_number - second_number
            elif operation == 'multiply':
                result = first_number * second_number
            elif operation == 'divide':
                result = first_number / second_number
            else:
                result = "Invalid operation"
            
            result_label.config(text=str(result))

        add_button = Button(root, text='Add', command=lambda: do_operation('add'))
        add_button.grid(sticky=E+W, row=2, padx=5, pady=5, column=0)

        subtract_button = Button(root, text='Subtract', command=lambda: do_operation('subtract'))
        subtract_button.grid(sticky=E+W, row=2, padx=5, pady=5, column=1)

        multiply_button = Button(root, text='Multiply', command=lambda: do_operation('multiply'))
        multiply_button.grid(sticky=E+W, row=2, padx=5, pady=5, column=2)

        divide_button = Button(root, text='Divide', command=lambda: do_operation('divide'))
        divide_button.grid(sticky=E+W, row=2, padx=5, pady=5, column=3)

        result_label = Label(root, text='Result')
        result_label.grid(sticky=E+W, padx=5, pady=5, row=3, column=0, columnspan=4)

        root.mainloop()

if __name__ == '__main__':
    app = Operations()
    app.display()



