def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 提前退出冒泡循环的标志位
        flag = False
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                # 交换两个元素
                arr[j-1], arr[j] = arr[j], arr[j-1]
                flag = True
        if not flag:
            # 没有数据交换，提前退出
            break
    return arr

# 测试代码
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(test_array)
    print("Sorted array is:", sorted_array)
