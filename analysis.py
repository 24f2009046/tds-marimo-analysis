# 24f2009046@ds.study.iitm.ac.in

# Cell 1: Define a base variable and UI slider widget for interactivity
import marimo as mo

# Create a slider widget to interactively select a multiplier value
multiplier = mo.ui.slider(min=1, max=10, step=1, value=5)

# Base value for calculation
base_value = 10

# Cell 2: Compute a dependent variable based on slider input
# This cell depends on 'multiplier' from Cell 1
result = base_value * multiplier

# Cell 3: Display dynamic markdown output that updates with the slider
# This markdown reflects the current value of 'result'
mo.markdown(f"### Computed Result\n\nThe current result of {base_value} multiplied by the slider value {multiplier} is **{result}**.")

