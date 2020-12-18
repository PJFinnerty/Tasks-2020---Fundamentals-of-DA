# Peter Finnerty

# Tasks-2020-52446

## List of Tasks

### Task 1
#### October 5th, 2020: 
Write a Python function called counts that takes a list as
input and returns a dictionary of unique items in the list as keys and the number of
times each item appears as values. So, the input ['A', 'A', 'B', 'C', 'A']
should have output {'A': 3, 'B': 1, 'C': 1} . Your code should not depend
on any module from the standard library1 or otherwise. You should research
the task first and include a description with references of your algorithm in the
notebook.

### Task 2
#### 2. November 2nd, 2020:  Write a Python function called dicerolls that simulates rolling dice.

* Your function should take two parameters: the number of dice k and
the number of times to roll the dice n. The function should simulate randomly
rolling k dice n times, keeping track of each total face value. It should then return
a dictionary with the number of times each possible total face value occurred. 

* So, calling the function as diceroll(k=2, n=1000) should return a dictionary like:
{2:19,3:50,4:82,5:112,6:135,7:174,8:133,9:114,10:75,11:70,12:36}

* You can use any module from the Python standard library you wish and you should include a description with references of your algorithm in the notebook. By the standard library, we mean the modules and packages that come as standard with Python.
Anything built-in that can be used without an import statement can be used.

### Task 3
#### November 16th, 2020: Coin Flips

* The numpy.random.binomial function can be used to simulate flipping a coin with a 50/50 chance of heads or tails. Interestingly, if a
coin is flipped many times then the number of heads is well approximated by a
bell-shaped curve. For instance, if we flip a coin 100 times in a row the chance of
getting 50 heads is relatively high, the chances of getting 0 or 100 heads is relatively
low, and the chances of getting any other number of heads decreases as you move
away from 50 in either direction towards 0 or 100. 

* Write some python code that simulates flipping a coin 100 times. Then run this code 1,000 times, keeping track
of the number of heads in each of the 1,000 simulations. 

* Select an appropriate plot to depict the resulting list of 1,000 numbers, showing that it roughly follows a bell-shaped curve. 

* You should explain your work in a Markdown cell above the
code.

### Task 4
#### 4. November 30th, 2020: Simpson’s Paradox
Simpson’s Paradox is a well-known statistical paradox
where a trend evident in a number of groups reverses when the groups are combined
into one big data set. 

* Use numpy to create four data sets, each with an x array and a corresponding y array, to demonstrate Simpson’s paradox. 

* You might create your x arrays using numpy.linspace and create the y array for each x using notation like y = a * x + b where you choose the a and b for each x , y pair to demonstrate the paradox. 

* You might see the Wikipedia page for Simpson’s paradox for inspiration.



## References:

### Task 1

#### Information on Lists

1. https://www.w3schools.com/python/python_lists_access.asp

2. Image: https://blog.finxter.com/wp-content/uploads/2020/07/pythonlist-scaled.jpg

#### Information on Dictionaries:

3. https://www.geeksforgeeks.org/python-accessing-key-value-in-dictionary/

4. https://openbookproject.net/thinkcs/python/english3e/dictionaries.html#:~:text=Dictionaries%20are%20yet%20another%20kind,of%20a%20list%20or%20tuple.

5. https://artofproblemsolving.com/wiki/index.php/Dictionary#:~:text=In%20Python%20a%20dictionary%20is,key%20and%20its%20associated%20value.&text=Dictionaries%20themselves%20are%20mutable%2C%20so,and%20changed%20at%20any%20time.

6. https://www.w3schools.com/python/python_dictionaries.asp

7. Image: https://lh3.googleusercontent.com/proxy/f0wACWCqx-IqJhqsGrnR9aYh7PcWDhZE9_YwBD8XLjIU-2n2qy-xPMYHPbr5CgtkX51yQXRvOvsW27uPXvdLArp7EZMtudhoot1IRICtnf4

### Task 2

#### Information on Discrete and Binomial Distributions:

8. https://people.richland.edu/james/lecture/m113/binomial.html

9. https://www.investopedia.com/terms/d/discrete-distribution.asp#:~:text=A%20discrete%20distribution%20is%20a,%2C%202%2C%203...&text=Overall%2C%20the%20concepts%20of%20discrete,probability%20theory%20and%20statistical%20analysis.

10. https://magoosh.com/statistics/understanding-binomial-distribution/#:~:text=Lastly%2C%20the%20binomial%20distribution%20is,you%20cannot%20roll%20a%203.5.

#### Information on .zip() Function

11. https://realpython.com/python-zip-function/#:~:text=Python's%20zip()%20function%20is,%2C%20sets%2C%20and%20so%20on.

### Task 3

#### Information on Binomial Distribution

12. https://www.statisticshowto.com/probability-and-statistics/binomial-theorem/binomial-distribution-formula/

13. https://demonstrations.wolfram.com/BinomialDistributionViaCoinFlips/

#### Information on Bernoulli Distribution in Relation to Coin Flips

14. https://math.stackexchange.com/questions/838107/what-is-the-difference-and-relationship-between-the-binomial-and-bernoulli-distr



### Task 4

15. https://www.clinfo.eu/simpsons-paradox/

16. https://academic.oup.com/ije/article/40/3/780/746837

17. https://en.wikipedia.org/wiki/Simpson%27s_paradox#:~:text=Simpson's%20paradox%2C%20which%20also%20goes,when%20these%20groups%20are%20combined.

18. https://www.kdnuggets.com/2020/09/simpsons-paradox.html




