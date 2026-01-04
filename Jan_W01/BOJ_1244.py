# 스위치 켜고 끄기

def girl(arr, num, N):
    left = num - 1
    right = num + 1
    
    while True:
        
        if 0 > left or right >= N:
            break
        
        if arr[left] == arr[right]:
            arr[left] = abs(arr[left] - 1)
    return 


def boy(arr, num, N):
    for i in range(N):
        if i % num == 0:
            arr[i] = abs(arr[i] - 1)
    return 