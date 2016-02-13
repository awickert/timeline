# timeline

***Plots events on a timeline that is optimized to take up the least amount of space.***

"timeline" generates plots like the flollowing one. It does so by fitting the largest number of non-overlapping events in each line.

![alt text](https://github.com/awickert/timeline/blob/master/events_plot.png?raw=true "Timeline of Events")

Input files for timeline are CSV files, like the provided example "events.txt". Each line of the CSV is formatted as:

Event Name, line style, lower time, higher time, extended lower time, extended higher time

* **Event name:** The label on the timeline bar
* **Line style:** "solid", "dashed", or "dotted"
* **Lower time** and **higher time:**: These are the ages of the event. "Lower" is earlier if going forward in time, or later if going backwards in time (as you see above, with calendar years BP, before present).
* **extended lower time** and **extended higher time:** These create a thin line that extends past the edge of the timeline, and removes the vertical bars that show that there are known, hard start and end dates. This can be used to indicate some uncertainty as to when the event starts and ends.

Send a message if you have questions about the code, and enjoy!
