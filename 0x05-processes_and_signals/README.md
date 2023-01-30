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
