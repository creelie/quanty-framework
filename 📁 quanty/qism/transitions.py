"""
Abstract handlers for Topologically Transient transitions.
"""

def apply_tt_transition(state):
    """
    Apply a formal TT transition to a state.
    """
    state["tt_applied"] = True
    return state
