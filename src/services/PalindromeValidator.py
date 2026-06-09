class PalindromeValidator:
    @staticmethod
    def validateFileContent(fileContent: list[str]) -> list[str]:
        validSubjects = []

        for word in fileContent:
            left = 0
            right = len(word) - 1
            isPalindrome = True

            while left < right:
                if (word[left] != word[right]):
                    isPalindrome = False
                    break
                
                left += 1
                right -= 1

            if (isPalindrome):
                validSubjects.append(word)

        return validSubjects