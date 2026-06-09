from services.FileDialog import FileDialog
from services.RegexValidator import RegexValidator
from services.SubjectsPrinter import SubjectsPrinter
from services.GraphicMaker import GraphicMaker
from enums.RegexPatterns import RegexPatterns


class MenuService:
    @staticmethod
    def startInitialMenu() -> tuple[list[str], int]:
        validSubjects = None
        totalSubjects = None

        print("*" * 20, "WELCOME TO VALIDAXAPP", "*" * 20)
        print("\n Available Options: \n")
        print("[1] Validate IPv4 Subjects")
        print("[2] Validate Email Subjects")
        print("[3] Validate Palindrome Subjects")

        selectedOption = int(input("\nPlease select an option to continue: "))

        match (selectedOption):
            case 1:
                ipv4Subjects = FileDialog.getFileContent()
                validSubjects = RegexValidator.validateFileContent(
                    fileContent=ipv4Subjects,
                    regexPattern=RegexPatterns.IPV4_PATTERN.value,
                )

                totalSubjects = len(ipv4Subjects)

            case 2:
                emailSubjects = FileDialog.getFileContent()
                validSubjects = RegexValidator.validateFileContent(
                    fileContent=emailSubjects,
                    regexPattern=RegexPatterns.EMAIL_PATTERN.value,
                )

                totalSubjects = len(emailSubjects)

            case 3:
                print("You have selected Option 3")

            case _:
                print(
                    f"\nWe couldn't recognize option {selectedOption}! Try it again, please.\n"
                )

        return validSubjects, totalSubjects

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
            
            match (selectedOption):
                case 1:
                    GraphicMaker.generateValidAndNonValidSubjectsGraphic(totalValidSubjects=len(validSubjects), totalSubjects=totalSubjects)
            
                case 2:
                    SubjectsPrinter.printAllValidSubjects(validSubjects=validSubjects)
            
                case 3:
                    print("\nYessir, We are coming back to the Initial Menu!\n")
                    break
            
                case _:
                    print(
                        f"\nWe couldn't recognize option {selectedOption}! Try it again, please.\n"
                    )
