import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
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

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=labels,
            y=thoreau_values,
            name="Thoreau's Era (~1850)",
            marker_color='rgb(0, 173, 181)'  # Teal color
        )
    )

    fig.add_trace(
        go.Bar(
            x=labels,
            y=modern_values,
            name='Modern Era (~2020)',
            marker_color='rgb(220, 20, 60)'  # Crimson color
        )
    )

    fig.update_layout(
        template='plotly',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(
            l=50,    # left margin
            r=20,    # right margin
            t=80,    # top margin
            b=50     # bottom margin
        ),
        title=dict(
            text='Wealth Distribution Comparison',
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(size=18, color='#333333')
        ),
        yaxis=dict(
            title='Share of Total Wealth (%)',
            gridcolor='rgba(128,128,128,0.2)',
            tickfont=dict(size=12, color='#333333'),
            title_font=dict(size=14, color='#333333')
        ),
        xaxis=dict(
            tickfont=dict(size=12, color='#333333')
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=12, color='#333333')
        )
    )

    config = {
        'responsive': True,
        'displayModeBar': False
    }

    fig.write_html(
        'assets/plots/wealth_distribution.html',
        config=config,
        include_plotlyjs=True,
        full_html=False
    )

# Generate the plot
create_interactive_wealth_distribution_plot(thoreau_era, modern_era) 