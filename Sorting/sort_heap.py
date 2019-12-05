#complexity is O(nlogn) as height of tree is logn


def heap_maker(arr, n, i):

    largest_node = i
    left_node = (i*2) + 1
    right_node = (i*2) + 2

    if left_node < n and arr[left_node] > arr[i]:
        largest_node = left_node

    if right_node < n and arr[right_node] > arr[i]:
        largest_node = right_node

    if largest_node != i:
        arr[i], arr[largest_node] = arr[largest_node], arr[i]
        #Now continue the trickle down of the new node moved from largest, to trickle down the leaf nodes
        heap_maker(arr,n,largest_node)


def heap_sort(arr):
    n = len(arr)

    #first make a max-heap from scratch starting from lowest leafs
    for i in range(n,0,-1):
        heap_maker(arr,n,i)

    for i in range (n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heap_maker(arr,i,0)


input_array = [5,4,3,2,1,0]
heap_sort(input_array)
print(input_array)
