from services.SubjectsPrinter import SubjectsPrinter
from services.GraphicMaker import GraphicMaker

class MenuService:
    @staticmethod
    def startPostValidationMenu(validSubjects: list[str], totalSubjects: int) -> None:
        while True:
            print("\n")
            print("*" * 20, "POST VALIDATION MENU", "*" * 20)
            print("\n Now, what do you want to do?: \n")
            print("[1] Visualize Valid VS Non Valid Subjects Via Graphics")
            print("[2] Print All Valid Subjects")
            print("[3] Return To Initial Menu")

            selectedOption = int(input("\nPlease select an option to continue: "))

            match selectedOption:
                case 1:
                    GraphicMaker.generateValidAndNonValidSubjectsGraphic(
                        totalValidSubjects=len(validSubjects),
                        totalSubjects=totalSubjects,
                    )

                case 2:
                    SubjectsPrinter.printAllValidSubjects(validSubjects=validSubjects)

                case 3:
                    print("\nYessir, We are coming back to the Initial Menu!\n")
                    break

                case _:
                    print(
                        f"\nWe couldn't recognize option {selectedOption}! Try it again, please.\n"
                    )
