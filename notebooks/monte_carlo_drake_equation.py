import numpy as np
import matplotlib.pyplot as plt

# --- 1. Simulation Parameters ---
num_simulations = 100000
print(f"Running {num_simulations} parallel universes...")

# --- 2. Define Probability Distributions for the 7 Factors ---

# R_star: Rate of star formation (stars per year)
# Well constrained by astrophysics. Normal distribution centered around 2.0 with a small variance.
R_star = np.random.normal(loc=2.0, scale=0.5, size=num_simulations)
R_star = np.clip(R_star, 0.5, 5.0) # Prevent negative or absurdly low/high star formation

# f_p: Fraction of stars with planets
# Highly constrained by Kepler data. Almost every star has planets.
f_p = np.random.normal(loc=0.8, scale=0.1, size=num_simulations)
f_p = np.clip(f_p, 0.1, 1.0)

# n_e: Number of habitable planets per system
# Somewhat constrained. Let's assume between 0.1 and 1.0.
n_e = np.random.uniform(low=0.1, high=1.0, size=num_simulations)

# f_l: Fraction where life emerges
# Unknown. Could be incredibly rare or nearly guaranteed if conditions are right.
# We use a uniform distribution to represent complete uncertainty between 1% and 100%
f_l = np.random.uniform(low=0.01, high=1.0, size=num_simulations)

# f_i: Fraction where intelligence emerges
# Unknown. Let's use a log-uniform distribution (can range from 1 in a million to 1 in 10).
f_i = 10 ** np.random.uniform(low=-4.0, high=-1.0, size=num_simulations)

# f_c: Fraction that develop communicative technology
# Let's assume if they are intelligent, they likely build radios eventually (10% to 50%)
f_c = np.random.uniform(low=0.1, high=0.5, size=num_simulations)

# L: Lifespan of the civilization (years)
# Highly uncertain. Could destroy themselves in 100 years, or last 100 million years.
# A log-normal distribution is perfect for this.
mean_L_log = np.log(10000) # Centered around 10,000 years
sigma_L_log = 1.5          # Wide spread
L = np.random.lognormal(mean=mean_L_log, sigma=sigma_L_log, size=num_simulations)

# --- 3. The Monte Carlo Execution ---
# Multiply the 100,000 samples element-wise
N = R_star * f_p * n_e * f_l * f_i * f_c * L

# --- 4. Statistical Analysis ---
median_N = np.median(N)
percentile_5 = np.percentile(N, 5)
percentile_95 = np.percentile(N, 95)

print("\n--- Monte Carlo Results ---")
print(f"Median number of civilizations (N): {median_N:.1f}")
print(f"90% Confidence Interval: Between {percentile_5:.1f} and {percentile_95:.1f} civilizations.")
print(f"Probability that we are entirely alone (N < 1): {(np.sum(N < 1) / num_simulations) * 100:.1f}%\n")

# --- 5. Visualization ---
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#111122')
ax.set_facecolor('#0b0c10')

# We use log bins because the results span many orders of magnitude
bins = np.logspace(np.log10(np.min(N[N>0])), np.log10(np.max(N)), 100)
ax.hist(N, bins=bins, color='cyan', edgecolor='black', alpha=0.7)

# Mark the statistical milestones
ax.axvline(median_N, color='lime', linestyle='dashed', linewidth=3, label=f'Median: ~{int(median_N)}')
ax.axvline(1.0, color='red', linestyle='solid', linewidth=2, label='N = 1 (We are alone)')
ax.axvspan(percentile_5, percentile_95, color='cyan', alpha=0.1, label='90% Confidence Interval')

ax.set_xscale('log')
ax.set_title("Monte Carlo Distribution of the Drake Equation", color='white', fontsize=16, pad=15)
ax.set_xlabel("Number of Civilizations (N) - Log Scale", color='white', fontsize=14)
ax.set_ylabel("Frequency (Number of Simulations)", color='white', fontsize=14)
ax.grid(True, linestyle=':', alpha=0.3, color='white')
ax.tick_params(colors='white')
ax.legend(loc='upper right', facecolor='#1f2833', edgecolor='white', labelcolor='white')

plt.tight_layout()
plt.show()