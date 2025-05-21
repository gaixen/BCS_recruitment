# Physics-Informed Neural Network: 2-Body Gravitational System

This notebook implements a **Physics-Informed Neural Network (PINN)** to predict the motion of two bodies under Newtonian gravitation — *without using traditional numerical solvers during inference*. It trains the model using both data and physical laws.
## Structure
### Sections in Notebook:
1. **Dependencies Installation**
2. **User Inputs**
   - Masses `m1`, `m2`
   - Initial positions and velocities
   - Prediction time `T`
3. **Training Data Generation**
   - Simulated using `solve_ivp` (ODE solver)
4. **Model Definition**
   - Neural network to map `t → [x1, x2]`
5. **Loss Function**
   - Combines data loss with ODE residuals
6. **Training Loop**
7. **Unseen Test Dataset**
   - Generated with different initial conditions
   - Kept fully unseen during training
8. **Evaluation**
   - MAE between predicted and true orbits
   - Optionally plots trajectories
## Key Concepts
- **PINN**: Neural net trained to satisfy known physical laws.
- **ODE Loss**: Penalizes network outputs if they deviate from Newton’s graviational law.
- **Data Loss**: Penalizes mismatch with synthetic training data.
- **Generalization**: Test set ensures performance is evaluated on unseen physical scenarios.
## Metrics
- *MAE (Mean Absolute Error)* on position predictions
- *Mean ODE residual* on test set
##  Evaluation
| Metric      | MAE x1  | MAE x2  |
|-------------|---------|---------|
| Accuracy    |`0.00556`|`0.00333`|
## Descripton
- Ground truth is generated using `scipy.integrate.solve_ivp`.
- all time inputs are continuous (float-based).
- You can customize the no. of time points
- Test data is strictly separated and never seen during training.
## Usage
1. Open `demo-solution.ipynb`
2. Run each cell in order.
3. View final model performance on unseen test data.
4. unseen test data is commented in the notebook
## Requirements

- Python 3.8+
- `torch`, `numpy`, `scipy`, `matplotlib`, `pandas`
Install using:
```bash
pip install torch numpy scipy matplotlib pandas

