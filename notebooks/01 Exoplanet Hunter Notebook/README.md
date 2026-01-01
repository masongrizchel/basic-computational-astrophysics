# 🪐 Exoplanet Hunter: Radial Velocity Simulator

**Objective:** Recover the orbital parameters of an invisible planet using advanced signal processing and Bayesian inference on simulated telescope data.

## Overview
This module simulates the **Radial Velocity (Doppler) Method** used to detect "Hot Jupiters." It demonstrates a complete Data Science pipeline: from generating synthetic physical data to recovering "hidden" signals using industry-standard astrophysical algorithms.

## The Physics Model
The radial velocity $v_r$ of the host star is modeled as a sine wave:
$$v_r(t) = K \sin\left( \frac{2\pi t}{P} + \phi \right) + \text{noise}$$

* **$K$:** Velocity semi-amplitude (star's wobble speed).
* **$P$:** Orbital period.
* **$\phi$:** Orbital phase.

## Analysis Pipeline

### 1. Simulation & Noise Injection
We generate a "Ground Truth" orbit ($P \approx 4.2$ days, $K \approx 50$ m/s) and sample it sparsely (20 random nights) to mimic real observing schedules. Gaussian noise is added to simulate instrument limits.

### 2. Blind Signal Detection (Lomb-Scargle)
Before fitting a model, we must find the period.
* **Technique:** **Lomb-Scargle Periodogram**.
* **Purpose:** Detects periodic signals in unevenly sampled time-series data (where standard FFT fails).
* **Result:** Identifies the most likely orbital period peaks from the noisy data.

### 3. Parameter Estimation (Non-Linear Regression)
* **Technique:** `scipy.optimize.curve_fit`.
* **Purpose:** Minimizes the $\chi^2$ loss function to find the "best fit" orbit.
* **Metrics:** Evaluated using $R^2$ score and Reduced Chi-Squared ($\chi^2_\nu$) to check for overfitting.

### 4. Uncertainty Analysis (Bayesian Inference)
* **Technique:** **Markov Chain Monte Carlo (MCMC)** using `emcee`.
* **Purpose:** Explores the probability landscape to quantify uncertainties.
* **Result:** Generates a "Corner Plot" showing the posterior probability distributions for Mass and Period, providing scientific error bars (e.g., $P = 4.23 \pm 0.05$ days).

## Key Results & Plots
The notebook generates the following visualizations:
* **Radial Velocity Curve:** Theoretical model vs. Noisy observations.
* **Periodogram:** Power spectrum revealing the hidden signal frequency.
* **Residual Analysis:** Diagnostics to ensure the model captures the physics.
* **Corner Plot:** Joint probability distributions for the orbital parameters.

## Requirements
* `numpy` (Physics & Noise)
* `matplotlib` (Visualization)
* `scipy` (Optimization & Signal Processing)
* `emcee` (MCMC Sampling)
* `corner` (Bayesian Visualization)
