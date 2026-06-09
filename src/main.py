from services.MenuService import MenuService
from services.PalindromeValidator import PalindromeValidator
from services.BracketsValidator import BracketsValidator
from enums.RegexPatterns import RegexPatterns
from services.FileDialog import FileDialog
from services.RegexValidator import RegexValidator

if __name__ == "__main__":
    while True:
        try:
            validSubjects = None
            totalSubjects = None
            
            print("*" * 20, "WELCOME TO VALIDAXAPP | By Alina Tsvetkov :)", "*" * 20)
            print("\n Available Options: \n")
            print("[1] Validate IPv4 Subjects")
            print("[2] Validate Email Subjects")
            print("[3] Validate Palindrome Subjects")
            print("[4] Validate Brackets Subjects")
            print("[5] Exit Program")
    
            selectedOption = int(input("\nPlease select an option to continue: "))
    
            match selectedOption:
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
                    palindromeSubjects = FileDialog.getFileContent()
                    validSubjects = PalindromeValidator.validateFileContent(
                        fileContent=palindromeSubjects
                    )
    
                    totalSubjects = len(palindromeSubjects)
    
                case 4:
                    bracketsSubjects = FileDialog.getFileContent()
                    validSubjects = BracketsValidator.validateFileContent(
                        fileContent=bracketsSubjects
                    )
    
                    totalSubjects = len(bracketsSubjects)
    
                case 5:
                    print("Goodbye, Sir :)!")
                    break
    
                case _:
                    print(
                        f"\nWe couldn't recognize option {selectedOption}! Try it again, please.\n"
                    )

            MenuService.startPostValidationMenu(validSubjects=validSubjects, totalSubjects=totalSubjects)
        except ValueError:
            print("\nInvalid input option! Try it again, please.\n")
        except FileNotFoundError:
            print("You didn't select a File! Try it again, please.\n")
