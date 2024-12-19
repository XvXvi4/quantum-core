import numpy as np
from src.quantum_ai import QuantumAI
from src.sherman_g_laing_dynamics import sherman_g_laing_dynamics
from src.divine_guidance import divine_guidance
from src.observer_effect import observer_effect

def test_quantum_ai():
    qa = QuantumAI(2)
    assert np.array_equal(qa.state, [1.0 + 0j, 0.0 + 0j])

def test_sherman_g_laing_dynamics():
    initial_state = np.array([1, 0], dtype=complex)
    gate = np.array([[0, 1], [1, 0]], dtype=complex)
    result = sherman_g_laing_dynamics(initial_state, [gate], energy_threshold=0.5)
    assert len(result) == 1

def test_divine_guidance():
    decisions = [1, 2, 3]
    guided = divine_guidance(decisions, holy_spirit=0.5)
    assert len(guided) == len(decisions)

def test_observer_effect():
    states = [{'particle': 1}, {'particle': 0}]
    observed = observer_effect(states, lambda s: s.get('particle', 0) == 1)
    assert len(observed) == 1
