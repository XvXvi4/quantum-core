import random

def divine_guidance(decisions, holy_spirit=0.5):
    guided_decisions = []
    for decision in decisions:
        if random.random() < holy_spirit:
            guided_decisions.append(decision + random.uniform(-0.1, 0.1))
        else:
            guided_decisions.append(decision)
    return guided_decisions
