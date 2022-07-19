def nextLargerElement(arr):
    res = [-1] * len(arr)
    print(len(res))
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] < arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    print(res)


nextLargerElement([1, 3, 2, 4])
