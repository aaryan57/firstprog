import matplotlib.pyplot as plt
def main():
    N = 10
    arr = [10, 4, 2, 12, 3, 20, 30, 11, 25, 31]  # initial data
    i, m1, m2, a, b, n = 0, 0, 0, 0, 0, 0
    flag = True
    sum1, sum2 = 0, 0
    a = arr[0]
    b = arr[1]
    m1 = a
    m2 = b
    cluster1 = [0] * 10
    cluster2 = [0] * 10
    k, j = 0, 0
    for i in range(10):
        print(arr[i], end="\t")
    print()
    while flag==True:
        n += 1
        k, j = 0, 0
        for i in range(10):
            if abs(arr[i] - m1) <= abs(arr[i] - m2):
                cluster1[k] = arr[i]
                k += 1
            else:
                cluster2[j] = arr[i]
                j += 1
        sum1, sum2 = 0, 0
        for i in range(k):
            sum1 += cluster1[i]
        for i in range(j):
            sum2 += cluster2[i]
        a, b = m1, m2
        m1 = round(sum1 / k)
        m2 = round(sum2 / j)
        if m1 == a and m2 == b:
            flag = False
        else:
            flag = True
        print(f"After iteration {n}, cluster 1 :\n")
        for i in range(k):
            if cluster1[i] != 0:
                print(cluster1[i], end="\t")
        print("\n")
        print(f"After iteration {n}, cluster 2 :\n")
        for i in range(j):
            if cluster2[i] != 0:
                print(cluster2[i], end="\t")
        if flag == False:
            break
    print("Final cluster 1 :\n")
    for i in range(k):
        if cluster1[i] != 0:
            print(cluster1[i], end="\t")
    print()
    print("Final cluster 2 :\n")
    for i in range(j):
        if cluster2[i] != 0:
            print(cluster2[i], end="\t")
    print()
    # Plot the clusters
    plt.scatter(range(k), cluster1[:k], c='r', label='Cluster 1')
    plt.scatter(range(k, k + j), cluster2[:j], c='b', label='Cluster 2')
    plt.xlabel('Data Point Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
if __name__ =="__main__":
    main()