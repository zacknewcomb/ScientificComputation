def cross_prod(v1,v2):
    i = (v2[2]*v1[1])-(v2[1]*v1[2])
    j = -1* ((v2[2]*v1[0])-(v2[0]*v1[2]))
    k = (v2[1]*v1[0])-(v2[0]*v1[1])
    
    return (i, j, k)

def main():
    v1 = list(map(int, input("First vector: ").strip().split()))
    v2 = list(map(int, input("Second vector: ").strip().split()))
    i, j, k = cross_prod(v1,v2)
    print( str(i) + 'i ' + str(j) + 'j ' + str(k) + 'k')
    
    
main()
    
    