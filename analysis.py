# 24f2009046@ds.study.iitm.ac.in

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt

# Cell 1: Define input data and parameters
# These variables will be used in other cells for analysis
x = np.linspace(0, 10, 100)
freq_slider = mo.ui.slider(label="Frequency", min=1, max=10, value=5)

# Cell 2: Compute dependent variable y based on x and frequency slider
# y depends on x and freq_slider.value, it will update reactively when freq_slider changes
y = np.sin(freq_slider.value * x)

# Cell 3: Plot showing the relationship between variables x and y
# The title depends on freq_slider.value and will update when it changes
plt.plot(x, y)
plt.title(f"Sine wave with frequency = {freq_slider.value}")
plt.xlabel("x")
plt.ylabel("sin(freq * x)")
plt.grid(True)
plt.show()

# Cell 4: Dynamic markdown output showing current frequency value
# This cell depends on freq_slider.value and will update reactively
mo.markdown(f"### Current frequency value: **{freq_slider.value}**")
