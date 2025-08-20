# 24f2009046@ds.study.iitm.ac.in

import marimo as mo

# Cell 1: Define a base variable and UI slider widget for interactivity
# Create a slider widget to interactively select a multiplier value
multiplier = mo.ui.slider(min=1, max=10, step=1, value=5)

# Base value for calculation
base_value = 10

# Cell 2: Compute a dependent variable based on slider input
# This cell depends on 'multiplier' from Cell 1
result = base_value * multiplier

# Cell 3: Display dynamic markdown output that updates with the slider
# Use mo.md() to render markdown dynamically
mo.md(f"""
### Computed Result

The base value is {base_value}.

The slider multiplier is currently {multiplier}.

The resulting value is **{result}**.
""")


