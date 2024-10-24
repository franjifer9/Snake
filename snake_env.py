"""
Snake Eater Environment
Made with PyGame
Last modification in April 2024 by José Luis Perán
Machine Learning Classes - University Carlos III of Madrid
"""
import math

import numpy as np
import random

class SnakeGameEnv:
    def __init__(self, frame_size_x=150, frame_size_y=150, growing_body=True):
        # Initializes the environment with default values
        self.frame_size_x = frame_size_x
        self.frame_size_y = frame_size_y
        self.growing_body = growing_body
        self.score = 0
        self.prev_score=0
        self.reset()

    def reset(self):
        # Resets the environment with default values
        self.snake_pos = [50, 50]
        self.snake_body = [[50, 50], [60, 50], [70, 50]]
        self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10, random.randrange(1, (self.frame_size_y // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False
        self.prevdistance = int()
        return self.get_state()

    def get_score(self):
        return self.score

    def step(self, action):
        # Implements the logic to change the snake's direction based on action
        # Update the snake's head position based on the direction
        # Check for collision with food, walls, or self
        # Update the score and reset food as necessary
        # Determine if the game is over
        self.prevdistance = math.sqrt(math.pow((self.get_food()[0] - self.get_snake_pos()[0]),2) +
                                      math.pow((self.get_food()[1] - self.get_snake_pos()[1]),2) )
        reward = self.calculate_reward()
        self.update_snake_position(action)
        self.update_food_position()
        state = self.get_state()
        #self.game_over = self.check_game_over()
        return state, reward

    def ocupation(self, snake_pos, body,range1,FRAME_SIZE_X, FRAME_SIZE_Y = 150):
        r_oc = 0
        l_oc = 0
        u_oc = 0
        d_oc = 0
        if ([snake_pos[0] + 10, snake_pos[1]] in body) or (snake_pos[0] + 10 >= FRAME_SIZE_X - 10):
            r_oc = 1
        # left
        if ([snake_pos[0] - 10, snake_pos[1]] in body) or (snake_pos[0] - 10 <= 0):
            l_oc = 1
        # up
        if ([snake_pos[0], snake_pos[1] - 10] in body) or (snake_pos[1] - 10 <= 0):
            u_oc = 1
        # down
        if ([snake_pos[0], snake_pos[1] + 10] in body) or (snake_pos[1] + 10 >= FRAME_SIZE_Y - 10):
            d_oc = 1
        return (r_oc,l_oc, u_oc,d_oc)

    def get_state(self):
        state = int()

        range = round(int(self.frame_size_x * 0.1) / 10) * 10
        snake_pos = [self.get_snake_pos()[0], self.get_snake_pos()[1] ]
        ocup_dir = self.ocupation(snake_pos, self.get_body(), range,
                                  self.frame_size_x, self.frame_size_y)
        food_pos = self.get_food()
        snake_pos = self.get_snake_pos()
        if food_pos[0] > snake_pos[0]:  # Food to the right
            if food_pos[1] < snake_pos[1]:  # Food above
                state = 19 if ocup_dir[2] == 1 and ocup_dir[0] == 1 else 20 if ocup_dir[0] == 1 else 22 if ocup_dir[
                                                                                                               2] == 1 else 21
            elif food_pos[1] > snake_pos[1]:  # Food below
                state = 23 if ocup_dir[3] == 1 and ocup_dir[0] == 1 else 24 if ocup_dir[0] == 1 else 26 if ocup_dir[
                                                                                                               3] == 1 else 25
            else:  # Food on the same y-axis
                state = 4 if ocup_dir[0] == 1 else 6 if ocup_dir[3] == 1 else 5 if ocup_dir[2] == 1 else 12
        elif food_pos[0] < snake_pos[0]:  # Food to the left
            if food_pos[1] < snake_pos[1]:  # Food above
                state = 27 if ocup_dir[2] == 1 and ocup_dir[1] == 1 else 28 if ocup_dir[1] == 1 else 30 if ocup_dir[
                                                                                                               2] == 1 else 29
            elif food_pos[1] > snake_pos[1]:  # Food below
                state = 31 if ocup_dir[3] == 1 and ocup_dir[1] == 1 else 32 if ocup_dir[1] == 1 else 34 if ocup_dir[
                                                                                                               3] == 1 else 33
            else:  # Food on the same y-axis
                state = 3 if ocup_dir[1] == 1 else 5 if ocup_dir[2] == 1 else 12 if ocup_dir[0] == 1 else 11
        else:  # Food on the same x-axis
            if food_pos[1] < snake_pos[1]:  # Food above
                state = 9 if ocup_dir[2] == 1 else 10 if ocup_dir[0] == 1 else 1 if ocup_dir[1] == 1 else 2
            elif food_pos[1] > snake_pos[1]:  # Food below
                state = 13 if ocup_dir[3] == 1 else 14 if ocup_dir[0] == 1 else 7 if ocup_dir[1] == 1 else 8
            else:  # Food at the same position as the snake
                state = 18 if ocup_dir[0] == 1 else 17 if ocup_dir[1] == 1 else 15 if ocup_dir[2] == 1 else 16

        return state

    def get_next_state(self, action):
        state = int()
        if (action == 0):
            x_axis = 0
            y_axis = -10
        elif (action == 1):
            x_axis = 0
            y_axis = 10
        elif (action == 2):
            x_axis = -10
            y_axis = 0
        else:
            x_axis = 10
            y_axis = 0

        range = round(int(self.frame_size_x * 0.1) / 10) * 10
        snake_pos = [self.get_snake_pos()[0] + x_axis, self.get_snake_pos()[1] + y_axis]
        ocup_dir = self.ocupation(snake_pos, self.get_body(), range,
                                  self.frame_size_x, self.frame_size_y)
        food_pos = self.get_food()
        snake_pos = self.get_snake_pos()
        if food_pos[0] > snake_pos[0]:  # Food to the right
            if food_pos[1] < snake_pos[1]:  # Food above
                state = 19 if ocup_dir[2] == 1 and ocup_dir[0] == 1 else 20 if ocup_dir[0] == 1 else 22 if ocup_dir[
                                                                                                               2] == 1 else 21
            elif food_pos[1] > snake_pos[1]:  # Food below
                state = 23 if ocup_dir[3] == 1 and ocup_dir[0] == 1 else 24 if ocup_dir[0] == 1 else 26 if ocup_dir[
                                                                                                               3] == 1 else 25
            else:  # Food on the same y-axis
                state = 4 if ocup_dir[0] == 1 else 6 if ocup_dir[3] == 1 else 5 if ocup_dir[2] == 1 else 12
        elif food_pos[0] < snake_pos[0]:  # Food to the left
            if food_pos[1] < snake_pos[1]:  # Food above
                state = 27 if ocup_dir[2] == 1 and ocup_dir[1] == 1 else 28 if ocup_dir[1] == 1 else 30 if ocup_dir[
                                                                                                               2] == 1 else 29
            elif food_pos[1] > snake_pos[1]:  # Food below
                state = 31 if ocup_dir[3] == 1 and ocup_dir[1] == 1 else 32 if ocup_dir[1] == 1 else 34 if ocup_dir[
                                                                                                               3] == 1 else 33
            else:  # Food on the same y-axis
                state = 3 if ocup_dir[1] == 1 else 5 if ocup_dir[2] == 1 else 12 if ocup_dir[0] == 1 else 11
        else:  # Food on the same x-axis
            if food_pos[1] < snake_pos[1]:  # Food above
                state = 9 if ocup_dir[2] == 1 else 10 if ocup_dir[0] == 1 else 1 if ocup_dir[1] == 1 else 2
            elif food_pos[1] > snake_pos[1]:  # Food below
                state = 13 if ocup_dir[3] == 1 else 14 if ocup_dir[0] == 1 else 7 if ocup_dir[1] == 1 else 8
            else:  # Food at the same position as the snake
                state = 18 if ocup_dir[0] == 1 else 17 if ocup_dir[1] == 1 else 15 if ocup_dir[2] == 1 else 16

        return state

    def get_body(self):
    	return self.snake_body

    def get_food(self):
    	return self.food_pos

    def get_snake_pos(self):
        return self.snake_pos

    def get_distance(self):
        return self.prevdistance

    def calculate_reward(self):
        actual_distance = math.sqrt(math.pow(self.get_food()[0] - self.get_snake_pos()[0],2)  + math.pow(self.get_food()[1] - self.get_snake_pos()[1],2))
        if self.score != self.prev_score:
            self.prevdistance = actual_distance
            self.prev_score = self.score
            return 1000 # Positive reward for eating food
        elif self.check_game_over():
            self.prevdistance = actual_distance
            return -1000 # Negative reward for collision
        elif self.get_distance() > actual_distance:
            self.prevdistance = actual_distance
            return 10 # Slight positive reward to encourage shortest path to food
        else:
            self.prevdistance = actual_distance
            return -10
        # Calculate and return the reward. Remember that you can provide possitive or negative reward.


    def check_game_over(self):
        # Return True if the game is over, else False
        if self.snake_pos[0] < 0 or self.snake_pos[0] > self.frame_size_x-10:
            return True
        if self.snake_pos[1] < 0 or self.snake_pos[1] > self.frame_size_y-10:
            return True
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                return True

        return False

    def update_snake_position(self, action):
        # Updates the snake's position based on the action
        # Map action to direction
        change_to = ''
        direction = self.direction
        if action == 0:
            change_to = 'UP'
        elif action == 1:
            change_to = 'DOWN'
        elif action == 2:
            change_to = 'LEFT'
        elif action == 3:
            change_to = 'RIGHT'

        # Move the snake
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            self.snake_pos[1] -= 10
        elif direction == 'DOWN':
            self.snake_pos[1] += 10
        elif direction == 'LEFT':
            self.snake_pos[0] -= 10
        elif direction == 'RIGHT':
            self.snake_pos[0] += 10

        self.direction = direction


        self.snake_body.insert(0, list(self.snake_pos))

        if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
            self.score += 10
            self.food_spawn = False
            # If the snake is not growing
            if not self.growing_body:
                self.snake_body.pop()
        else:
            self.snake_body.pop()

    def update_food_position(self):
        if not self.food_spawn:
            self.food_pos = [random.randrange(1, (self.frame_size_x//10)) * 10, random.randrange(1, (self.frame_size_x//10)) * 10]
        self.food_spawn = True



