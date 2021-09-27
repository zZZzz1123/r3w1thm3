arr = [1, 10, 3, 2, 5, 9, 8, 7, 4, 6] # tuy co 10 element nhung de bai chi yeu chay toi 9 element dau tien

def swap(i):
    print("thay doi gia tri cua index ", i , " index " , i +1)
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
    

print("Mang ban dau: ", arr)
while(True):
    print("Nhap 1 so bat ki:")
    iput = int(input())
    if(iput > 8):
        break
    swap(iput)
    print("Mang hien tai: ", arr)
print("DONE !")



