from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies import KerasPolicy, MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.training import interactive
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)

memorization = MemoizationPolicy(max_history=5)
keras = KerasPolicy(max_history=5, epochs=100, batch_size=50)

def online_trainer(interpreter,domain_file="domain.yml",training_data_file='data/stories.md'):
    
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")						  
    agent = Agent(domain_file,
                  policies=[memorization,keras],
                  interpreter=interpreter,
				  action_endpoint=action_endpoint)
    				  
    data = agent.load_data(training_data_file)			   
    agent.train(data)
    interactive.run_interactive_learning(agent, training_data_file)
    return agent

if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
    online_trainer(nlu_interpreter)
    