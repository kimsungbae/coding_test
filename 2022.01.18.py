# # 번호: 1288
# # 링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN
# # 문제
# '''
# 링크 참조
# '''

# T = int(input())
# for i in range(T):
#     array = [0] * 10
#     count = 0
#     j = 1
#     N = int(input())
    
#     while count != 10:
#         sheep = str(N * j)
#         for k in sheep:
#             if array[int(k)]==0:
#                 array[int(k)] = 1
#                 count += 1
#         j += 1
#     print("#{} {}".format(i+1, N*(j-1)))
