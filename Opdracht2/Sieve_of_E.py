import time
import sys
file = open("prime.dat" , "w")

N = int(sys.argv[1])
count = 0
List = list(range(0, N+1))
start = time.time()
for i in range (2, N+1):
    if i in List:
        file.write(str(i)+"\n")
        count = count +1
        for j in range (2, int(N/i)+1):
            List[i*j] * 0
        else:
            continue
file.close()
end = time.time()
print("Found " + str(count) + " Prime numbers smaller than " + str(N) + " in " + str (end-start) + " seconds")