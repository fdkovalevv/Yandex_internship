n = int(input())
all_languages = set()
known_by_all = set()

for i in range(n):
    Mi = int(input())
    student_language = set()
    for _ in range(Mi):
        language = input().strip()
        student_language.add(language)
    if i == 0:
        known_by_all = student_language.copy()
    else:
        known_by_all &= student_language
    all_languages |= student_language

print(len(known_by_all))
for _ in sorted(known_by_all):
    print(_)

print(len(all_languages))
for _ in sorted(all_languages):
    print(_)