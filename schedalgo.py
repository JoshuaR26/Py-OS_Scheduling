print("process name sep by space")
pl = list(map(str,input().split()))
print("arr time sep by space")
atl = list(map(float,input().split()))
print("exec time sep by space")
etl = list(map(float,input().split()))

def FCFSalgo(processList, arrTimeList, execTimeList):

    dict1 = list(zip(processList,arrTimeList,execTimeList))
    print("as inputted")
    print(dict1)

    l=len(dict1)

    for i in range(0,l):
        for j in range(0,l-i-1):
            if(dict1[j][1]>dict1[j+1][1]):
                temp=dict1[j]
                dict1[j]=dict1[j+1]
                dict1[j+1]=temp
    print("in asc order")
    print(dict1)

    compltnTime1=[]
    compltnTime=[]
    k=0

    for i,j,k in dict1:
        compltnTime1.append(k)
    compltnTime.append(compltnTime1[0])
    for i in range(0, len(compltnTime1)-1):
        if(i==0):
            k=compltnTime1[i]+compltnTime1[i+1]
            compltnTime.append(k)
        else:
            k=compltnTime1[i+1]+k
            compltnTime.append(k)
    arrTime=[]
    execTime=[]
    for i,j,k in dict1:
        arrTime.append(j)
        execTime.append(k)
    print("completion time")
    print(compltnTime)

    turnAroundTime=[]
    zipTurn = zip(compltnTime,arrTime)
    for i,j in zipTurn:
        turnAroundTime.append(i-j)
    print("turn around time")
    print(turnAroundTime)

    waitingTime=[]
    zipTurn1=zip(turnAroundTime,execTime)
    for i,j in zipTurn1:
        waitingTime.append(i-j)
    print("waiting time")
    print(waitingTime)

    avgWaitingTime=sum(waitingTime)/len(waitingTime)
    print("average waiting time = ",avgWaitingTime)

FCFSalgo(pl,atl,etl)

def sjf_scheduling(processList, arrival_times, burst_times):
    n = len(arrival_times)
    processes = list(zip(processList, arrival_times, burst_times))
    processes.sort(key=lambda x: x[1])
    
    current_time = 0
    waiting_time = 0
    turnaround_time = 0
    
    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    
    for process in processes:
        process_id, arrival_time, burst_time = process
        waiting_time = max(0, current_time - arrival_time) #HAV TO CHK IF CORRECT
        turnaround_time = waiting_time + burst_time #HAV TO CHK IF CORRECT
        
        print(f"{process_id}\t\t{arrival_time}\t\t{burst_time}\t\t{waiting_time}\t\t{turnaround_time}")
        current_time += burst_time

    avg_waiting_time = sum(process[3] for process in processes) / n #ERROR FROM HERE DOWN
    avg_turnaround_time = sum(process[4] for process in processes) / n
    
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage
#arrival_times = [0, 1, 2, 3]
#burst_times = [4, 3, 1, 5]
sjf_scheduling(pl,atl,etl)

'''# Python program to implement the Shortest Job First algorithm   
  
# Taking the input of the number of processes  
n = int(input("Enter the number of processes: "))  
  
# Creating a matrix for storing the Process Id, Burst Time of each process, Average Waiting Time, and the Average Turn Around Time according to the provided burst times.  
mat = [[0 for j in range(4)] for i in range(n)]  
t, avg_wttime, avg_tatime = 0, 0, 0  
print("Enter the Burst Time of the processes:")  
  
# Taking the input of the burst times of the processes  
# Alloting process Ids to each process  
for i in range(n):   
  mat[i][1] = int(input(f"P{i + 1}: "))  
  mat[i][0] = i + 1  
  
# Sorting the processes that we stored above according to their burst time  
for i in range(n):   
  ind = i  
  for j in range(i + 1, n):  
    if mat[j][1] < mat[ind][1]:  
      ind = j  
  a = mat[i][1]  
  mat[i][1] = mat[ind][1]  
  mat[ind][1] = a  
  a = mat[i][0]  
  mat[i][0] = mat[ind][0]  
  mat[ind][0] = a  
  
# Calculating the waiting times of the processes  
mat[0][2] = 0   
for i in range(1, n):  
  mat[i][2] = 0  
  for j in range(i):  
    mat[i][2] += mat[j][1]  
  t += mat[i][2]  
avg_wtime = t / n  
t = 0  
# Calculating the Turn Around Time for each process  
  
# Printing the data in the table form  
print("P B_T W_T TA_T")  
for i in range(n):  
  mat[i][3] = mat[i][1] + mat[i][2]  
  t += mat[i][3]  
  print(f"P{mat[i][0]} {mat[i][1]} {mat[i][2]} {mat[i][3]}")  
avg_tatime = t / n  
print(f"The average Waiting Time of the whole sequence of processes is = {avg_wtime}")  
print(f"The average Turn Around Time of the processes is = {avg_tatime}")''' 
