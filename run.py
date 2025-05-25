import ui
import sys
import menu

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.main_menu()
    else:
        app=ui.MainWindow()
        app.mainloop()
    # menu.main_menu()
