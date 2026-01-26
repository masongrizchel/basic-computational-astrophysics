# Gravitational Waves & Deep Learning

## Overview
This module explores **Gravitational Wave Astronomy**, moving from electromagnetic signals to ripples in spacetime itself. We simulate the merger of two black holes—a Compact Binary Coalescence (CBC)—and train an Artificial Intelligence to detect these signals hidden within high-volume noise.

While LIGO/Virgo use Matched Filtering to detect these waves, we implement a data-driven approach using a **1D Convolutional Neural Network (1D-CNN)** to identify the characteristic "Chirp" signal directly from time-series strain data.

## The Physics: The "Chirp"
When two black holes spiral into each other, they emit gravitational radiation. As the orbit decays, the frequency and amplitude of the waves increase rapidly until the moment of merger.

### The Signal Model
We simulate the **Inspiral Phase** using the Newtonian Quadrupole approximation:
* **Frequency Evolution:** $f(t) \propto (t_c - t)^{-3/8}$ (The pitch sweeps up).
* **Amplitude Evolution:** $A(t) \propto (t_c - t)^{-1/4}$ (The volume gets louder).
* **The Noise:** We inject Gaussian white noise to mimic the strain sensitivity limits of detectors like LIGO ($SNR < 1.0$), making the signal invisible to the naked eye.

## The AI: 1D Convolutional Neural Networks
Unlike image recognition (2D-CNNs), audio and wave data require temporal pattern recognition. We utilize a **1D-CNN**, which slides a filter across the time axis to detect specific frequency shifts.

* **Input:** A 1D array of 2048 time steps (Strain).
* **Architecture:**
    * `Conv1D (Kernel=32)`: Detects broad wave patterns and oscillations.
    * `MaxPooling1D`: Downsamples to focus on strong activations.
    * `GlobalAveragePooling1D`: Summarizes the presence of a signal over the entire duration.
    * `Dense Output`: Binary classification (Signal vs. Noise).

## The Experiment
1.  **Data Generation:** We created a dataset of 4,000 samples.
    * 50% Pure Noise.
    * 50% Noise + Hidden Chirp (Randomized Signal-to-Noise Ratio).
2.  **Training:** The model trained to minimize `binary_crossentropy`.
3.  **Result:** The AI learned to act as a **Non-Linear Matched Filter**, achieving high accuracy (>95%) in detecting mergers even when the signal was buried beneath the noise floor.

## Dependencies
* `TensorFlow/Keras` (Conv1D layers)
* `NumPy` (Waveform generation and noise injection)
* `Matplotlib` (Visualization of strain data)
* `Scikit-Learn` (Train/Test splitting)

## 📊 Visuals
The notebook includes visualizations comparing:
* **The Theoretical Signal:** The clean "Chirp" waveform.
* **The Detector Input:** The noisy mess the AI actually sees.
* **Detections:** Successful identification of "invisible" signals.
