Hi Kristi,

I've tried to provide some feedback for both of your hypotheses/ideas. Overall, both are sweet! Nice work.

### IDEA 1

**Hypotheses:** The statement makes sense and seems like a reasonable hypothesis. However, when you formulate H_0 and H_1 I think you made a type w.r.t. the "<=" and ">". As it is, both null and alternative have an "=" in the definition, but only one can have the "=". It also may be worth being explicit about how you'll use averages in the H_0 and H_1 formulas.

**Data sufficency:** Seems like you should have everything you need with the standard citibike data pull.

**Data munging:** See IDEA 2 section - feedback is the same for both.

**Recommended statistical test:** Comparing averages between two different samples, and we don't know the standard deviation of the population --> sounds like a t-test.


### IDEA 2

**Hypotheses:** There seems to be some divergence between the initial statement of your hypothesis and how you actually formulate it. I would say that "the average time spent on citibikes" (weekday vs weekend) is an interesting question to answer, but it suggests that you'd be able to take into account that many commuters would do more than one trip in a day, and you would sum that up for each user. But in your formulation, you simplify to "average trip duration" - which is also a totally legitimate research question - just different from the one you introduced in the "idea".

**Data sufficency:** Again, for the hypothesis as you formulated it, you have all the data you need. If you were to explore the "average time spent on citibikes" question, then I think you'd need a unique identifer for the actual user themself... and of course citibike doesn't provide that (for anonymity reasons).

**Data munging:** 
- I think a few more comments inline to explain the trickier lines (eg. daily_summary['tripdurationsum'] = df2.tripduration.resample('D').sum()) would be useful for readability and for future-you.
- The steps you took to index 'df2' with a series of datetimes seemed a little bit roundabout... I think you could've skipped the steps around the 'test_times-duration' objects.
- Curious what the need for 'start_station_id' is. Maybe you're going to use it later in the analysis?
- I don't a lot about resampling - but I thought that the .resample() method was usually used on time-series columns in dataframes? Could you maybe use some combination of .groupby() and some aggregation methods instead?
- Finally, you'll probably do this in the next part of the analysis, but it would be cool to visualize the distributions within weekday vs. weekend  - and I guess that will require some pandas timeseries methods to extract a day of week?

**Recommended statistical test:** Same as above: Comparing averages between two different samples, and we don't know the standard deviation of the population --> sounds like a t-test.