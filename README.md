# MAPS-Py : Multi-Algorithm Process Simulator - Python

# Project Description
The Multi-Algorithm CPU Process Scheduling Simulator is a comprehensive operating system project implemented in Python that allows users to explore and compare various CPU process scheduling algorithms, including First-Come-First-Serve (FCFS), Shortest Job First (SJF), Round Robin, and Priority-Based scheduling. This project provides a user-friendly graphical user interface (GUI) to input process parameters and analyze the performance of these scheduling algorithms by calculating average turnaround time, waiting time, and other relevant metrics.

# Key Features

1. **Graphical User Interface (GUI):** The project offers a user-friendly GUI that enables users to input essential process details such as process arrival time, burst time, priority, and time quantum (for Round Robin). This GUI simplifies the process of defining the scheduling scenarios.

2. **Algorithm Implementation:** The project contains Python implementations of the following CPU process scheduling algorithms:

    a. **FCFS (First-Come-First-Serve):** Processes are executed in the order they arrive, ensuring a simple, non-preemptive scheduling method.

    b. **SJF (Shortest Job First):** The scheduler selects the process with the shortest burst time, optimizing for minimum execution time.

    c. **Round Robin:** Processes are scheduled in a time-sliced manner with a fixed time quantum, allowing for preemption and fair execution.

    d. **Priority-Based:** Processes are executed based on their assigned priority, with the highest-priority process running first.

3. **Simulation and Metrics Calculation:** The project simulates the execution of processes using the selected scheduling algorithm. It calculates essential metrics such as average turnaround time, average waiting time, and CPU utilization for the specified scenario.

4. **Interactive Visualization:** Users can observe the scheduling process and the progress of each process in real-time using interactive visualizations within the GUI.

5. **Scenario Comparison:** Users can compare the performance of different scheduling algorithms by running scenarios with various input parameters and reviewing the calculated metrics.

# Project Goals
The primary objectives of this project are as follows:

- Provide an educational tool for understanding and visualizing the behavior of various CPU process scheduling algorithms.
- Allow users to experiment with different process scenarios and scheduling algorithms to gain insights into their strengths and weaknesses.
- Help students, educators, and OS enthusiasts in studying and teaching operating system concepts.

# Technologies Used
- Python for algorithm implementation and GUI development.
- Tkinter or a Python GUI library of your choice for creating the graphical user interface.

# Potential Extensions
This project can be extended in several ways, including the implementation of additional scheduling algorithms (e.g., Priority-Based Round Robin), support for multiple CPU cores, and the ability to load and save scheduling scenarios for later analysis.

By implementing a comprehensive set of CPU process scheduling algorithms and providing a user-friendly interface, this project serves as a valuable resource for understanding and experimenting with the core concepts of operating system design and process scheduling.

# Project Team
Gorav Jhabakh -  22BAI1037

Siddharth S -  22BAI1099

V Kamal Jerome - 22BAI1212

Joshua S Raju - 22BAI1213

