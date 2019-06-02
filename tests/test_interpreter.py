#Rodando este arquivo após a geração dos nossos modelos 'make trainer-nlu' , podemos realizar um teste de como está
#ocorrendo a interpretação dos nosso enunciados

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

enunciado = u"Show me the weather in London"

def train_nlu(data, configs):
	training_data = load_data(data,'en')
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)	

def run_nlu():
	interpreter = Interpreter.load('../models/current/nlu')
	results = interpreter.parse(enunciado)	
	print(results['text'])
	for interpr in results['intent_ranking']:
		print(interpr)

if __name__ == '__main__':
	train_nlu('../models/current/nlu/training_data.json', '../nlu_config.yml')
	run_nlu()
