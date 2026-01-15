# Stellar Remnants Part 3: Time-Domain Astrophysics & LSTMs

## Overview
While previous modules focused on *spatial* detection (images of Einstein Rings), this notebook tackles **Time-Domain Astrophysics**. 

In the real world, most Black Holes are detected via **Gravitational Microlensing**—a transient brightening of a background star as a massive object passes in front of it. This project simulates these "Light Curves" and trains a **Long Short-Term Memory (LSTM)** Neural Network to distinguish rare Black Hole events from common variable stars.

## The Paczyński Curve
We simulate the magnification of a background source over time using the standard microlensing model derived by Bohdan Paczyński (1986).

### The Model
The brightness amplification $A(t)$ is governed by the normalized impact parameter $u(t)$:

$$u(t) = \sqrt{u_{min}^2 + \left( \frac{t - t_0}{t_E} \right)^2}$$

$$A(t) = \frac{u(t)^2 + 2}{u(t) \sqrt{u(t)^2 + 4}}$$

* **$t_E$ (Einstein Time):** The duration of the event (proportional to $\sqrt{Mass}$).
* **Signature:** A symmetric, achromatic "Shark Fin" peak that differs subtly from sinusoidal variable stars or random atmospheric noise.

## The AI: Recurrent Neural Networks (LSTM)
Standard Neural Networks (like the MLP used in Part 1) fail at this task because they treat data as a "bag of numbers" without order. We utilize an **LSTM (Long Short-Term Memory)** network, which is designed for sequential data.

* **Input:** A sequence of 100 flux measurements (Light Curve).
* **Memory:** The LSTM cell retains context from previous time steps to determine if a rise in brightness follows the specific *shape* of a lensing event.
* **Architecture:** `Input(100,1) -> LSTM(64) -> Dropout(0.2) -> Dense(32) -> Output(Sigmoid)`

## The "Needle in a Haystack" Experiment
Real astronomical surveys are highly imbalanced (millions of stars, very few black holes). We simulated this reality to stress-test the AI.

### The Challenge
* **Dataset:** 5,000 Light Curves.
* **Imbalance:** 99% Noise/Variable Stars, **1% Black Holes**.
* **The Trap:** A naive model can achieve 99% accuracy by simply guessing "No Black Hole" every time.

### The Solution
* **Class Weights:** We penalized the model heavily for missing a Black Hole during training.
* **Evaluation:** We moved beyond "Accuracy" to use a **Confusion Matrix**, focusing on **Precision** (avoiding false alarms) and **Recall** (catching every black hole).

## 🛠️ Dependencies
* `TensorFlow/Keras` (LSTM implementation)
* `NumPy` (Physics simulation)
* `Matplotlib` (Visualization of light curves)
* `Seaborn` (Heatmap for Confusion Matrix)
* `Scikit-Learn` (Metrics and Data Splitting)

## 📊 Results Summary
* **Clean Data:** The LSTM achieves >95% accuracy in distinguishing Paczyński curves from sine waves.
* **Noisy/Imbalanced Data:** The model successfully identifies rare events but exhibits a trade-off between False Positives and False Negatives, reflecting the real-world challenges of surveys like OGLE or MOA.

---
*Created via interaction with Gemini AI | Date: January 16, 2026*
