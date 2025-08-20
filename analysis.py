# 24f2009046@ds.study.iitm.ac.in

import marimo as mo

app = mo.App()

# ---------------------------
# Cell 1: Define base variable and interactive widget
# ---------------------------
@app.cell
def cell1():
    # Slider widget to select multiplier (1–10)
    multiplier = mo.ui.slider(start=1, stop=10, step=1, value=5, label="Multiplier")
    base_value = 10
    return multiplier, base_value

# ---------------------------
# Cell 2: Compute dependent variable
# ---------------------------
@app.cell
def cell2(multiplier, base_value):
    # Depends on multiplier (Cell 1), base_value (Cell 1)
    result = base_value * multiplier.value
    return result

# ---------------------------
# Cell 3: Display dynamic markdown
# ---------------------------
@app.cell
def cell3(multiplier, base_value, result):
    # This markdown updates whenever multiplier changes
    return mo.md(f"""
    ### Computed Result

    - Base value: **{base_value}**
    - Multiplier (from slider): **{multiplier.value}**
    - Result: **{result}**
    """)

if __name__ == "__main__":
    app.run()
