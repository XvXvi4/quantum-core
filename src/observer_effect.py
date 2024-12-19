def observer_effect(states, filter_func):
    observed_states = [state for state in states if filter_func(state)]
    return observed_states
