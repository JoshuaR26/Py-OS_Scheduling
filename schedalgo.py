def calculate_total_execution_time(turnaround_times):
    return sum(turnaround_times)

def calculate_throughput(total_execution_time, num_processes):
    return num_processes / total_execution_time

def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][2]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][2]
        completion_time[i] = turnaround_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = round(sum(turnaround_time) / n, 2)
    total_execution_time = calculate_total_execution_time(turnaround_time)

    print("\nFCFS Scheduling:")
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{completion_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Total Execution Time: {total_execution_time}")
    return total_execution_time

def round_robin(processes, quantum):
    n = len(processes)
    remaining_time = [process[2] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    time = 0
    queue = []

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > quantum:
                    time += quantum
                    remaining_time[i] -= quantum
                    queue.append(i)
                else:
                    time += remaining_time[i]
                    waiting_time[i] = time - processes[i][2]
                    turnaround_time[i] = time
                    completion_time[i] = turnaround_time[i]
                    remaining_time[i] = 0

        if done:
            break

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = round(sum(turnaround_time) / n, 2)
    total_execution_time = calculate_total_execution_time(turnaround_time)

    print("\nRound Robin Scheduling:")
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{completion_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Total Execution Time: {total_execution_time}")
    return total_execution_time

def sjf(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[2])
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    time = 0

    for i in range(n):
        waiting_time[i] = time
        time += processes[i][2]
        turnaround_time[i] = time
        completion_time[i] = turnaround_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = round(sum(turnaround_time) / n, 2)
    total_execution_time = calculate_total_execution_time(turnaround_time)

    print("\nSJF Scheduling:")
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{completion_time[i]}")


    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Total Execution Time: {total_execution_time}")
    return total_execution_time

def priority_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[2])
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    time = 0

    for i in range(n):
        waiting_time[i] = time
        time += processes[i][2]
        turnaround_time[i] = time
        completion_time[i] = turnaround_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = round(sum(turnaround_time) / n, 2)
    total_execution_time = calculate_total_execution_time(turnaround_time)

    print("\nPriority Scheduling:")
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{completion_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Total Execution Time: {total_execution_time}")
    return total_execution_time

# USER INPUT
n = int(input("Enter the number of processes: "))
processes = []
for i in range(n):
    process_id = input(f"Enter the process ID for process {i + 1}: ")
    arrival_time = int(input(f"Enter the arrival time for process {process_id}: "))
    burst_time = int(input(f"Enter the burst time for process {process_id}: "))
    processes.append((process_id, arrival_time, burst_time))

quantum = int(input("Enter the time quantum for Round Robin scheduling: "))

fcfs_total_execution_time = fcfs(processes)
round_robin_total_execution_time = round_robin(processes, quantum)
sjf_total_execution_time = sjf(processes)
priority_scheduling_total_execution_time = priority_scheduling(processes)

fcfs_throughput = round(calculate_throughput(fcfs_total_execution_time, len(processes)), 4)
round_robin_throughput = round(calculate_throughput(round_robin_total_execution_time, len(processes)), 4)
sjf_throughput = round(calculate_throughput(sjf_total_execution_time, len(processes)), 4)
priority_scheduling_throughput = round(calculate_throughput(priority_scheduling_total_execution_time, len(processes)), 4)

print("\nEfficiency Metrics:")
print(f"FCFS - Throughput: {fcfs_throughput}")
print(f"Round Robin - Throughput: {round_robin_throughput}")
print(f"SJF - Throughput: {sjf_throughput}")
print(f"Priority Scheduling - Throughput: {priority_scheduling_throughput}")
