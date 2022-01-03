# # 단계: SW Expert Academy
# # 링크: https://swexpertacademy.com/main/main.do
# # 2022-01-03(월)

# # 번호: 2072
# # 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq
# # 문제: 홀수만 더하기

# # 테스트 케이스 갯수 입력
# test_case = int(input())
# # for문을 통해 2차원 배열 입력 / 행갯수 : test_case / 열갯수 : 제한없음, 입력값은 띄어쓰기로 구분
# num = [list(map(int, input().split())) for _ in range(test_case)]

# # 2중 for문을 통해 odd_sum에 홀수값만 더하고 출력
# for i in range(test_case):
#     odd_sum=0
#     for j in range(10):
#         if (num[i][j] % 2) == 1:
#             odd_sum += num[i][j]
#     print('#{} {}'.format(i + 1, odd_sum))

# # 번호: 2056
# # 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QLkdKAz4DFAUq
# # 문제:
# '''
# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# '''

# # 테스트 케이스 갯수 입력
# test_case = int(input())
# # for문을 통해 2차원 배열 입력 / 행갯수 : test_case / 열갯수 : 제한없음
# yyyymmdd = [list(map(int, input())) for _ in range(test_case)]
# # for문을 통해 day에 입력된 날짜의 유효성 판단 후 형식 변환 후 출력
# for i in range(test_case):
#     output_day = ''
#     # yyyy에 년을 저장, mm에 월을 저장, dd에 일을 저장
#     yyyy = str(yyyymmdd[i][0])+str(yyyymmdd[i][1])+str(yyyymmdd[i][2])+str(yyyymmdd[i][3])
#     mm = str(yyyymmdd[i][4])+str(yyyymmdd[i][5])
#     dd = str(yyyymmdd[i][6])+str(yyyymmdd[i][7])
#     # 1월~12월, 1일~31일을 벗어난 값은 -1 출력
#     if int(mm) < 1 or int(mm) > 12 or int(dd) < 1 or int(dd) > 32:
#         output_day = -1
#     # 4월, 6월, 9월, 11월은 30일까지 가능
#     elif int(mm) in [4, 6, 9, 11] and int(dd) > 30:
#         output_day = -1
#     # 2월은 28일까지 가능
#     elif int(mm) == 2 and int(dd) > 28:
#         output_day = -1
#     else:
#         output_day = yyyy + "/" + mm + "/" + dd
#     print('#{} {}'.format(i + 1, output_day))

# # 번호: 2071
# # 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QRnJqA5cDFAUq
# # 문제: 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

# # 테스트 케이스 갯수 입력
# test_case = int(input())
# # for문을 통해 2차원 배열 입력 / 행갯수 : test_case / 열갯수 : 제한없음
# num = [list(map(int, input().split())) for _ in range(test_case)]

# # for문을 통해 평균값 출력
# for i in range(test_case):
#     mean = int(round(sum(num[i]) / 10, 0))
#     print('#{} {}'.format(i + 1, mean))