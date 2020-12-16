import random
 
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot, load, save, validate, plot_validation
 
 
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

my_agent = MyAgent(alpha=(0.03), epsilon=(0.5))


random_agent = RandomAgent()
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=90,
    trainings=100,
    validations=1000)

my_agent.learning = False
save(my_agent, "MyAgentHoogsteRating")


validation_agent = RandomAgent()

validation_result= validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
plot_validation(validation_result)


