import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# --- 1. Simulation Parameters & Grid Setup ---
# We define a 2D grid representing a cross-section of the Sun's corona
x = np.linspace(-np.pi, np.pi, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

# Number of frames for our solar flare animation
frames = 100

# --- 2. The MHD Physics Engine ---

def calculate_fields(X, Y, t_fraction):
    """
    Calculates the Magnetic Vector Potential (A_z), the Magnetic Field (Bx, By),
    and the Current Density (J_z) at a specific time step.
    """
    # epsilon controls the size of the magnetic perturbation.
    # It grows from 0.0 (perfectly flat fields) to 0.8 (violent reconnection)
    epsilon = t_fraction * 0.8 
    
    # 1. Magnetic Vector Potential (A_z)
    # The first term creates the opposing flat fields (Current Sheet)
    # The second term introduces the tearing mode instability (growing islands)
    A_z = -np.log(np.cosh(Y)) + epsilon * np.cos(X) * np.exp(-Y**2)
    
    # 2. Magnetic Field Vectors (B = curl A)
    # Bx = d(A_z)/dy
    B_x = -np.tanh(Y) - 2 * Y * epsilon * np.cos(X) * np.exp(-Y**2)
    # By = -d(A_z)/dx
    B_y = epsilon * np.sin(X) * np.exp(-Y**2)
    
    # 3. Current Density (J = curl B)
    # J_z = d(B_y)/dx - d(B_x)/dy
    # This represents the intense electrical current trapped between the snapping fields
    dB_y_dx = epsilon * np.cos(X) * np.exp(-Y**2)
    dB_x_dy = -(1.0 / np.cosh(Y)**2) - 2 * epsilon * np.cos(X) * np.exp(-Y**2) * (1 - 2*Y**2)
    J_z = dB_y_dx - dB_x_dy
    
    return A_z, B_x, B_y, J_z

# --- 3. Animation Setup ---
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#050505')
ax.set_facecolor('#000000')

# We will plot the Current Density (J_z) as a glowing heatmap
# and overlay the Magnetic Field lines as contours
initial_Az, initial_Bx, initial_By, initial_Jz = calculate_fields(X, Y, 0.0)

# The heatmap background
heatmap = ax.imshow(initial_Jz, extent=[-np.pi, np.pi, -3, 3], origin='lower', 
                    cmap='magma', vmin=-1.0, vmax=2.5, interpolation='bilinear')

# The magnetic field lines
contour = ax.contour(X, Y, initial_Az, levels=15, colors='cyan', linewidths=1.5, alpha=0.8)

# Aesthetics
ax.set_title("MHD Simulation: Magnetic Reconnection (Solar Flare)", color='white', fontsize=15, pad=15)
ax.set_xlabel("X Position (Corona Surface)", color='white')
ax.set_ylabel("Y Position (Altitude)", color='white')
ax.tick_params(colors='white')
ax.set_xlim(-np.pi, np.pi)
ax.set_ylim(-3, 3)

time_text = ax.text(-3, 2.5, '', color='white', fontsize=12, fontweight='bold', fontfamily='monospace')

# --- 4. The Animation Engine ---
def update(frame):
    global contour
    
    # Time fraction goes from 0.0 to 1.0
    t_fraction = frame / float(frames - 1)
    
    # Recalculate physics for this time step
    A_z, B_x, B_y, J_z = calculate_fields(X, Y, t_fraction)
    
    # Update Heatmap (Current Density)
    heatmap.set_data(J_z)
    
    # Update Contours (Magnetic Field Lines)
    # Contours cannot be simply "set_data", they must be removed and redrawn
    for c in contour.collections:
        c.remove()
    contour = ax.contour(X, Y, A_z, levels=15, colors='cyan', linewidths=1.5, alpha=0.8)
    
    # Update Text
    if t_fraction < 0.2:
        status = "Stable Current Sheet"
    elif t_fraction < 0.7:
        status = "Tearing Mode Instability Growing"
    else:
        status = "MAGNETIC RECONNECTION! (Flare Emitted)"
        time_text.set_color('red')
        
    time_text.set_text(f"T={t_fraction:.2f} | Status: {status}")
    
    return [heatmap, time_text]

print("Simulating MHD Plasma physics... rendering frames.")
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=False)
plt.close(fig)

# Display the animation in Jupyter
HTML(ani.to_jshtml())