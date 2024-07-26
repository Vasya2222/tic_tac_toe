import flet
class Testing(flet.UserControl):
    def __init__(self, data=None):
        super().__init__()
        self.data = data

    def print_data(self):
        print(self.data)