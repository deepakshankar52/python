
# for i in roommates:
#         print(i)

# for i in roommates:
#     if(i == "deepak"):
#         print("success")

# print(roommates)

# print(roommates[0],roommates[1])
# print(roommates[0],roommates[2])
# print(roommates[0],roommates[3])
# print(roommates[0],roommates[4])

# print('---')

# print(roommates[0],roommates[1])
# print(roommates[2],roommates[3])
# print(roommates[4],roommates[0])

i = 0
# while(i<5):
#     if(roommates[i] != roommates[i+1]):
#         print(roommates[i])
#     i += 1
# print(roommates[i+1])

roommates = ["deepak","vijay","kabilan","suvin","kabilavathan"]
sec_roommates = ["deepak","vijay","kabilan","suvin","kabilavathan"]

result = []

for i in range(len(roommates)):
    for j in range(len(sec_roommates)):
        if(i != j):
            result.append(roommates[i])
print(result)

        # names = roommates[i]
        # print(i, names)