student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
print(min(student_scores))
print(max(student_scores))

#pause 1
#max score
max_score = 0
for i in student_scores:
    if i > max_score:
        max_score = i

print(max_score)

#min score
min_score = max_score
for j in student_scores:
    if j < min_score:
        min_score = j

print(min_score)

#COMPLETE THIS CHALLENGE WITHOUT USING max()
exam_results = [8, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for a in exam_results:
    if a > highest_score:
        highest_score = a

print(highest_score)
