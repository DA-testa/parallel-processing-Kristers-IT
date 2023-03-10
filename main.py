# python3

def parallel_processing(n, m, data):
    output = []
    laiks = []

    for i in range(m):
        output.append(0)

    for j in range(n):
        laiks.append(0)
    
    n = n - 1
    indekss  = 0
    data_lielums = len(data)
    while data_lielums > 0:
        
        for elementi in range(m):
            
            output[elementi] = (indekss, laiks[indekss])
            laiks[indekss] = laiks[indekss] + data[elementi]
            data_lielums = data_lielums - 1

            if indekss < n:
                indekss = indekss + 1
            else:
                indekss = 0
                
            if len(data) == 0:
                break

    return output

def main():

    n = 0
    m = 0
    n,m = map(int, input().split())
    
    data = []
    data = list(map(int, input().split()))
    
    result = parallel_processing(n,m,data)
    
    for i,j in result:
        print(i,j)

if __name__ == "__main__":
    main()
