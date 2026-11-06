def quick_merge(total_list):
    total_list = []
    for i in range(n):
        total_list += input().split()

    total_list = [int(x) for x in total_list]
    total_list.sort()
    return total_list


n = int(input())

print(*quick_merge(n), sep=' ')