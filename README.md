# Print labels with Brother printer

The app has a simple GUI where the employee writes the item number and clicks Print button (or hits return key).
At this point, the script searches for the item number in the company's API (after parsing the csv), finds the product name and returns it.
It then limits the string to 90 chars (to fit the label field) and adds the item number and processed name in the according fields.
Finally, it prints the label.

This simple app reduces the time to print a label from 30.5 sec to 12.2 sec, which at the company's rate of aprox. 926 labels per month, saves one employee around 4 hours and 43 minutes per month.

Print-screen:
![image](https://github.com/avaseduard/print-label/assets/108252343/01125e8a-68c2-4ecf-9de6-b3fc3f36e980)
