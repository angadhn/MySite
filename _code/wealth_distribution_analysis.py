import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Wealth share estimates for different time periods
# Based on research by economists like Piketty, Saez, and Zucman

# Mid-19th century America (Thoreau's time, ~1850)
thoreau_era = {
    "top_1_percent": 0.25,  # ~25% of wealth
    "next_9_percent": 0.28,  # ~28% of wealth
    "middle_40_percent": 0.33,  # ~33% of wealth
    "bottom_50_percent": 0.14   # ~14% of wealth
}

# Modern America (most recent estimates, ~2020)
modern_era = {
    "top_1_percent": 0.35,  # ~35% of wealth
    "next_9_percent": 0.38,  # ~38% of wealth
    "middle_40_percent": 0.26,  # ~26% of wealth
    "bottom_50_percent": 0.01   # ~1% of wealth
}

# Calculate the concentration ratios
thoreau_concentration = thoreau_era["top_1_percent"] / thoreau_era["middle_40_percent"]
modern_concentration = modern_era["top_1_percent"] / modern_era["middle_40_percent"]

print("Wealth concentration comparison:")
print(f"Thoreau era - Top 1% wealth share: {thoreau_era['top_1_percent'] * 100:.1f}%")
print(f"Modern era - Top 1% wealth share: {modern_era['top_1_percent'] * 100:.1f}%")
print(f"Thoreau era - Middle 40% wealth share: {thoreau_era['middle_40_percent'] * 100:.1f}%")
print(f"Modern era - Middle 40% wealth share: {modern_era['middle_40_percent'] * 100:.1f}%")
print(f"Thoreau era - Concentration ratio (Top 1% / Middle 40%): {thoreau_concentration:.2f}")
print(f"Modern era - Concentration ratio (Top 1% / Middle 40%): {modern_concentration:.2f}")

# Slave ownership distribution in the South
southern_white_population = {
    "non_slaveholders": 0.75,  # ~75% owned no slaves
    "small_slaveholders": 0.24,  # ~24% owned between 1-19 slaves
    "large_slaveholders": 0.01   # ~1% owned 20+ slaves
}

print("\nSlavery in the antebellum South:")
print(f"Percentage of Southern white families owning no slaves: {southern_white_population['non_slaveholders'] * 100:.1f}%")
print(f"Percentage of Southern white families owning 1-19 slaves: {southern_white_population['small_slaveholders'] * 100:.1f}%")
print(f"Percentage of Southern white families owning 20+ slaves: {southern_white_population['large_slaveholders'] * 100:.1f}%")

# Economic composition of antebellum America
antebellum_economic_groups = {
    "wealthy_elites": 0.05,  # ~5% 
    "middle_class": 0.30,    # ~30% (merchants, small farmers, professionals, skilled workers)
    "working_class": 0.50,   # ~50% (laborers, tenant farmers, unskilled workers)
    "enslaved": 0.15         # ~15% of total population
}

print("\nEconomic composition of antebellum America (approximate):")
for group, percentage in antebellum_economic_groups.items():
    print(f"{group}: {percentage * 100:.1f}%")

# Additional factors in middle class comparison
print("\nAdditional factors in middle class comparison:")
additional_factors = [
    "Land availability in 1850s provided path to economic independence",
    "Lower wealth concentration among non-elites in 1850s",
    "Different definition of 'middle class' between eras",
    "Different types of assets (land vs financial instruments)"
]
for factor in additional_factors:
    print(f"- {factor}")

# Optional: Create visualization of wealth distribution comparison
def create_interactive_wealth_distribution_plot(thoreau_era, modern_era):
    labels = ['Top 1%', 'Next 9%', 'Middle 40%', 'Bottom 50%']
    thoreau_values = [
        thoreau_era['top_1_percent'] * 100, 
        thoreau_era['next_9_percent'] * 100,
        thoreau_era['middle_40_percent'] * 100,
        thoreau_era['bottom_50_percent'] * 100
    ]
    modern_values = [
        modern_era['top_1_percent'] * 100, 
        modern_era['next_9_percent'] * 100,
        modern_era['middle_40_percent'] * 100,
        modern_era['bottom_50_percent'] * 100
    ]

    fig = go.Figure(data=[
        go.Bar(name="Thoreau's Era (~1850)", x=labels, y=thoreau_values),
        go.Bar(name='Modern Era (~2020)', x=labels, y=modern_values)
    ])

    fig.update_layout(
        title='Wealth Distribution Comparison',
        yaxis_title='Share of Total Wealth (%)',
        barmode='group',
        height=500
    )

    # Save the plot as an HTML file
    fig.write_html('assets/plots/wealth_distribution.html')

# Create the interactive plot
create_interactive_wealth_distribution_plot(thoreau_era, modern_era) 