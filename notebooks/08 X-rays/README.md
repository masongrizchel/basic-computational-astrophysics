# Stellar Remnants Part 5: X-Ray Binaries & Unsupervised Learning

## Overview
The final module of the Stellar Remnant series focuses on **High-Energy Astrophysics**. We simulate **X-Ray Binaries (XRBs)**—systems where a Black Hole or Neutron Star accretes matter from a companion.

Unlike previous modules that used Supervised Learning (training on labeled data), this session utilizes **Unsupervised Learning** (K-Means and PCA). The goal is to let the AI independently "rediscover" the physical accretion states of a Black Hole without human guidance.

## The Physics: Accretion States
A Black Hole in outburst cycles through distinct spectral states, defined by two components:
1.  **The Accretion Disk (Soft State):** Thermal blackbody radiation from the spiraling gas ($kT \approx 1-2$ keV).
2.  **The Corona (Hard State):** Inverse Compton scattering creates a high-energy Power Law tail ($\Gamma \approx 1.5-2.0$).

The transition between these states creates a characteristic hysteresis loop known as the **Hardness-Intensity Diagram (HID)** or "Q-Diagram."

## The AI: Unsupervised Clustering & Manifold Learning
We feed raw spectral data (photon counts in 100 energy bins) into the algorithms.

### 1. K-Means Clustering
* **Input:** Normalized X-ray Spectra.
* **Task:** Group the data into $k=3$ natural clusters.
* **Result:** The AI successfully separates the data into **Hard**, **Soft**, and **Intermediate** states, matching physical ground truth.

### 2. Principal Component Analysis (PCA)
* **Task:** Dimensionality Reduction (Projecting 100D data to 2D).
* **Result:** The PCA projection automatically recovers the geometry of the accretion flow (the Q-curve), identifying the Spectral Slope and Disk Temperature as the primary drivers of variance.

## Dependencies
* `Scikit-Learn` (KMeans, PCA, StandardScaler)
* `NumPy` (Physics simulation of Blackbody + Power Law)
* `Matplotlib` (Visualization of Spectra and HID)

## Results Summary
* **Simulation:** Generated a realistic 300-day outburst cycle exhibiting spectral hysteresis.
* **Clustering:** K-Means achieved near-perfect separation of accretion states based purely on spectral shape.
* **Manifold:** PCA revealed that >95% of the spectral variance is explained by just two physical parameters (Temperature and Index).

---
*Created via interaction with Gemini AI | Date: January 23, 2026*
