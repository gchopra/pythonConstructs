#Same time complexity as bubble and selection sort

def insertion_sort(arr):

    for i in range(1, len(arr)):
        insertion_item = arr[i];
        j = i -1;
        #if insertion item is lesser than the current item, move sorted list up
        while j >= 0 and arr[j]>insertion_item:
            arr[j+1] = arr[j] #insertion item has been saved, so you can overwrite it
            j -= 1
        arr[j+1] = insertion_item


input_array = [5,4,3,2,1,0]
insertion_sort(input_array)
print(input_array)
