# Memes

# Description

"Dark times have come. Article 13 has been passed almost 2 years ago. Memes are illegal.
People use USB sticks to store and sell them for caps. Every meme is identified by a size,
given in MiB, and its market price. xXxDankScavengerxXx sells memes as his way of
earning a living. Help him by writing function calculate(usb_size, memes) that
calculates the best set of memes, so that he can sell the USB stick for the highest price.
"

# Explanation
To solve this task I used a dynamic programming.
When we use dynamic programming, we build a grid.
The rows of the grid are the items and the columns are USB memory.
We fill each cell of the grid. To fill blank we must count max value of the previous max cell vs
value from current item + value of the remaining space


# Installation 
In my solution i used Python 3.7.3

1. Clone the repository.
2. Install requrements.
   ```
   pip install requirements.txt
   ```
3. Run tests

```pytest -q tests.py```
