def roundRobin(burst_times, TQ):
    copy1 = burst_times[:]
    copy2 = burst_times[:]
    copy3 = burst_times[:]
    processes = [i+1 for i in range(len(copy2))]
    w=0
    while (copy2.count(None) != len(copy2)):
        if (copy2[w] != None):
            k = copy2[w]-TQ
            if (k<1):
                copy2[w] = None
            else:
                copy2[w] = k
            if (w == len(copy2)-1):
                w=0
                for k in range(len(copy2)):
                    if (copy2[k] != None):
                        processes.append(k+1)

arrivalTime = []
burstTime = []
completionTime = []

N = int(input('Enter No. of Processes: '))

for i in range(N):
    burstTime.append(int(input('Enter Burst Time for Process ' + str(i+1) + ': ')))
TQ = int(input('Enter Time Quantum: '))
lis = roundRobin(burstTime, TQ)
print('Average Waiting Time: '+str(lis[0]))
print('Avergae Turn Around Time: ' + str(lis[1]))