NOTE/TODO: README OUT OF DATE, WILL UPDATE

Instructions to run the code:

If "ImportError: Matplotlib requires dateutil>=2.7; you have 2.6.1",
run ' pip install python-dateutil --force-reinstall --upgrade '.

bogoCoin1(p): is our original function to obtain a BOGO coin of easy p-value.

bogoCoin(p): is our improved function that can work for any p-value.

If you would like to switch which function is being used, you can change
line 60 to say "sum += bogoCoin1(p)".

The desired p value can be adjusted by changing p in our main function
on line 51.

Based on this, you will also need to change the title of the graph to say 
"P = 'new value' Histogram" on line 72. This 'new value' should match
the p value stated on line 51.

To adjust the number of fair coins per BOGO coin flip, you can adjust "numCoins"
on line 33.

Also, if you want to change the number of BOGO coin flips per sample you
can adjust the variable called "flips" on line 54.

Lastly, if you would like to change the number of samples taken for the
histogram, you can adjust the variable "samples" on line 55.
