# 🌈 Module: Hydrogen Atom Spectroscopy

**Objective:** Simulate the quantum mechanical emission spectrum of Hydrogen using the Rydberg Formula.

## The Physics
This notebook models the discrete spectral lines emitted by a Hydrogen atom as electrons transition between energy levels. The wavelength $\lambda$ of the emitted photon is calculated using the **Rydberg Formula**:

$$\frac{1}{\lambda} = R_H \left( \frac{1}{n_{lower}^2} - \frac{1}{n_{upper}^2} \right)$$

* **$R_H$ (Rydberg Constant):** $1.097 \times 10^7 \, m^{-1}$
* **$n_{lower}$:** The final energy level (orbit).
* **$n_{upper}$:** The initial energy level ($n_{upper} > n_{lower}$).

## Spectral Series Simulated
The code calculates and visualizes the three primary series:
1.  **Lyman Series ($n_{lower}=1$):** Transitions to the ground state (Ultraviolet).
2.  **Balmer Series ($n_{lower}=2$):** Transitions to the first excited state (Visible Light).
3.  **Paschen Series ($n_{lower}=3$):** Transitions to the second excited state (Infrared).

## Contents
* `hydrogen_spectra.ipynb`: a series of Python (Jupyter notebooks) implementations calculating wavelengths and converting them to RGB colors for visualization.

## Key Skills Demonstrated
* **Quantum Mechanics:** Translating atomic transition rules into code.
* **Data Visualization:** Plotting emission spectra on a realistic wavelength scale.
* **Color Theory:** Mapping physical wavelengths (nm) to digital RGB values for accurate rendering.

## 📸 Visualization
The notebook generates a "digital spectrometer" view, showing the distinct "fingerprint" of Hydrogen that astronomers use to identify the element in distant stars.

---
*Part of the Basic Computational Astrophysics Series.*
