if __name__ == '__main__':
    n = int(input())
    arr=(input().split())
    arr.sort(reverse=True)
    print(arr[(arr.index(max(arr)))-1])
   
