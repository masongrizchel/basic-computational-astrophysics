import numpy as np
import matplotlib.pyplot as plt

# --- 1. Astrophysical Constants (cgs units for standard astrophysics) ---
G = 6.674e-8           # Gravitational constant (cm^3 / g s^2)
c = 2.998e10           # Speed of light (cm/s)
sigma = 5.67e-5        # Stefan-Boltzmann constant (erg / cm^2 s K^4)
M_sun = 1.989e33       # Solar mass (g)
yr = 3.154e7           # Year in seconds

# --- 2. Black Hole Parameters ---
# Let's model a Quasar powered by a 100 Million Solar Mass Black Hole
M_bh = 1e8 * M_sun     

# Accretion rate: consuming 2 solar masses per year
M_dot = 2.0 * M_sun / yr 

# Calculate the Schwarzschild Radius (Event Horizon) and ISCO
R_s = (2.0 * G * M_bh) / c**2
R_isco = 3.0 * R_s  # Inner edge of the disk for a non-rotating BH

# --- 3. The Thermal Disk Engine ---
def disk_temperature(R, M, M_dot, R_in):
    """Calculates the temperature of a standard thin accretion disk at radius R."""
    # The temperature drops to 0 at exactly R_in due to the boundary condition,
    # peaks slightly further out, and then drops off as R^(-3/4)
    term1 = (3.0 * G * M * M_dot) / (8.0 * np.pi * sigma * R**3)
    term2 = 1.0 - np.sqrt(R_in / R)
    
    # Avoid negative values due to floating point precision exactly at R_in
    term2 = np.maximum(term2, 0.0) 
    
    T = (term1 * term2)**0.25
    return T

# Define a logarithmic array of radii from the inner edge out to 100x the ISCO
radii = np.logspace(np.log10(R_isco), np.log10(100 * R_isco), 500)
temperatures = disk_temperature(radii, M_bh, M_dot, R_isco)

print(f"Supermassive Black Hole Mass: 10^8 M_sun")
print(f"Peak Accretion Disk Temperature: {np.max(temperatures):.0f} Kelvin")

# --- 4. 2D Visual Mapping (Polar Coordinates) ---
# Create a 2D mesh to visualize the glowing disk from top-down
theta = np.linspace(0, 2 * np.pi, 200)
R_mesh, Theta_mesh = np.meshgrid(radii, theta)
T_mesh = disk_temperature(R_mesh, M_bh, M_dot, R_isco)

# Convert polar to cartesian for plotting the 2D visual
X = (R_mesh / R_isco) * np.cos(Theta_mesh)
Y = (R_mesh / R_isco) * np.sin(Theta_mesh)

# --- 5. Visualization ---
fig = plt.figure(figsize=(14, 6))
fig.patch.set_facecolor('#050505')

# Panel 1: Temperature vs Radius Plot
ax1 = fig.add_subplot(121)
ax1.set_facecolor('#0b0c10')
ax1.plot(radii / R_isco, temperatures, color='cyan', linewidth=3)
ax1.set_title("Accretion Disk Temperature Profile", color='white', fontsize=14)
ax1.set_xlabel("Radius (Multiples of $R_{isco}$)", color='white')
ax1.set_ylabel("Temperature (Kelvin)", color='white')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.grid(True, linestyle=':', alpha=0.3, color='white')
ax1.tick_params(colors='white')

# Highlight the peak
peak_idx = np.argmax(temperatures)
ax1.scatter(radii[peak_idx] / R_isco, temperatures[peak_idx], color='red', s=50, zorder=5)
ax1.text(radii[peak_idx] / R_isco * 1.2, temperatures[peak_idx], "Peak Emission\n(X-ray/UV)", color='red')

# Panel 2: Top-Down Visual of the Disk
ax2 = fig.add_subplot(122)
ax2.set_facecolor('#000000')

# Use a colormap that transitions from black -> red -> yellow -> white
# We apply a power-law norm to make the rapid temperature gradient visible
contour = ax2.pcolormesh(X, Y, T_mesh, shading='auto', cmap='hot', vmin=0, vmax=np.max(temperatures))

# Draw the Event Horizon (Black Hole Shadow)
circle = plt.Circle((0, 0), 1/3, color='black', zorder=10) # R_s is 1/3 of R_isco
ax2.add_patch(circle)

ax2.set_title("Top-Down Disk Visual", color='white', fontsize=14)
ax2.set_aspect('equal')
ax2.axis('off')

# Add colorbar
cbar = plt.colorbar(contour, ax=ax2, fraction=0.046, pad=0.04)
cbar.set_label('Temperature (K)', color='white')
cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white')

plt.tight_layout()
plt.show()