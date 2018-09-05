# CS-GO-Challenger-Stage-Predictor

When you're bored on a tuesday night what else is there to do besides build some shitty python script?

### How it works:
-Each team has a rating somewhat randomly assigned (explained more below)
-A random number is generated between 0 and the sum of the two teams ratings
-If the random number falls within 0 - team 1's rating then team 1 wins
-If it's greater than team 1's rating then team 2 wins
-3 wins to move on and 3 losses and the team is out
-Generates all 5 rounds


### Rating:
Rating was initially the rating 2.0 (HLTV) of each team multiplied by number of maps in big events
Unfortuantely not every team has played in big events.
I then would take LAN maps multiplied by rating 2.0 and divided by 2
Some team didn't even have enough LAN maps to display a rating so it was just randomly assigned
I adjusted the numbers slightly until they made sense

### Issues:
-It is possible for teams to play against each other twice if they meet in a later round
-I never implemented the Buchholz system which reseeds round 3-5


This was the very first time I ran the program and it generated these results:
!(https://github.com/jeffrohlman/CS-GO-Challenger-Stage-Predictor/blob/master/roundbyround.PNG)
!(https://github.com/jeffrohlman/CS-GO-Challenger-Stage-Predictor/blob/master/results.PNG)
!(https://github.com/jeffrohlman/CS-GO-Challenger-Stage-Predictor/blob/master/matches.PNG)
