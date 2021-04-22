num = int(input())
nums=[i for i in range(10,100)]
for i in nums:
    if str(num) in str(i):
        print(f'Ответ 1 :{nums.index(i)+1}')
        break
print(f'Ответ 2 : 1{num}')
print(f'Ответ 3 : {nums[num+1]}')