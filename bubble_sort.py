##This is bubble sort with flag based optimization

def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if(arr[i]) > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                swapped = True

input_array = [5,4,3,2,1,0]
bubble_sort(input_array)
print(input_array)