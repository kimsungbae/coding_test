# 단계: while문
# 링크: https://www.acmicpc.net/step/2
# 2022-01-04(화)

# 번호: 10952
# 링크: https://www.acmicpc.net/problem/10952
# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

A = B = 1
while True:
    A, B = map(int, input().split())
    if A!=0 and B!=0:
        print(A+B)
    else:
        break

# 번호: 10951
# 링크: https://www.acmicpc.net/problem/10951
# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

# 번호: 1110
# 링크: https://www.acmicpc.net/problem/1110
# 문제:
'''
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 
새로운 수는 26이다.
위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
'''

N = int(input())
count = 0
new_N = N

while True:
    num_10 = new_N // 10
    num_1 = new_N % 10
    new_N = (num_1 * 10) + ((num_10 + num_1) % 10)
    count += 1
    if N == new_N:
        break

print(count)

# 번호: 10818
# 링크: https://www.acmicpc.net/problem/10818
# 문제: N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
num = list(map(int,input().split()))
_min = num[0]
_max = num[0]

for i in num:
    if i < _min:
        _min = i
    if i > _max:
        _max = i
print(_min, _max)

# 번호: 2562
# 링크: https://www.acmicpc.net/problem/2562
# 문제:
'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
'''

num = list(int(input()) for _ in range(9))
count = 0
_max = num[0]

for i in range(9):
    if num[i] > _max:
        _max = num[i]
        count = i+1
print(_max, count, sep="\n")

# 번호: 2577
# 링크: https://www.acmicpc.net/problem/2577
# 문제:
'''
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
'''

A = int(input())
B = int(input())
C = int(input())

multi = A * B * C
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while multi != 0:
    array[multi % 10] += 1
    multi = multi // 10
for i in array:
    print(i)

# 번호: 3052
# 링크: https://www.acmicpc.net/problem/3052
# 문제:
'''
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''

array = []
for i in range(10):
    array.append(int(input()) % 42)
print(len(set(array)))

# 번호: 1546
# 링크: https://www.acmicpc.net/problem/1546
# 문제:
'''
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다.
이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
'''

N = int(input())
score = list(map(int, input().split()))
_max = max(score)
for i in range(N):
    score[i] = score[i] / _max * 100
print(sum(score)/N)

# 번호: 8958
# 링크: https://www.acmicpc.net/problem/8958
# 문제:
'''
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''

test_case = int(input())
_quiz = list([input() for _ in range(test_case)])

for i in range(test_case):
    _result = 0
    score = 0
    for j in range(len(_quiz[i])):
        if _quiz[i][j] == 'O':
            score += 1
        else:
            score = 0
        _result += score
    print(_result)

# 번호: 4344
# 링크: https://www.acmicpc.net/problem/4344
# 문제:
'''
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
'''

test_case = int(input())
class_score = [list(map(int, input().split())) for _ in range(test_case)]

for i in range(test_case):
    _ratio = 0
    class_avg = sum(class_score[i][1:]) / class_score[i][0]
    for j in range(1, len(class_score[i])):
        if class_score[i][j] > class_avg:
            _ratio +=1
    print('{:.3f}%'.format(_ratio / class_score[i][0] * 100))