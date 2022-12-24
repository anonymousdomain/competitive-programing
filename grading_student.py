class Grade:
    def round_grade(self, grades):
        for i in range(0, len(grades)):
            if grades[i] < 38:
                continue

            else:
                temp = grades[i]
                te = grades[i] % 5
                if te == 3:
                    temp = temp+2
                    grades[i] = temp
                elif te == 4:
                    temp = temp+1
                    grades[i] = temp
                else:
                    continue

        return grades


g = Grade()

s = g.round_grade([34, 54, 67])

print(s)
