# PROCESSES AND SIGNALS
### TASKS 
**0. WHAT IS MY PID**

Write a Bash script that displays its own PID.

**1. LIST YOUR PROCESSES**

Write a Bash script that displays a list of currently running processes.

Requirements:
+ Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
+ Show process hierarchy

**2. SHOW YOUR BASH PID**

Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:
+ You cannot use pgrep
- The third line of your script must be # shellcheck disable=SC2009

**3. SHOW YOUR BASH PID MADE EASY**

Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:
+ You cannot use ps

**4. TO INFINITY AND BEYOND**

Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:
+ In between each iteration of the loop, add a sleep 2

**5. DON'T STOP ME NOW**

We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:
+ You must use kill

**6. STOP ME IF YOU CAN**

Write a Bash script that stops 4-to_infinity_and_beyond process.

Requirements:
+ You cannot use kill or killall

**7. HIGHLANDER**

Write a Bash script that displays:

+ To infinity and beyond indefinitely
- With a sleep 2 in between each iteration
+ I am invincible!!! when receiving a SIGTERM signal

Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

**8. BEHEADED PROCESS**

Write a Bash script that kills the process 7-highlander.
