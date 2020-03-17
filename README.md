# CS260-hw3
Repository for Data Structures Course homework 3

Problem 1
Testing Done:
For this assignment we used timeit to test the timing on inserting 
100 to 900 elements, with increments of 100. The number of buckets will be input // 10.
We ran each of these tests 100 times each, dividing the total time by 100 to 
get the average. We then multiplied by 1000 to get the time in 10ths of a second. 
It must be noted that because we used a lambda function in the timeit
execution, there is some timing overhead, but it should be the same 
for every input and can be ignored in asymptotic analysis. As the inputs
are still quite small all things considered, the output does not show 
perfectly consistent growth.


Program Output:

Inserting:

input  |  timing (0.1s)  |  timing per elem. (0.1s)   
---------------------------------------------------   
100    |     0.54359     |         0.005436
200    |     1.06596     |         0.005330
300    |     0.83840     |         0.002795
400    |     1.40682     |         0.003517
500    |     1.83414     |         0.003668
600    |     2.21976     |         0.003700
700    |     2.30421     |         0.003292
800    |     2.69650     |         0.003371
900    |     2.89829     |         0.003220

Deleting:

input  |  timing (0.1s)  |  timing per elem. (0.1s)   
---------------------------------------------------   
100    |     0.47314     |         0.004731
200    |     1.00346     |         0.005017
300    |     1.60374     |         0.005346
400    |     1.90448     |         0.004761
500    |     2.38918     |         0.004778
600    |     2.92062     |         0.004868
700    |     3.19077     |         0.004558
800    |     3.36670     |         0.004208
900    |     3.88057     |         0.004312


Conclusion:
Although the timing seems to grow, that's because it's measured for the entire input size,
not only per element. The per element timing shows that it's pretty close to constant
(differences are partly on account of the runtime environment). The other reason there is a
difference is the constant, as was pointed out in the question, the runtime is O(1 + a) where
a is a constant. The constant is best described by n / b, where n is the number of elements,
and b is the number of buckets. This is because in an open hashtable, every bucket will have an
average of n / b elements. The hashing function will take you to the right bucket, and then you
run through the n / b elements in it to find the one to delete, or until the end for insertion
(O(n / b) time in both cases).


Problem 2
Testing Done:
Wran the insertion and deletion on datasets of size 100-900, inserting
or deleting 100 elements. In each insertion and deletion we counted the 
number of probes and summed them for that insertion or deletion. Dividing this final result
by 100 gives the average number of probes for an insertion or deletion in our example.
We also calculated a (# elements over # buckets). From there we calculated the expected 
values using the given formula and checked if they were close.

Program Output:

Inserting:
input  |  avg. number of probes  |   a   |  (1+1/(1-a)^2)/2      
-----------------------------------------------------------      
100    |           45            | 0.99  |     5000.50
200    |           45            | 0.49  |      2.46
300    |           45            | 0.33  |      1.61
400    |           45            | 0.25  |      1.38
500    |           45            | 0.20  |      1.28
600    |           44            | 0.17  |      1.22
700    |           45            | 0.14  |      1.18
800    |           45            | 0.12  |      1.15
900    |           45            | 0.11  |      1.13

Deleting:
input  |  avg. number of probes  |   a   |  (1+1/(1-a))/2        
-----------------------------------------------------------      
100    |            3            | 0.00  |      1.00
200    |           10            | 0.50  |      1.50
300    |            9            | 0.67  |      2.00
400    |           20            | 0.75  |      2.50
500    |           19            | 0.80  |      3.00
600    |           14            | 0.83  |      3.50
700    |           24            | 0.86  |      4.00
800    |           21            | 0.88  |      4.50
900    |           65            | 0.89  |      5.00


Conclusion:
Based on our understanding of the constant a, from problem 1,
a should be # elements / # buckets. But when we ran with this code,
a was nowhere near the average # of probes. Our results are wrong
for a. Also the value for the insertion into a 100 bucket list is wrong,
because it inserts 100 elements into 100 buckets and the formula breaks.