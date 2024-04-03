def get_grade(score):
   return {
        90 <= score <= 100: "A",
        80 <= score < 90: "B",
        70 <= score <80: "C",
        60 >= score < 70: "D",
        score < 60:"F"
    }.get(True, "Invalide score")

print(get_grade(10))