def mergeSort(input_list:list[int]):

    if len(input_list) == 1:
        return input_list
    mid_point :int= len(input_list) // 2

    list_1: list= mergeSort(input_list=input_list[:mid_point])
    list_2:list = mergeSort(input_list=input_list[mid_point:])

    return merge(list_1, list_2)

def merge(list_1: list[int], list_2: list[int]) -> list[int]:

    i, j = 0,0

    result: list[int] = [None for _ in range(len(list_1 + list_2))]

    for k in range(len(result)):

        # if i >  len(list_1):
        #     result [k:] = list_2 [j:]
        #     break

        # elif j > len(list_2):
        #     result [k:] =list_1 [i:]
        #     break

        if list_1[i] > list_2[j]:
            result[k] = list_2[j]
            if j == len(list_1):
                print('sium')
                break
            else:
                j+=1
                print('gg')
                break

        else:
            result[k]=list_1[i]
            if j == len(list_2):
                print('2X sium')
                break
            else:
                i+=1
                print('2X gg')
                
    return result







if __name__ == "__main__":

    input_list : list[int]= [0, 1, 2, 3, 4, 5, 6, 7]

    mergeSort(input_list=input_list)
