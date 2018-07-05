import pyforms
from views_controllers.pom_sheet_window import PomSheetWindow

if __name__ == "__main__":
    pyforms.start_app(PomSheetWindow, geometry=(800, 800, 1000, 1000))
