# Snake
Machine learning project of creating the Snake AI using Q-learning
MACHINELEARNING
 NATALIA ALBARRÁN PEÑAS
 100498962
 FRANCISCO JIMENO FERNÁNDEZ
 100499080
 GROUP196
The aim of this project is to develop a machine learning algorithm which is capable of
 playing the snake game better than the algorithm of the first tutorial. The main tool for doing
 it is Q-learning. In this type of learning we have a table to store the different rewards for each
 action in each state. For implementing this technique we have followed the instructions of the
 different phases.
 PHASE1
 This phase consists in creating the functions that the agent will use to learn which are state,
 next state and the rewarding function as well as creating the functions we had to complete the
 code so it could be runned and the agent could start learning.
 STATE
 The first state function was implemented just returning the distance between the snake
 position and the food position but after just trying it a couple of times we realized we decided
 to change it completely.
 To implement the initial set of state we have implemented the function get state which
 calculates the state in function of the:----
Snake_pos: This is the position of the head of the snake which is in a list [x, y] too
 and is used as the reference part of the snake.
 Range: It is a variable that we have created that determines the range around the
 snake_pos that considers the presence of walls which is 10% of the frame size.
 Frames_size_x and frame_Size_y: They contain the frame size and are used to
 compute the range. Along the project we have changed these parameters to see which
 is the size that gives the best results.
 Ocup_dir: It is a list that contains 4 binary variables one for each possible direction.
 This value is computed with a function called occupation which receives as input the
 parameters above. Then it compares the position of the snake and the different
 obstacles, the limits of the board only for phase 2 and also the body for phase 3, and
 returns 1 if any direction is occupied and 0 if it is free.
 Direction: It shows the previous direction in order to take it as an occupied direction.
 This gave us in total a set of 18 states while combining the different combinations of the
 occupied directions.
 REWARDFUNCTION
 The reward function uses mainly the distance between the snake position and the food
 position to reward the agent. Let’s see how it works:
If the distance between the snake and the food increases it gives a negative reward of
 1.
If the distance decreases it gives a positive reward of 1 which leads the snake to the
 food by rewarding it positively.
We have also taken into account if the snake dies or if it eats a piece of food which is the
 main objective of the game so:--
 If the snake dies it has a negative reward of-10.
 If it eats a piece of food it will be rewarded with +10.
 The objective of this reward function is to take care of the distance between the food and the
 snake as it was thought in the first states but using new states that take more things into
 account.
PHASE2AND3
 STATE
 After training we realized that we had to rethink the initial state and reward function so we
 updated them mainly for the phase 3 as the growing body was a problem and we have taken
 into account these variables:------
 Food_pos: As the snake should move to the food and it has the position of the food in
 a list [x,y].
 Snake_pos: This is the position of the head of the snake which is in a list [x, y] too
 and is used as the reference part of the snake.
 Range: It is a variable that we have created that determines the range around the
 snake_pos that considers the presence of walls or the snake's body which is 10% of
 the frame size.
 Frames_size_x and frame_Size_y: They contain the frame size and are used to
 compute the range. Along the project we have changed these parameters to see which
 is the size that gives the best results.
 Ocup_dir: It is a list that contains 4 binary variables one for each possible direction.
 This value is computed with a function called occupation which receives as input the
 parameters above. Then it compares the position of the snake and the different
 obstacles, the limits of the board only for phase 2 and also the body for phase 3, and
 returns 1 if any direction is occupied and 0 if it is free.
 Snake_body: It contains all the bodies in a list and it is used in order to see if the
 blocks in the range of that direction are occupied by walls. This variable was used in
 phase 3 to take into account the body growing.
 Taking all these values we computed some initial states as it is explained in phase one. But
 after testing those states we realized that is not enough by taking into account the distance
 only in the reward, but it needs to be also in the states. Finally the combination that gave us
 the best results was computed in the following way: it first take into account the combination
 of the directions that are occupied and in function of the occupied directions and the relative
 position of the snake to the food (if the food is up right, down left…) it assigns a state from
 1-34, which are the following:
 1. Upandleft occupied, and the food is above-left.
 2. Upis occupied, and the food is above.
 3. Up, right occupied, and the food is above-right.
 4. Upis occupied, and the food is to the right.
 5. Upis occupied, and the food is to the left.
 6. Upis occupied, and the food is below-right.
 7. Upandleft occupied, and the food is below-left.
8. Upis occupied, and the food is below.
 9. Upis occupied, and the food is on the same x-axis.
 10. Right is occupied, and the food is above-right.
 11. Right is occupied, and the food is to the right.
 12. Right is occupied, and the food is below-right.
 13. Right is occupied, and the food is above.
 14. Right is occupied, and the food is below.
 15. Right is occupied, and the food is on the same y-axis.
 16. Down, left occupied, and the food is above-left.
 17. Down is occupied, and the food is above.
 18. Down, right occupied, and the food is above-right.
 19. Down is occupied, and the food is to the right.
 20. Down is occupied, and the food is to the left.
 21. Down is occupied, and the food is below-right.
 22. Down, left occupied, and the food is below-left.
 23. Down is occupied, and the food is below.
 24. Down is occupied, and the food is on the same x-axis.
 25. Left is occupied, and the food is above-left.
 26. Left is occupied, and the food is to the left.
 27. Left is occupied, and the food is below-left.
 28. Left is occupied, and the food is above.
 29. Left is occupied, and the food is below.
 30. Left is occupied, and the food is on the same y-axis.
 31. No valid move, and the food is above-left.
 32. No valid move, and the food is above-right.
 33. No valid move, and the food is below-left.
 34. No valid move, and the food is below-right.
 
 Each state is thought so in each there is usually an optimal action to take. To make the
 program learn which action is the optimal in each state we computed the reward function.
The function for getting the state, get_state(), in the different situations does not receive any
 input. Before starting to compute the different states it creates the range, the snake pos and
 calls the function occupation to compute the ocup_dir list. Then it starts an iterative process
 where it compares the position of the food and the head and also takes into account the
 directions of ocup_dir. As it has been mentioned above for phase 3 the ocup_dir also takes
 into account the body positions.
 We also have the function get_next_state(action). This function is exactly the same as the
 previous one but in this case we have the action as an input. This action is used to see which
 direction is going to take the snake and according to it increase the coordinates of it. For
 example if the direction is down, we add ten to the y-coordinate of the snake. Then with this
 new value for the snake_pos starts the same iterative process as in get_state().
 REWARDFUNCTION
 For the reward function we have stated that it takes into consideration 4 things:----
 Does it eat the food? If so it gives a positive reward of 1000. This event does not
 happen very often, so when it happens we want the program to learn that it is very
 good, that is why the reward is so high. What we used to implement this part of the
 code was to detect when the score was incrementing.
 Is the distance between the food and the snake reduced? If the distance between the
 previous state and now the distance is smaller it gives a positive reward of 100. In this
 case the snake has not eaten any food, so the situation is not as good as the previous
 one, but is close to the food, so it has made some improvement.
 If the distance between the food and the snake is augmented it gives a negative reward
 of-100. This is the opposite case, and that is why the reward is the same amount but
 with a negative sign.
 Does the snake movement lead to game over ? If the snake dies there is a negative
 reward of-1000. This is the worst case and in consequence it has the worst reward.
 We do not want the snake to die, so that is why we want to penalize very much a
 move that leads the game to end.
 As is explained in phase one, at the beginning we had other values for the reward. We
 realized that eating the food is much more important than dying, because that is the aim of the
 game and if we wanted the program to learn the optimal action, that action needed to have a
 much higher reward. As we increment the value for the eating the food reward, we
 incremented the other values in a similar way.
 Q-TABLE
 The function for updating the q-table is called update_q_table(state, action, reward,
 next_state). As can be seen it takes those inputs. The state and the action are used to know
where we are located in the q-table at that moment. The states are the rows and the actions
 the columns. Then the reward ,that it has been already computed, and the next state are used
 to update the values. The function starts by computing the maximum value of the actual
 q-table for the next state with the function computeValueFromQValues(next_state), and also
 the value for the current state and action. Then it updates the q-value taking into account the
 parameter alpha. This parameter penalices the current values. At the beginning of the training
 we set a high value of alpha because we wanted our q-table to update with the new values and
 onesthe values where more or less stable we changed it to a more normal value. Also each
 time we saved the table in a field.
 ACTIONS
 There are four possible actions, up (0) , down(1), left (2) and right(3). To choose the action in
 each iteration we created the function choose_action(state, allowed_actions). This function
 takes the current state and the allowed actions and chooses an action. The criteria for
 choosing is with the epsilon parameter. This value is used to find an equilibrium between
 explore and exploit. If a random value between zero and one is lower than epsilon, then the
 action is random. If not then the action is the higher value of the q-table for that state. Here
 we had a similar case than with the alpha. For the training phase we were interested in finding
 new movements, so we set a high value for this parameter.
 TRAININGANDTESTING
 Once we had all the functions ready we started with the phase of training. The aim of this
 phase is to get the best q-table as possible. Before starting the process we defined the number
 of episodes. This is the number of times that the snake is going to play. For a good training
 we need a high number of episodes. Then we also created a variable to store the total reward
 so we could see how the snake was doing.
 In each episode we enter into a loop that repeats until the snake dies. Inside this loop we set
 the state, with this state we compute the action and update the position of the snake and in
 case of need it the position of the food. Then we have an if condition in which we enter only
 if we are training. Inside this loop what we do is to compute the reward and update the
 q-table with the functions that we have already mentioned.
 It has already been explained how we have changed the values of alpha and epsilon, but
 another parameter that we have been changing is the frame size. At the beginning we started
 with a frame of 150 by 150. With these values we trained our snake and we obtained very
 good results. But then we decided to experiment with other sizes for the phase 3, as the body
 grows we thought that a bigger frame could be better. First we tested 200, 300 and 400 and all
 of them were very bad. But then we tried with 500 and we were very surprised to see that it
 worked very well for when the body was growing.
With this new discovery we decided to do the same with the case for when the body was nor
 growing. We thought that we had good results with 150, but then we tried with 300 and it was
 much better. Now we had much better results, almost the same as with 500 for when the body
 was growing.
 Once our q-table was trained it was time to test the model. For testing we just changed the
 epsilon to 0.1 and set training to false, so the q-table is not updated anymore, and we did that
 with both cases, phase 2 and phase 3. Is true that for some episodes we had bad results, but
 for most of them the results were very successful. In both cases the results were very similar
 to the ones of the training phase. After including the body in ocup_dir we tried it in the phase
 2 and realized that it improved a lot the agent so we decided to take into account the body in
 phase 2 too
CONCLUSION
 The main point of this assignment was the same as in the previous one: make an intelligent
 agent which eats as many pieces of food as possible but this time instead of using weka based
 on some training instances we have to create a model based on reinforcement learning using
 q-learning.
 The q-learning learning process consists of learning the actions based on different states of
 the game using exploration which is using random actions and exploitation which uses the
 action with the highest q-value. In this learning process is very important the state
 representation so you do not create a really concrete scenario but not a representation of
 states that shows a general scenario that the learned thing by the agent are not really useful.
 As we have mentioned in various points of the assignment we had some troubles deciding
 which set of sets was the optimal one. We tested several but most of them were very bad.
 This made us realize that a main part of this process is testing and learning from the errors.
 Another important thing in this kind of algorithm is the reward function which is the one in
 charge of assigning the q-values to the state in the function assigned to the different actions.
 In this part we had a similar problem than with the states but we learned that the eros could
 give us very useful information.
 We enjoyed this assignment more than the first one as in this one we could see how a
 machine learning process actually works and how applying different techniques and values
 for the variables such as epsilon, alpha and gamma can change the model completely. A very
 cool thing about this assignment was watching the snake evolving from luckily eating a piece
 of fruit to eating tens of them.
