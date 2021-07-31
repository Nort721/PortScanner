![Capture](https://user-images.githubusercontent.com/24839815/127751275-02d9205c-203b-47e5-a6e2-69aca23f42f1.PNG)

# What is it?
This is a simple multithreaded port scanner script made with python, since it takes at least one second to verify
if a port is open or closed because of the need to wait for timeout to verify if its closed or the delay is caused by connection lag, this script allows you to choose how many threads
you want to use for the scanning, the advantage of using multiple threads is that each thread would be able
to scan different ports at the same time

# Example
Lets say you want to scan ports 1 to 1000, lets estimate that every port scan takes 1 second,
in that case the scanning would take about 16 minutes if we use only one thread which is pretty bad.
if we choose to do the same task though this time we decide to use 10 threads, we can devide the Task
to all of these threads meaning each one will scan 100 ports at the same time, effectively reducing the
time it would take to one minute and 40 seconds which is a huge improvement


# Why I made it?
I made it completely for fun and learning as a short out of interest project, also its been a while since I made something with python
so I wanted to make something with it again, also because I grew some interest in making small tools for all kinds of tasks with python,
and I'm fully aware that there are a lot of ways it could be improved and that there are way better tools out there like NMap: https://nmap.org/
which I completely recommend you to use over this one for any task you might need to get done since as said before this project was made as a quick
experiment for fun and learning pourposes and was not aimed at making the best port scanner in the world,

however if you are interested in how a script
like that would work or want to experiment with it feel free to fork the project or download the source code and have fun

## Warning
Do not scan for open ports of other peoples stuff as thats illegal, only use it either on servers that you own or that you
got direct permission to scan
