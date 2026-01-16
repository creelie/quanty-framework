# Theory–Code Mapping for QuanTY

This document explains how the theoretical constructions in the QuanTY paper
map to the reference implementations in this repository.

---

## Appendix G: TT Algorithms

**Paper content**
- Detection criteria for Topologically Transient (TT) events
- Parametric dependence on Y
- Controlled transition operators

**Code**
- `quanty/tt/detection.py`
- `quanty/tt/transitions.py`
- `quanty/tt/recovery.py`

These modules implement the TT detection logic, state transition rules, and
recovery procedures described in Appendix G.

---

## Appendix H: Formal Correctness of TT Transitions

**Paper content**
- Continuation maps
- Invariance under TT transitions
- Polynomial complexity bounds

**Code**
- `quanty/floer/floer_complex.py`
- `quanty/floer/continuation_maps.py`
- `quanty/floer/grading.py`

These components encode the algebraic and homological structures used in the
correctness proofs of Appendix H.

---

## QISM Construction

**Paper content**
- Product symplectic manifolds
- Inner state geometry

**Code**
- `quanty/qism/qism_factory.py`
- `quanty/qism/symplectic_forms.py`
- `quanty/qism/product_manifolds.py`

---

## Numerical Experiments

**Paper content**
- Scaling with Y
- TT frequency analysis

**Code**
- `benchmarks/scaling_y.py`
- `benchmarks/tt_frequency.py`

---

## Remarks

The code is designed to mirror the logical structure of the paper rather than
optimize performance. Its primary role is validation, reproducibility, and
conceptual clarity.
