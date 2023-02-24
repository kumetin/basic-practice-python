# Given the names and grades for each student in a class of students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
#
# Example
# records = [["chi",20.0],["beta",50.0],["alpha",50.0]]
# The ordered list of scores is [20,0,50.0], so the second lowest score is 50.0 . There are two students with that score:
#
# . Ordered alphabetically, the names are printed as:
#
# alpha
# beta
#
# Input Format
#
# The first line contains an integer, N, the number of students.
# The subsequent lines describe each student over
#
# lines.
# - The first line contains a student's name.
# - The second line contains their grade.
#
# Constraints
#
#     There will always be one or more students having the second lowest grade.
#
# Output Format
#
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input 0
#
# 5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21
#
# Sample Output 0
#
# Beria
# Harsh
#
# Explanation 0
#
# There are 5 students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
# The lowest grade of 37.2 belongs to Tina. The second lowest grade of belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
import sys


def find_mins(records: list):
    min_val = sys.float_info.max
    mins_indices = []
    for i,curr_score in enumerate(records):
        curr_score = records[i][1]
        if curr_score < min_val:
            mins_indices = [i]
        elif curr_score == min_val:
            mins_indices.append(i)
        min_val = curr_score if curr_score < min_val else min_val
    return list(map(lambda x: records[x], mins_indices))


if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append(list((name, score)))

    lowest_grades_records = find_mins(records)

    for r in lowest_grades_records:
        records.remove(r)

    records.sort(key=lambda x: x[0])
    second_lowest_grades_records = find_mins(records)
    for r in second_lowest_grades_records:
        print(r[0])
