# 단계: 스택
# 링크: https://www.acmicpc.net/step/11
# 2022-01-06(목)

# 번호: 10828
# 링크: https://www.acmicpc.net/problem/10952
# 문제:
'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

# import sys

# N = int(sys.stdin.readline())
# _stack = []
# for i in range(N):
#     A = list(sys.stdin.readline().split())
#     if A[0] == 'push':
#         _stack.append(A[1])
#     elif A[0] == 'pop':
#         if len(_stack) != 0:
#             print(_stack.pop())
#         else:
#             print(-1)
#     elif A[0] == 'size':
#         print(len(_stack))
#     elif A[0] == 'empty':
#         if _stack == []:
#             print(1)
#         else:
#             print(0)
#     elif A[0] == 'top':
#         if len(_stack) != 0:
#             print(_stack[-1])
#         else:
#             print(-1)

# # 번호: 10773
# # 링크: https://www.acmicpc.net/problem/10773
# # 문제
# '''
# 나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.
# 재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.
# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!
# '''

# K = int(input())
# array = [0 for _ in range(K)]
# j = 0
# for i in range(K):
#     num = int(input())
#     if num != 0:
#         array[j] = num
#         j += 1
#     else:
#         array[j-1] = 0
#         j -= 1
# print(sum(array))

# # 번호: 9012
# # 링크: https://www.acmicpc.net/problem/9012
# # 문제
# '''
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
# 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
# '''

# T = int(input())
# VPS = [input() for _ in range(T)]
# # print(VPS)
# # print(VPS[0])
# # print(VPS[0][0])

# for i in range(T):
#     VPS_result ,j = 0, 0
#     _result = 'NO'
#     while (VPS_result >= 0) and (j < len(VPS[i])):
#         if VPS[i][j] =='(':
#             VPS_result += 1
#         elif VPS[i][j] ==')':
#             VPS_result -= 1
#         j += 1
#     if VPS_result == 0:
#         _result = 'YES'
#     print(_result)

# 번호: 4949
# 링크: https://www.acmicpc.net/problem/4949
# 문제
'''
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
하나 또는 여러줄에 걸쳐서 문자열이 주어진다.
각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
'''