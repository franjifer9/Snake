"""
Snake Eater Q learning basic algorithm
Made with PyGame
Last modification in April 2024 by José Luis Perán
Machine Learning Classes - University Carlos III of Madrid
"""
import numpy as np
import random
import json
import time


class QLearning:
    def __init__(self, n_states, n_actions, alpha=0.5, gamma=0.5, epsilon=0.5, epsilon_min=0.01,
                 epsilon_decay=0.95):
        self.n_states = n_states
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.load_q_table()

    def get_qtable(self):
        return self.q_table

    def set_to_0 (self, num_states, num_actions):
        self.q_table= np.zeros((num_states, num_actions))

    def choose_action(self, state, allowed_actions):
        if np.random.uniform(0, 1) < self.epsilon:
            action = random.choice(allowed_actions)  # Explore
        else:
            # Exploit
            q_values = self.q_table[state]
            max_q = np.max(q_values)
            best_actions = [allowed_actions[i] for i in range(len(allowed_actions)) if q_values[i] == max_q]
            action = random.choice(best_actions)

        self.epsilon = max(self.epsilon_min, self.epsilon_decay * self.epsilon)
        return action




    def getQValue(self, state, action):
        return self.q_table[state][action]

    def computeValueFromQValues(self, state):
        return max(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        current_q_value = self.getQValue(state, action)
        """if self.getQValue(state, action) != 0:
            updated_q_value = (1 - self.alpha) * current_q_value + self.alpha * (reward + 0)
        else:"""
        max_next_q_value = self.computeValueFromQValues(next_state)
        updated_q_value = (1 - self.alpha) * current_q_value + self.alpha * (
                reward + self.gamma * max_next_q_value)
        self.q_table[state][action] = updated_q_value
        # Update the current Q-value using the Q-learning formula

    def save_q_table(self, filename="q_table.txt"):
        np.savetxt(filename, self.q_table)

    def load_q_table(self, filename="q_table.txt"):
        try:
            self.q_table = np.loadtxt(filename)
        except IOError:
            # If the file doesn't exist, initialize Q-table with zeros as per dimensions
            self.q_table = np.zeros((self.n_states, self.n_actions))
