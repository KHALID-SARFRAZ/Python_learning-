student_scores = [150,142,185,120,171,184,24,59,68,199,78,65,89,86,]
total_exam_scores = sum(student_scores)


max_score = 0

for i in student_scores:
    if i > max_score:
        max_score = i

print(max_score)