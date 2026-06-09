ValidBrackets = {
    ")": "(",
    "}": "{",
    "]": "["
}

openBrackets = set(ValidBrackets.values())

class BracketsValidator:
    @staticmethod
    def validateFileContent(fileContent: list[str]) -> list[str]:
        validSubjects = []

        for brackets in fileContent:
            bracketsStack = []
            areBracketsValid = True

            for bracket in brackets:

                if (bracket in openBrackets):
                    bracketsStack.append(bracket)

                else:
                    if (len(bracketsStack) == 0 or bracketsStack[-1] != ValidBrackets[bracket]):
                        areBracketsValid = False
                        break

                    bracketsStack.pop()

            if (areBracketsValid and len(bracketsStack) == 0):
                validSubjects.append(brackets)

        return validSubjects


