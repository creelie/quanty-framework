"""
Invariant tracking utilities.

Used to verify invariant preservation across TT transitions.
"""

def track_invariants(state):
    return state.get("invariants", {})
