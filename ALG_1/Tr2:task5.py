# def find_min_append(seq):
#     n = len(seq)
#     for i in range(n):
#         # Проверяем, является ли суффикс от i до n-1 палиндромом
#         suffix = seq[i:]
#         if suffix == suffix[::-1]:
#             # Дописываем элементы от 0 до i-1 в обратном порядке
#             to_append = seq[:i][::-1]
#             return len(to_append), to_append
#     # Если не нашли палиндром, дописываем все элементы в обратном порядке, кроме последнего
#     to_append = seq[:-1][::-1]
#     return len(to_append), to_append
#
# # Чтение входных данных
# N = int(input())
# sequence = list(map(int, input().split()))
#
# M, append_numbers = find_min_append(sequence)
#
# # Вывод результатов
# print(M)
# if M > 0:
#     print(' '.join(map(str, append_numbers)))


def is_palindrome(seq, start, end):
    while start < end:
        if seq[start] != seq[end]:
            return False
        start += 1
        end -= 1
    return True

def find_min_append(seq):
    n = len(seq)
    for i in range(n):
        if is_palindrome(seq, i, n - 1):
            min_append = i
            break
    else:
        min_append = n

    to_append = []
    for j in range(min_append - 1, -1, -1):
        to_append.append(seq[j])

    return len(to_append), to_append

# Чтение входных данных
N_and_rest = input().strip()
while N_and_rest == '':
    N_and_rest = input().strip()
N = int(N_and_rest)
sequence_line = ''
while len(sequence_line.strip().split()) < N:
    sequence_line += input().strip() + ' '
sequence = list(map(int, sequence_line.strip().split()))

M, append_numbers = find_min_append(sequence)

# Вывод результатов
print(M)
if M > 0:
    print(' '.join(map(str, append_numbers)))
