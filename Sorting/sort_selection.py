##The time complexity here is same as bubble sort, but it takes lower space

def selection_sort(arr):

    for i in range(len(arr)):
        lowest_element = i;
        for j in range(lowest_element+1, len(arr)):
            if(arr[lowest_element]) > arr[j]:
                arr[lowest_element], arr[j] = arr[j], arr[lowest_element]


input_array = [5,4,3,2,1,0]
selection_sort(input_array)
print(input_array)
