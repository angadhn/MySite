import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

# Wealth share estimates for different time periods
# Based on research by economists like Piketty, Saez, and Zucman

# Mid-19th century America (Thoreau's time, ~1850)
thoreau_era = {
    "top_1_percent": 0.20,  # ~20% of wealth (estimate based on historical trends)
    "next_9_percent": 0.30,  # ~30% of wealth
    "middle_40_percent": 0.35,  # ~35% of wealth
    "bottom_50_percent": 0.15   # ~15% of wealth
}

# Modern America (most recent estimates, ~2020)
modern_era = {
    "top_1_percent": 0.32,  # ~32.1% of wealth (Federal Reserve estimate)
    "next_9_percent": 0.38,  # ~37.7% of wealth
    "middle_40_percent": 0.28,  # ~27.9% of wealth
    "bottom_50_percent": 0.02   # ~2% of wealth
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

# Update the slave ownership data to match 1860 statistics
slaveholding_1860 = {
    "non_slaveholders": 76.1,    # 76.1%
    "slaves_1_9": 17.2,         # 17.2%
    "slaves_10_99": 6.6,        # 6.6%
    "slaves_over_100": 0.1      # 0.1%
}

# Distribution of slaves held
slave_distribution = {
    "no_slaves": {"families": 75, "slaves_held": 0},
    "slaves_1_6": {"families": 15, "slaves_held": 16},
    "slaves_7_39": {"families": 9, "slaves_held": 53},
    "slaves_40plus": {"families": 1, "slaves_held": 31}
}

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
            marker_color='rgb(0, 173, 181)'
        )
    )

    fig.add_trace(
        go.Bar(
            x=labels,
            y=modern_values,
            name='Modern Era (~2020)',
            marker_color='rgb(220, 20, 60)'
        )
    )

    fig.update_layout(
        template='plotly',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis={
            'title': {
                'text': 'Share of Total Wealth (%)',
                'font': {'size': 14}
            },
            'gridcolor': 'rgba(128,128,128,0.2)',
            'tickfont': {'size': 12}
        },
        xaxis={
            'tickfont': {'size': 12}
        },
        legend=dict(
            orientation="h",     
            yanchor="bottom",   
            y=1.02,            
            xanchor="center",
            x=0.5,
            font={'size': 12}
        ),
        margin=dict(
            l=50,    
            r=20,    
            t=80,    
            b=50     
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

def create_slave_ownership_plot():
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Data for slaveholding distribution
    labels = ['0', '1-9', '10-99', '100+']
    values = [
        slaveholding_1860['non_slaveholders'],
        slaveholding_1860['slaves_1_9'],
        slaveholding_1860['slaves_10_99'],
        slaveholding_1860['slaves_over_100']
    ]

    # First bar plot - Percentage of slaveholding families
    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            name="% of White Families",
            marker_color='rgb(0, 173, 181)',
            text=[f'{v:.1f}%' for v in values],
            textposition='auto',
        ),
        secondary_y=False
    )

    # Second bar plot - Distribution of slaves held
    slave_labels = ['0', '1-6', '7-39', '40+']
    slave_values = [
        slave_distribution['no_slaves']['slaves_held'],
        slave_distribution['slaves_1_6']['slaves_held'],
        slave_distribution['slaves_7_39']['slaves_held'],
        slave_distribution['slaves_40plus']['slaves_held']
    ]

    fig.add_trace(
        go.Bar(
            x=slave_labels,
            y=slave_values,
            name="% of Slaves Held",
            marker_color='rgb(220, 20, 60)',
            text=[f'{v:.1f}%' for v in slave_values],
            textposition='auto',
        ),
        secondary_y=True
    )

    fig.update_layout(
        template='plotly',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font={'size': 12}
        ),
        margin=dict(
            l=50,
            r=20,
            t=80,
            b=50
        ),
        barmode='group'  # Group bars side by side
    )

    # Update yaxis properties
    fig.update_yaxes(
        title_text="Percentage of White Families",
        title_font={'size': 14},
        tickfont={'size': 12},
        gridcolor='rgba(128,128,128,0.2)',
        range=[0, 100],
        secondary_y=False
    )

    # Update secondary yaxis properties
    fig.update_yaxes(
        title_text="Percentage of Total Slaves Held",
        title_font={'size': 14},
        tickfont={'size': 12},
        gridcolor='rgba(128,128,128,0.2)',
        range=[0, 100],
        secondary_y=True
    )

    # Update xaxis properties
    fig.update_xaxes(
        title_text="Number of Slaves Owned",
        title_font={'size': 14},
        tickfont={'size': 12}
    )

    config = {
        'responsive': True,
        'displayModeBar': False
    }

    fig.write_html(
        'assets/plots/slave_ownership.html',
        config=config,
        include_plotlyjs=True,
        full_html=False
    )

# Generate both plots
create_interactive_wealth_distribution_plot(thoreau_era, modern_era)
create_slave_ownership_plot()