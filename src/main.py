from services.MenuService import MenuService

if __name__ == "__main__":
    while True:
        try:
            validSubjects, totalSubjects = MenuService.startInitialMenu()
            MenuService.startPostValidationMenu(validSubjects=validSubjects, totalSubjects=totalSubjects)
        except ValueError:
            print("\nInvalid input option! Try it again, please.\n")
        except FileNotFoundError:
            print("You didn't select a File! Try it again, please.\n")
