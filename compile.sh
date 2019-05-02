pyinstaller -F -w --icon=logo.ico main.py -p welcome.py --hidden-import WelcomeShow -p ui_main.py --hidden-import UiMain -p line_show.py --hidden-import LineShow -p set_show.py --hidden-import
SetShow -p sqlite_util.py --hidden-import query --hidden-import update
or
pyinstaller -F -w --icon=logo.ico main.py