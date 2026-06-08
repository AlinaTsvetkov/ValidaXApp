from enums import RegexPatterns
from re import fullmatch

class RegexValidator:
    @staticmethod
    def validateFileContent(fileContent: list[str], regexPattern: RegexPatterns) -> list[str]:
        return [x for x in fileContent if bool(fullmatch(pattern=regexPattern, string=x)) is True]

    