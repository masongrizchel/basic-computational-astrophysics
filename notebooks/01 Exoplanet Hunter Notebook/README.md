# 🪐 Exoplanet Hunter: Radial Velocity Simulator

**Objective:** Recover the orbital parameters of an invisible planet using `scipy.optimize` on simulated noisy telescope data.

## Overview
This module simulates the **Radial Velocity (Doppler) Method** used to detect "Hot Jupiters." It demonstrates the complete data science pipeline: generating synthetic physical data, adding realistic instrument noise, and using non-linear regression to "learn" the planet's properties.

## The Physics Model
The radial velocity $v_r$ of the host star is modeled as a sine wave:
$$v_r(t) = K \sin\left( \frac{2\pi t}{P} + \phi \right) + \text{noise}$$

* **$K$:** Velocity semi-amplitude (star's wobble speed).
* **$P$:** Orbital period.
* **$\phi$:** Orbital phase.

## Workflow
1.  **Simulation:** Generate "Ground Truth" orbit for a star with a generic Hot Jupiter ($P \approx 4$ days, $K \approx 50$ m/s).
2.  **Noise Injection:** Add Gaussian noise ($\sigma = 10$ m/s) to mimic imperfect telescope observations.
3.  **Model Fitting:** Use `scipy.optimize.curve_fit` to minimize the loss function and recover parameters $K$ and $P$.
4.  **Evaluation:** Validate the model using **Residual Analysis** and **Reduced Chi-Squared ($\chi^2_\nu$)**.

## Key Results
The notebook outputs a dashboard comparing the "True" vs. "Learned" parameters, including:
* **$R^2$ Score:** Measures variance explained by the model.
* **$\chi^2_\nu$:** Checks if the model fits the data within statistical noise limits (Target $\approx 1.0$).

## Requirements
* `numpy` (Physics & Noise)
* `matplotlib` (Visualization)
* `scipy` (Optimization/Regression)
* `sklearn` (Metrics)
