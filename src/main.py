# Documentation of Api : https://jikan.docs.apiary.io/

import constants
import menu

def main():
    # calling menu function
    menu.createMenu(constants.API, constants.ICON_NAME, constants.SCHEDULE_SCRIPT)

if __name__ == "__main__":
    # Call main when this python file is not imported 
    # to other python file
    main()