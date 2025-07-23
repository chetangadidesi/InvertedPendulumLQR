# Inverted Pendulum Simulation using Discrete-Time LQR
This project simulates the control of a classic inverted pendulum on a cart system using a Discrete-Time Linear Quadratic Regulator (LQR) in Python. The simulation demonstrates how optimal control techniques can be used to stabilize an inherently unstable system. The LQR controller calculates the optimal control input to keep the pendulum upright while minimizing a quadratic cost function.

# Features
- Accurate state-space modeling of the inverted pendulum system
- Real-time simulation and visualization using matplotlib
- Implementation of Discrete Algebraic Riccati Equation (DARE)
- LQR gain computation with performance metrics
- Customizable cost matrices (Q, R) and simulation parameters

# Background
The inverted pendulum is a benchmark problem in control theory, often used to evaluate control algorithms due to its instability and nonlinearity. This simulation uses a discretized linear state-space model and solves the DARE to obtain the optimal feedback gain K that minimizes the cost function:
```math
J = \sum_{k=0}^{\infty} \left( x_k^\top Q x_k + u_k^\top R u_k \right)
```

# Simulation
- The simulation runs in a loop until the defined sim_time is reached. At each time step:
- The LQR gain is computed using the current state.
- The new control input is applied.
- The next state is computed using the system matrices.
- A live plot visualizes the cart and pendulum motion.

# Inference
- The LQR controller is able to stabilize the pendulum in upright position from an initial perturbation.
- Real-time performance is sufficient for small time steps (~0.1s).
- Fine-tuning Q and R matrices allows prioritizing stabilization speed vs. control effort.

# Applications
- Control system design prototyping
- Benchmark for optimal control algorithms

