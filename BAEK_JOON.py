# 단계: 입출력과 사칙연산
# 링크: https://www.acmicpc.net/step/1
# 2022-01-01(토)

# 번호: 2557
# 링크: https://www.acmicpc.net/problem/2557
# 문제: Hello World!를 출력하시오
print('Hello World!')

# 번호: 10718
# 링크: https://www.acmicpc.net/problem/10718
# 문제: 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.
print('강한친구 대한육군\n' * 2)

# 번호: 10171
# 링크: https://www.acmicpc.net/problem/10171
# 문제
'''
\    /\
 )  ( ')
(  /  )
 \(__)|
'''
print('\\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \(__)|')

# 번호: 10172
# 링크: https://www.acmicpc.net/problem/10172
# 문제
'''
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''
print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

# 번호: 1000
# 링크: https://www.acmicpc.net/problem/1000
# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

A, B = map(int, input().split())
print(A+B)

# 번호: 1001
# 링크: https://www.acmicpc.net/problem/1001
# 문제: 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

A, B = map(int, input().split())
print(A-B)

# 번호: 10998
# 링크: https://www.acmicpc.net/problem/10998
# 문제: 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

A, B = map(int, input().split())
print(A*B)

# 번호: 1008
# 링크: https://www.acmicpc.net/problem/1008
# 문제: 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

A, B = map(int, input().split())
print(A/B)

# 번호: 10869
# 링크: https://www.acmicpc.net/problem/10869
# 문제: 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

# 번호: 10430
# 링크: https://www.acmicpc.net/problem/10430
# 문제: 
'''
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
'''

A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# 번호: 2588
# 링크: https://www.acmicpc.net/problem/2588
# 문제: 
'''
문제 링크 참조
'''

A = int(input())
B = int(input())
print(A*(B%10))
print(A*(B%100//10))
print(A*(B//100))
print(A*B)