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
    while m > 0:
        
        for elementi in range(m):

            output[elementi] = (indekss, laiks[indekss])
            laiks[indekss] = laiks[indekss] + data[elementi]
            m = m - 1

            if indekss < n:
                indekss = indekss + 1
            else:
                indekss = 0
                
            if m == 0:
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
