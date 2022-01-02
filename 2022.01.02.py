# 단계: 입출력과 사칙연산
# 링크: https://www.acmicpc.net/step/1
# 2022-01-02(일)

# 번호: 1330
# 링크: https://www.acmicpc.net/problem/1330
# 문제: 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

# 번호: 9498
# 링크: https://www.acmicpc.net/problem/9498
# 문제: 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
A = int(input())
if A >= 90 and A <= 100:
    print('A')
elif A >= 80 and A <= 89:
    print('B')
elif A >= 70 and A <= 79:
    print('C')
elif A >= 60 and A <= 69:
    print('D')
else:
    print('F')

# 번호: 2753
# 링크: https://www.acmicpc.net/problem/2753
# 문제: 
'''
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
'''
A = int(input())
if A%4==0 and A%100!=0 or A%400==0:
    print('1')
else:
    print('0')

# 번호: 14681
# 링크: https://www.acmicpc.net/problem/14681
# 문제: 문제 링크 참조

A = int(input())
B = int(input())
if A > 0 and B > 0:
    print('1')
elif A < 0 and B > 0:
    print('1')
elif A < 0 and B < 0:
    print('1')
else:
    print('4')

# 번호: 2884
# 링크: https://www.acmicpc.net/problem/2884
# 문제: 문제 링크 참조

A, B = map(int, input().split())
if B >= 45:
    print(A, B-45)
elif B < 45:
    if A == 0:
        print(23, B+60-45)
    else:
        print(A-1, B+60-45)