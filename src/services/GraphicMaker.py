import matplotlib.pyplot as mp

class GraphicMaker:
    @staticmethod
    def generateValidAndNonValidSubjectsGraphic(totalValidSubjects: int, totalSubjects: int) -> None:
        mp.title("Total of Valid and Non Valid Subjects")
        bars = mp.bar(
            x=["Valid Subjects", "Non Valid Subjects"],
            height=[totalValidSubjects, totalSubjects - totalValidSubjects]
        )

        mp.bar_label(bars)
        mp.xlabel("Subjects")
        mp.ylabel("Total")

        mp.show()
