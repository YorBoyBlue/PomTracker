class AddMenu():
    """
    This class is used to add menu functionality to the main window
    """

    def __init__(self):
        # It adds the next options to the main menu
        self.mainmenu = [
            {'File': [
                {'Save': self.save_pom_sheet},
                '-',
                {'Open Pom Window': self.open_pom_window},
                {'Open Current Pom Sheet': self.load_pom_sheet},
                '-',
                {'Exit': self.exit},
            ]
            }
        ]

    def save_pom_sheet(self):
        pass

    def load_pom_sheet(self):
        pass

    def open_pom_window(self):
        pass

    @staticmethod
    def exit():
        exit()
