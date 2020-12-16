import random
 
from bke import MLAgent, is_winner, opponent, RandomAgent, train, save, load, validate, plot_validation
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    
random.seed(1)
highest_validation = 0
highest_a = 0
highest_e = 0

for e in range(0,11):
    for a in range(0,11):
        my_agent = MyAgent(alpha=(a/10), epsilon=(e/10))
        random_agent = RandomAgent()
        train(
            agent=my_agent,
            iterations=5000)
        my_agent.learning = False
         
        validation_agent = RandomAgent()
         
        validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=1000)
        if validation_result["X"] > highest_validation:
            highest_validation = validation_result["X"]
            highest_a = a
            highest_e = e
 
print(validation_result)
print(highest_a)
print(highest_e)
save(my_agent, "MyAgent_3000")
