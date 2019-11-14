"""wxPython provides a GUI for applications."""
import wx


class CalcFrame(wx.Frame):
    """This class sets the maximum size that the calculator can be.
    This is the frame and the panel sits inside."""

    def __init__(self):
        super().__init__(
            None, title="wxCalculator",
            size=(350, 375))
        panel = CalcPanel(self)
        self.SetSizeHints(350, 375, 350, 375)
        self.Show()


class CalcPanel(wx.Panel):
    """This class is the bulk of the application.  The panel sits inside the frame."""

    def __init__(self, parent):
        """The init sets all the text fields to right-justified and sets the last button pressed to None."""
        super().__init__(parent)
        self.running_total = wx.StaticText(self)
        self.solution = wx.TextCtrl(self, style=wx.TE_RIGHT)
        self.last_button_pressed = None
        self.create_ui()

    def create_ui(self):
        """This module is the start of the graphics and input processing."""
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL)
        """This section defines the font used in the solutions field.  Also disables eval"""
        self.solution.SetFont(font)
        self.solution.Disable()
        main_sizer.Add(self.solution, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.running_total, 0, wx.ALIGN_RIGHT)
        """Assigns buttons a value, determines layout, and uses update_equation to update the getValue()
        Which will be used to display info to the user."""
        buttons = [['7', '8', '9', '/'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '-'],
                   ['.', '0', '', '+']]
        for label_list in buttons:
            btn_sizer = wx.BoxSizer()
            for label in label_list:
                button = wx.Button(self, label=label)
                btn_sizer.Add(button, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
                button.Bind(wx.EVT_BUTTON, self.update_equation)
            main_sizer.Add(btn_sizer, 1, wx.ALIGN_CENTER | wx.EXPAND)
        """Creates an equal button and calls on_total."""
        equals_btn = wx.Button(self, label='=')
        equals_btn.Bind(wx.EVT_BUTTON, self.on_total)
        main_sizer.Add(equals_btn, 0, wx.EXPAND | wx.ALL, 3)
        """Creates a clear button and calls on_clear."""
        clear_btn = wx.Button(self, label='Clear')
        clear_btn.Bind(wx.EVT_BUTTON, self.on_clear)
        main_sizer.Add(clear_btn, 0, wx.EXPAND | wx.ALL, 3)

        self.SetSizer(main_sizer)

    def update_equation(self, event):
        """Uses the button's label to process the user input.
        Updates the display."""
        operators = ['/', '*', '-', '+']
        btn = event.GetEventObject()
        label = btn.GetLabel()
        current_equation = self.solution.GetValue()

        if label not in operators:
            if self.last_button_pressed in operators:
                self.solution.SetValue(f"{current_equation} {label}")
            else:
                self.solution.SetValue(current_equation + label)
        elif label in operators and current_equation != '' \
                and self.last_button_pressed not in operators:
            self.solution.SetValue(f"{current_equation} {label}")

        self.last_button_pressed = label

        for item in operators:
            if item in self.solution.GetValue():
                self.update_solution()
                break

    def update_solution(self):
        """This module processes the user's request.
        Updates the display.
        eval is used, but with constraints. The user is not able to enter text into this field."""
        try:
            current_solution = str(eval(self.solution.GetValue()))
            self.running_total.SetLabel(f"{current_solution}    ")
            self.Layout()
            return current_solution
        except ZeroDivisionError:
            self.solution.SetValue("You can not divide by zero.")

    """Clears the both the SetValue and SetLabel which clears the screen."""

    def on_clear(self, event):
        self.solution.Clear()
        self.running_total.SetLabel("")

    """Is called by the equal button being pressed.  Updates the SetLabel"""

    def on_total(self, event):
        solution = self.update_solution()
        if solution:
            self.running_total.SetLabel(f"{solution}")


if __name__ == '__main__':
    app = wx.App(False)
    frame = CalcFrame()
    app.MainLoop()
