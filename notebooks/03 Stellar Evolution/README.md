# 🌟 Module: Stellar Evolution & Cluster Age Prediction

**Objective:** Simulate the life cycle of a star cluster and train a Machine Learning model to determine its age.

## Overview
This module explores **Stellar Evolution** by simulating a population of 2,000 stars born simultaneously. It visualizes how massive stars evolve off the Main Sequence first, creating a "Turn-off Point" that acts as a cosmic clock. Finally, it demonstrates **Simulation-Based Inference (SBI)** by training a Random Forest Regressor to predict the age of a cluster based solely on its observed properties.

## The Physics Model
The simulation relies on stellar scaling relations, where a star's fate is determined entirely by its Mass ($M$):
* **Luminosity:** $L \propto M^{3.5}$ (Massive stars are exponentially brighter).
* **Temperature:** $T \propto M^{0.55}$ (Massive stars are hotter).
* **Lifetime:** $t \propto M^{-2.5}$ (Massive stars die young).

As time advances, stars exhaust their fuel and leave the Main Sequence:
* **< 8 Solar Masses:** Expand into **Red Giants**, then shed layers to become **White Dwarfs**.
* **> 8 Solar Masses:** Explode as **Supernovae** (leaving Neutron Stars/Black Holes).

## Key Features

### 1. The Hertzsprung-Russell (H-R) Animation
We generate a dynamic visualization of the cluster's history over 12 billion years.
* **Visual:** `stellar_evolution_hrd.gif`
* **Observation:** Watch the "Turn-off Point" slide down the diagonal sequence as the cluster ages.

### 2. Automated Age Dating (The "Cosmic Clock")
We implement an algorithmic estimator that calculates the cluster's age by identifying the heaviest star still on the Main Sequence ($M_{TO}$):
$$\text{Age} \approx 10^{10} \times (M_{TO})^{-2.5} \text{ years}$$

### 3. AI / Machine Learning Layer
We treat the physical simulation as a "Training Data Generator" for a Data Science problem.
* **Dataset:** Generated 1,000 synthetic clusters with random ages.
* **Model:** **Random Forest Regressor** (`sklearn.ensemble`).
* **Input Features:** Hottest surviving star, brightest surviving star, and mean temperature of the brightest 10%.
* **Result:** The AI successfully learned the physics of stellar death (R² Score > 0.95) and can accurately predict the age of unseen clusters without being explicitly programmed with the physics formulas.

## 📂 Files
* `2026-01-02-_03-Stellar-Evolution.ipynb`: The core notebook containing the `StarCluster` class, physics engine, and ML pipeline.
* `stellar_evolution_hrd.gif`: The generated animation of the H-R diagram.

## Requirements
* `numpy` (Physics engine)
* `matplotlib` (Animation & Plotting)
* `sklearn` (Random Forest Regression)
* `pandas` (Feature analysis)

---
*Part of the Basic Computational Astrophysics Series.*
