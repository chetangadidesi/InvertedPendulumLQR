import numpy as np
from controller import solve_DARE, dlqr, lqr_control
from model import get_model_matrix
from config import Q, R

def test_dare_solution_converges():
    A, B = get_model_matrix()
    P = solve_DARE(A, B, Q, R)
    assert P.shape == Q.shape, "P should match Q in dimensions"
    assert np.all(np.linalg.eigvals(P) >= 0), "P should be positive semi-definite"

def test_lqr_gain_shape():
    A, B = get_model_matrix()
    K, P, eigvals = dlqr(A, B, Q, R)
    assert K.shape == (1, 4), "LQR gain K should be 1x4"
    assert np.all(np.abs(eigvals) < 1), "Closed-loop eigenvalues should be inside unit circle"

def test_lqr_control_output():
    x = np.array([[1.0], [0.0], [0.1], [0.0]])
    u = lqr_control(x)
    assert u.shape == (1, 1), "Control input u should be 1x1"
