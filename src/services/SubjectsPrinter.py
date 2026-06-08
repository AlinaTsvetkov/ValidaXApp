class SubjectsPrinter:
    @staticmethod
    def printAllValidSubjects(validSubjects: list[str]) -> None:
        print("\n")
        print("*" * 20, "PRINTING ALL VALID SUBJECTS", "*" * 20)

        for i, x in enumerate(validSubjects):
            print(f"Valid Subject N.{i+1}: {x}")