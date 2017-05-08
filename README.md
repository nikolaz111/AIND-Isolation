# Build a Game-playing Agent

## Results

### Heuristic 1

The first heuristic uses the improved score heuristic but also penalises positions in the board where the player is less
than 2 squares away from the border. As the movements allowed by the game are L shaped knight movements, the player
that gets closer to the border will have less available movements. As the farthest a player can move through an axis
with this kind of movement is 2 squares, then the heuristic will reduce the score of a play if the player gets close to
the border.

Attempt 1

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 16 to 4
  Match 2: ID_Improved vs   MM_Null   	Result: 18 to 2
  Match 3: ID_Improved vs   MM_Open   	Result: 13 to 7
  Match 4: ID_Improved vs MM_Improved 	Result: 11 to 9
  Match 5: ID_Improved vs   AB_Null   	Result: 13 to 7
  Match 6: ID_Improved vs   AB_Open   	Result: 12 to 8
  Match 7: ID_Improved vs AB_Improved 	Result: 7 to 13


Results:
----------
ID_Improved         64.29%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 17 to 3
  Match 2:   Student   vs   MM_Null   	Result: 15 to 5
  Match 3:   Student   vs   MM_Open   	Result: 12 to 8
  Match 4:   Student   vs MM_Improved 	Result: 12 to 8
  Match 5:   Student   vs   AB_Null   	Result: 15 to 5
  Match 6:   Student   vs   AB_Open   	Result: 15 to 5
  Match 7:   Student   vs AB_Improved 	Result: 12 to 8


Results:
----------
Student             70.00%
```

Attempt 2

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 14 to 6
  Match 2: ID_Improved vs   MM_Null   	Result: 16 to 4
  Match 3: ID_Improved vs   MM_Open   	Result: 15 to 5
  Match 4: ID_Improved vs MM_Improved 	Result: 11 to 9
  Match 5: ID_Improved vs   AB_Null   	Result: 13 to 7
  Match 6: ID_Improved vs   AB_Open   	Result: 11 to 9
  Match 7: ID_Improved vs AB_Improved 	Result: 11 to 9


Results:
----------
ID_Improved         65.00%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 16 to 4
  Match 2:   Student   vs   MM_Null   	Result: 15 to 5
  Match 3:   Student   vs   MM_Open   	Result: 16 to 4
  Match 4:   Student   vs MM_Improved 	Result: 14 to 6
  Match 5:   Student   vs   AB_Null   	Result: 13 to 7
  Match 6:   Student   vs   AB_Open   	Result: 15 to 5
  Match 7:   Student   vs AB_Improved 	Result: 11 to 9


Results:
----------
Student             71.43%
```

Attempt 3

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 13 to 7
  Match 2: ID_Improved vs   MM_Null   	Result: 16 to 4
  Match 3: ID_Improved vs   MM_Open   	Result: 10 to 10
  Match 4: ID_Improved vs MM_Improved 	Result: 14 to 6
  Match 5: ID_Improved vs   AB_Null   	Result: 12 to 8
  Match 6: ID_Improved vs   AB_Open   	Result: 10 to 10
  Match 7: ID_Improved vs AB_Improved 	Result: 16 to 4


Results:
----------
ID_Improved         65.00%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 16 to 4
  Match 2:   Student   vs   MM_Null   	Result: 16 to 4
  Match 3:   Student   vs   MM_Open   	Result: 12 to 8
  Match 4:   Student   vs MM_Improved 	Result: 12 to 8
  Match 5:   Student   vs   AB_Null   	Result: 14 to 6
  Match 6:   Student   vs   AB_Open   	Result: 13 to 7
  Match 7:   Student   vs AB_Improved 	Result: 11 to 9


Results:
----------
Student             67.14%
```



### Heuristic 2

The second heuristic uses the improved score heuristic but also gives points for positions in the board where the
opponent player is less than 2 squares away from the border. Here we use the same logic of being close to the border as
a bad thing because of the limitations of the L shaped movement, but this time we give points to branches that could
lead to the opponent being close to the border.

Attempt 1

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 15 to 5
  Match 2: ID_Improved vs   MM_Null   	Result: 14 to 6
  Match 3: ID_Improved vs   MM_Open   	Result: 11 to 9
  Match 4: ID_Improved vs MM_Improved 	Result: 13 to 7
  Match 5: ID_Improved vs   AB_Null   	Result: 14 to 6
  Match 6: ID_Improved vs   AB_Open   	Result: 11 to 9
  Match 7: ID_Improved vs AB_Improved 	Result: 12 to 8


Results:
----------
ID_Improved         64.29%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 13 to 7
  Match 2:   Student   vs   MM_Null   	Result: 19 to 1
  Match 3:   Student   vs   MM_Open   	Result: 12 to 8
  Match 4:   Student   vs MM_Improved 	Result: 11 to 9
  Match 5:   Student   vs   AB_Null   	Result: 16 to 4
  Match 6:   Student   vs   AB_Open   	Result: 14 to 6
  Match 7:   Student   vs AB_Improved 	Result: 10 to 10


Results:
----------
Student             67.86%
```

Attempt 2

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 17 to 3
  Match 2: ID_Improved vs   MM_Null   	Result: 15 to 5
  Match 3: ID_Improved vs   MM_Open   	Result: 15 to 5
  Match 4: ID_Improved vs MM_Improved 	Result: 14 to 6
  Match 5: ID_Improved vs   AB_Null   	Result: 16 to 4
  Match 6: ID_Improved vs   AB_Open   	Result: 13 to 7
  Match 7: ID_Improved vs AB_Improved 	Result: 13 to 7


Results:
----------
ID_Improved         73.57%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 19 to 1
  Match 2:   Student   vs   MM_Null   	Result: 13 to 7
  Match 3:   Student   vs   MM_Open   	Result: 15 to 5
  Match 4:   Student   vs MM_Improved 	Result: 15 to 5
  Match 5:   Student   vs   AB_Null   	Result: 17 to 3
  Match 6:   Student   vs   AB_Open   	Result: 14 to 6
  Match 7:   Student   vs AB_Improved 	Result: 13 to 7


Results:
----------
Student             75.71%
```

Attempt 3

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 17 to 3
  Match 2: ID_Improved vs   MM_Null   	Result: 10 to 10
  Match 3: ID_Improved vs   MM_Open   	Result: 10 to 10
  Match 4: ID_Improved vs MM_Improved 	Result: 10 to 10
  Match 5: ID_Improved vs   AB_Null   	Result: 12 to 8
  Match 6: ID_Improved vs   AB_Open   	Result: 13 to 7
  Match 7: ID_Improved vs AB_Improved 	Result: 10 to 10


Results:
----------
ID_Improved         58.57%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 17 to 3
  Match 2:   Student   vs   MM_Null   	Result: 14 to 6
  Match 3:   Student   vs   MM_Open   	Result: 12 to 8
  Match 4:   Student   vs MM_Improved 	Result: 14 to 6
  Match 5:   Student   vs   AB_Null   	Result: 14 to 6
  Match 6:   Student   vs   AB_Open   	Result: 12 to 8
  Match 7:   Student   vs AB_Improved 	Result: 12 to 8


Results:
----------
Student             67.86%
```

### Heuristic 3

The last heuristic is a combination of the two previous heuristics. Uses the improved score heuristic along with the
points given and taken away depending on how close to the border is the the player and the opponent player.

Attempt 1

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 18 to 2
  Match 2: ID_Improved vs   MM_Null   	Result: 17 to 3
  Match 3: ID_Improved vs   MM_Open   	Result: 14 to 6
  Match 4: ID_Improved vs MM_Improved 	Result: 15 to 5
  Match 5: ID_Improved vs   AB_Null   	Result: 15 to 5
  Match 6: ID_Improved vs   AB_Open   	Result: 13 to 7
  Match 7: ID_Improved vs AB_Improved 	Result: 14 to 6


Results:
----------
ID_Improved         75.71%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 15 to 5
  Match 2:   Student   vs   MM_Null   	Result: 16 to 4
  Match 3:   Student   vs   MM_Open   	Result: 15 to 5
  Match 4:   Student   vs MM_Improved 	Result: 13 to 7
  Match 5:   Student   vs   AB_Null   	Result: 14 to 6
  Match 6:   Student   vs   AB_Open   	Result: 14 to 6
  Match 7:   Student   vs AB_Improved 	Result: 12 to 8


Results:
----------
Student             70.71%
```

Attempt 2

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 17 to 3
  Match 2: ID_Improved vs   MM_Null   	Result: 15 to 5
  Match 3: ID_Improved vs   MM_Open   	Result: 13 to 7
  Match 4: ID_Improved vs MM_Improved 	Result: 13 to 7
  Match 5: ID_Improved vs   AB_Null   	Result: 14 to 6
  Match 6: ID_Improved vs   AB_Open   	Result: 14 to 6
  Match 7: ID_Improved vs AB_Improved 	Result: 13 to 7


Results:
----------
ID_Improved         70.71%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 17 to 3
  Match 2:   Student   vs   MM_Null   	Result: 16 to 4
  Match 3:   Student   vs   MM_Open   	Result: 12 to 8
  Match 4:   Student   vs MM_Improved 	Result: 14 to 6
  Match 5:   Student   vs   AB_Null   	Result: 15 to 5
  Match 6:   Student   vs   AB_Open   	Result: 13 to 7
  Match 7:   Student   vs AB_Improved 	Result: 12 to 8


Results:
----------
Student             70.71%
```

Attempt 3

```
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random    	Result: 15 to 5
  Match 2: ID_Improved vs   MM_Null   	Result: 17 to 3
  Match 3: ID_Improved vs   MM_Open   	Result: 13 to 7
  Match 4: ID_Improved vs MM_Improved 	Result: 13 to 7
  Match 5: ID_Improved vs   AB_Null   	Result: 16 to 4
  Match 6: ID_Improved vs   AB_Open   	Result: 13 to 7
  Match 7: ID_Improved vs AB_Improved 	Result: 10 to 10


Results:
----------
ID_Improved         69.29%

*************************
   Evaluating: Student   
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random    	Result: 15 to 5
  Match 2:   Student   vs   MM_Null   	Result: 16 to 4
  Match 3:   Student   vs   MM_Open   	Result: 16 to 4
  Match 4:   Student   vs MM_Improved 	Result: 13 to 7
  Match 5:   Student   vs   AB_Null   	Result: 17 to 3
  Match 6:   Student   vs   AB_Open   	Result: 14 to 6
  Match 7:   Student   vs AB_Improved 	Result: 14 to 6


Results:
----------
Student             75.00%
```

### Conclusions

The table below shows a summary of the results produced by the three heuristics.

![Heuristic comparison](heuristics_comparison.png)

As we can see in the results, all of the heuristics performed better than the ID_Improved heuristic although they rely
heavily in the improved score heuristic. The additional computations made on each of the heuristics do not represent a
lot of work to be made by the agent, so they don't add a burden to the calculation of the heuristic.

As the three heuristics are based on the improved score heuristic, we see that the results are not that different from
the improved score heuristic tests, but we can see that overall an improvement exists over the base heuristic. We see
that in average the last heuristic performed better than the others, including the improved score heuristic so the
recommendations would be to use the heuristic 3. The reasons for this are:

 * First of all, it is based on a already good heuristic that compares the available moves by the player. The results
 show there is not a big difference between the results of the improved score heuristic.
 * All the test for the third heuristic yielded a win  average above 70%, compared to the results for all other
 heuristics, this one had a better performance
 * If we look at the results of ID_Improved for the third heuristic, we see better results compared to the previous two
 heuristics, but still the last heuristic produces better results overall.

Because of this results, we should choose heuristic 3 over the other heuristics.
