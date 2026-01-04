# Stellar Remnants: Gravitational Lensing & AI Detection

## Overview
This project combines **Computational Astrophysics** and **Machine Learning** to study stellar remnants (specifically Black Holes). 

The notebook simulates the General Relativistic effect of **Gravitational Lensing**—where a massive object warps the light of background stars. We then treat this as a "Inverse Problem," training a Neural Network to detect invisible Black Holes and estimate their mass based solely on the distortion of background star fields.

## Key Features

### 1. The Physics (General Relativity)
* **Core Logic:** Implements Einstein's deflection formula to calculate how light bends around a massive object.
* **Simulation:** Generates a synthetic field of background stars and calculates their apparent displacement $\Delta \theta$ based on the position and mass of a foreground Black Hole.
* **Math:**
    $$\theta_E = \sqrt{\frac{4GM}{c^2} \frac{D_{ls}}{D_l D_s}}$$
    *(Simplified in code as a scaling factor proportional to Mass and $1/r^2$)*

### 2. Visualization
* **Dynamic Animation:** Renders a high-resolution GIF of a Black Hole transiting across a star cluster.
* **Visual Artifacts:** Accurately renders the "Einstein Ring" effect and the radial pushing of stars away from the event horizon.

### 3. AI Black Hole Detector (The Inverse Solver)
* **Objective:** Solve the inverse problem: *Given a distorted star map, can we recover the Mass and Position of the invisible Black Hole?*
* **Model:** A Multi-Layer Perceptron (MLP) Regressor built with `scikit-learn`.
* **Architecture:** Feed-forward Neural Network (Input: Star Displacements $\rightarrow$ Output: BH Mass & Location).
* **Performance:** Achieved $R^2 > 0.95$ on clean synthetic data.

### 4. Robustness & Noise Analysis
* **Simulation of Errors:** Injected Gaussian noise into star coordinates to simulate real-world telescope limitations (CCD noise, atmospheric turbulence).
* **Signal-to-Noise Ratio (SNR):** Analyzed the "tipping point" where the AI model fails to distinguish gravity from random noise.

## Dependencies
* **Python 3.x**
* **NumPy** (Vectorized physics calculations)
* **Matplotlib** (Static plotting and Animation)
* **Scikit-Learn** (Neural Network implementation and metrics)
* **Pandas** (Data handling)

## How to Run
1.  **Visualization:** Run the animation cell to generate `black_hole_lensing.gif`.
2.  **Data Generation:** Execute the `generate_synthetic_data` function to create thousands of lensing scenarios.
3.  **Training:** Run the `MLPRegressor` cell to train the AI on the synthetic data.
4.  **Testing:** Use the `generate_noisy_data` function to stress-test the model against simulated telescope noise.

## Future Work
* **Denoising:** Implementing a Denoising Autoencoder to clean noisy telescope data before analysis.
* **Deep Learning:** Transitioning to Convolutional Neural Networks (CNNs) to analyze raw images instead of coordinate lists.
* **Multi-Object Lensing:** Simulating binary black hole systems.

---
*Part of the Basic Computational Astrophysics Series*
