import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

# Create directories if they don't exist
os.makedirs('assets', exist_ok=True)

# Set style for a dark, sleek aesthetic
plt.style.use('dark_background')

# Generate synthetic data for an ML training curve
epochs = np.arange(1, 101)
# Simulated training loss: exponential decay with noise
train_loss = 2.5 * np.exp(-epochs/20) + 0.1 + np.random.normal(0, 0.02, len(epochs))
# Simulated validation loss: follows training but plateaus/overfits slightly
val_loss = 2.4 * np.exp(-epochs/22) + 0.15 + np.random.normal(0, 0.025, len(epochs))
val_loss[60:] += (epochs[60:] - 60) * 0.005 # simulate slight overfitting later on

# Create the plot
fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor('#0B0F19')
ax.set_facecolor('#0B0F19')

# Plot lines with neon colors
ax.plot(epochs, train_loss, label='Training Loss', color='#00D2FF', linewidth=2.5, alpha=0.9)
ax.plot(epochs, val_loss, label='Validation Loss', color='#FF007F', linewidth=2.5, alpha=0.9)

# Customize grid, axes, and labels
ax.grid(color='#1A233A', linestyle='--', linewidth=1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#273759')
ax.spines['left'].set_color('#273759')
ax.tick_params(colors='#8A9CC0')

# Titles and labels
ax.set_title('Live Model Performance (Simulated)', color='#FFFFFF', fontsize=16, pad=20, fontname='sans-serif', fontweight='bold')
ax.set_xlabel('Epochs', color='#8A9CC0', fontsize=12)
ax.set_ylabel('Loss', color='#8A9CC0', fontsize=12)

# Legend
legend = ax.legend(loc='upper right', facecolor='#1A233A', edgecolor='#273759', fontsize=11)
for text in legend.get_texts():
    text.set_color('#FFFFFF')

# Add a text watermark/timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
plt.figtext(0.95, 0.02, f"Last Updated: {timestamp}", ha="right", fontsize=9, color='#8A9CC0', alpha=0.7)

plt.tight_layout()
plt.savefig('assets/live_chart.png', dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Chart generated successfully at assets/live_chart.png")
