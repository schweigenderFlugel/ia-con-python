import termcolor

from logic import *

batmobil = Symbol('batimovil')
joker = Symbol('joker')
pinguin = Symbol('pinguino')

# Operaciones lógicas
# And()
# Or()
# Implication()
# Biconditional()
# Not()

knowledge_base = And(
    Implication(Not(batmobil), joker),
    Or(joker, pinguin),
    Not(And(joker, pinguin))
)

print(model_check(knowledge_base, pinguin))

# Resolución de la actividad
knight = Symbol('Caballero')  # they allways say the truth
knave = Symbol('Bribon')  # they are payhological liars
types = [knight, knave]

subjectA = Symbol('Sujeto A')
subjectB = Symbol('Sujeto B')
subjectC = Symbol('Sujeto C')
subjects = [subjectA, subjectB, subjectC]

truths = Symbol('Dice la verdad')
lies = Symbol('Miente')
says = [truths, lies]

symbols = subjects + types + says

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f'{symbol}: Sí', "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f'{symbol}: Tal vez')

first_scenario = And(
    subjectA,
    And(subjectA, And(knight, knave)),
    Implication(subjectA, And(truths, lies))
)

second_scenario = And(
    And(subjectA, knave), 
    And(subjectB, knave), 
    Implication(And(subjectA, subjectB), lies),
)

second_scenario.add(
    Not(subjectB),
)

third_scenario = And(

)

check_knowledge(second_scenario)