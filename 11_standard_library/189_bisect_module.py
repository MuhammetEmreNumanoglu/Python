import bisect

sorted_list = [1, 3, 5, 7, 9, 11]

pos = bisect.bisect_left(sorted_list, 5)
print("bisect_left for 5:", pos)

pos = bisect.bisect_right(sorted_list, 5)
print("bisect_right for 5:", pos)

pos = bisect.bisect_left(sorted_list, 6)
print("bisect_left for 6:", pos)

bisect.insort(sorted_list, 6)
print("After insort 6:", sorted_list)

bisect.insort(sorted_list, 4)
print("After insort 4:", sorted_list)

def grade(score):
    breakpoints = [60, 70, 80, 90]
    grades = ["F", "D", "C", "B", "A"]
    return grades[bisect.bisect(breakpoints, score)]

for s in [45, 65, 75, 85, 95]:
    print(f"Score {s}: {grade(s)}")
