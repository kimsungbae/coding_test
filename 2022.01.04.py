단계: for문
링크: https://www.acmicpc.net/step/3
2022-01-04(화)

# 번호: 2739
# 링크: https://www.acmicpc.net/problem/2739
# 문제: N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

N = int(input())
for i in range(1, 10):
    print('{} * {} = {}'.format(N, i, N*i))

# 번호: 10950
# 링크: https://www.acmicpc.net/problem/10950
# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

test_case = int(input())
num = [list(map(int, input().split())) for _ in range(test_case)]

for i in range(test_case):
    sum = 0
    for j in range(len(num[i])):
        sum += num[i][j]
    print(sum)

# 번호: 8393
# 링크: https://www.acmicpc.net/problem/8393
# 문제: n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

N = int(input())
sum = 0
for i in range(N):
    sum += i+1
print(sum)

# 번호: 15552
# 링크: https://www.acmicpc.net/problem/15552
# 문제: n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

import sys
test_case = int(input())
for i in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    
# 번호: 2741
# 링크: https://www.acmicpc.net/problem/2741
# 문제: 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

N = int(input())

for i in range(N):
    print(i+1)
        
# 번호: 2742
# 링크: https://www.acmicpc.net/problem/2742
# 문제: 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

N = int(input())

for i in range(N,0,-1):
    print(i)
  
# 번호: 11021
# 링크: https://www.acmicpc.net/problem/11021
# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

test_case = int(input())

num = [list(map(int, input().split())) for _ in range(test_case)]

for i in range(test_case):
    sum = 0
    sum = num[i][0]+num[i][1]
    print('Case #{}: {}'.format(i+1, sum))

# 번호: 11022
# 링크: https://www.acmicpc.net/problem/11022
# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

test_case = int(input())
num = [list(map(int, input().split())) for _ in range(test_case)]

for i in range(test_case):
    sum = 0
    sum = num[i][0] + num[i][1]
    print('Case #{}: {} + {} = {}'.format(i+1, num[i][0], num[i][1], sum))

# 번호: 2438
# 링크: https://www.acmicpc.net/problem/2438
# 문제: 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

N = int(input())

for i in range(1,N+1):
    print('{}'.format('*'*i))

# 번호: 2439
# 링크: https://www.acmicpc.net/problem/2439
# 문제: 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

N = int(input())

for i in range(1,N+1):
    print('{}{}'.format(' '*(N-i),'*'*i))

# 번호: 10871
# 링크: https://www.acmicpc.net/problem/10871
# 문제: 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

N, X = map(int, input().split())
A = list(map(int, input().split()))
A_output = 0
for i in range(N):
    if A[i] < X:
        print(A[i], end=' ')
    
