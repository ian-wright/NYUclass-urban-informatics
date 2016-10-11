## Cikibike Null Hypothesis project review

Great work! it is an original and interesting question, properly formulated Null, very good data munging, and good coding style.


The data has to be moved into the PUIDATA directory; data should not be kept in the same directory as code, and for the class it has to be stored in PUIDATA so that we avoiding having multiple copies of redundant data as we grade 90 notebooks. so you should not get data from the puidata dir, which is your own so it only hosts data you downloaded in it, but put your data in that dir (so when we run it goes into our own $PUIDATA). If it is still not clear please do ask me what I mean.

On the formulation of the question, the one objection I have is that you did not define what is a "similar" non-boudary zone; what features did you use (algoritmically or intellectually) to judge what constitutes a "similar" station to the boundary ones? (e.g. socioechonomic, traffic, docks density...)

The data supports the question, and now that you have two distributions you can easily compare them with a test of means (e.g. t-test)
