class AddMenu():
    """
    This class is used to add menu functionality to the main window
    """

    def __init__(self):
        # this adds the next options to the main menu
        self.mainmenu = [
            {'File': [
                {'Open Pom Window': self.open_pom_window},
                '-',
                {'Exit': self.exit},
            ]
            }
        ]

    def save_pom_sheet(self):
        pass

    def open_pom_window(self):
        pass

    @staticmethod
    def exit():
        exit()
