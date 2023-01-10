import random
import deap
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax",base.Fitness, weights=(1.0,))
creator.create("Individual",list,fitness=creator.FitnessMax)

toolbox = base.Toolbox()
