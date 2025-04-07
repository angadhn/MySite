import plotly.graph_objects as go
import numpy as np

# Shared space station data
SPACE_STATIONS = [
    # Real historical stations
    {'name': 'Salyut-1', 'total_volume': 214, 'pressurised_volume': 99, 'habitable_volume': 90, 'crew': 3, 'is_real': True, 'is_planned': False, 'has_gravity': False},
    {'name': 'Skylab', 'total_volume': 499, 'pressurised_volume': 351.6, 'habitable_volume': 270, 'crew': 3, 'is_real': True, 'is_planned': False, 'has_gravity': False},
    {'name': 'Tiangong', 'total_volume': 726.6 , 'pressurised_volume': 340, 'habitable_volume': 121, 'crew': 3, 'is_real': True, 'is_planned': False, 'has_gravity': False},
    {'name': 'ISS', 'total_volume': 1200, 'pressurised_volume': 1005, 'habitable_volume': 388, 'crew': 10, 'is_real': True, 'is_planned': False, 'has_gravity': False},
    
    # Planned station
    {'name': 'Lunar Gateway', 'total_volume': 183, 'pressurised_volume': 183, 'habitable_volume': 125, 'crew': 4, 'is_real': False, 'is_planned': True, 'has_gravity': False},
    
    # Conceptual designs
    {'name': 'von Braun', 'total_volume': 6217.85, 'pressurised_volume': 4800, 'habitable_volume': 3600, 'crew': 65, 'is_real': False, 'is_planned': False, 'has_gravity': True},
    # {'name': 'Space Base', 'total_volume': 1274325, 'pressurised_volume': 980000, 'crew': 87.5, 'is_real': False, 'is_planned': False, 'has_gravity': True},
    {'name': 'Hexagonal Station', 'total_volume': 1274.3, 'pressurised_volume': 980, 'habitable_volume': 980, 'crew': 36, 'is_real': False, 'is_planned': False, 'has_gravity': True}
]

def get_station_colors(data):
    """Helper function to get colors based on station type"""
    colors = []
    for station in data:
        if station['is_real']:
            colors.append('#FF5252')  # Red for real stations
        elif station['is_planned']:
            colors.append('#FFAB40')  # Orange for planned stations
        else:
            colors.append('#2979FF')  # Blue for conceptual stations
    return colors

def create_space_station_plot():
    # Extract data for plotting
    names = [station['name'] for station in SPACE_STATIONS]
    volumes = [station['total_volume'] for station in SPACE_STATIONS]
    crews = [station['crew'] for station in SPACE_STATIONS]
    colors = get_station_colors(SPACE_STATIONS)
    
    # Calculate marker sizes (log scale for better visualization)
    marker_sizes = [np.log10(vol) * 10 for vol in volumes]
    
    # Calculate min and max values for axis ranges
    x_min = min(volumes) * 0.8
    x_max = max(volumes) * 1.2
    
    # Create figure
    fig = go.Figure()
    
    # Add scatter plot
    fig.add_trace(go.Scatter(
        x=volumes,
        y=crews,
        mode='markers',
        name='Space Stations',
        marker=dict(
            size=marker_sizes,
            color=colors,
            line=dict(width=1, color='black'),
            opacity=0.8
        ),
        text=[f"{name}<br>Total Volume: {vol:,.2f} m³<br>Pressurised Volume: {station['pressurised_volume']:,.2f} m³<br>Crew: {crew}" 
              for name, vol, crew, station in zip(names, volumes, crews, SPACE_STATIONS)],
        hoverinfo='text'
    ))
    
    # Add station name labels with improved positioning
    label_positions = {
        'von Braun': dict(xanchor='right', yanchor='bottom', xshift=-10),
        'Hexagonal Station': dict(xanchor='left', yanchor='bottom', xshift=10),
        'ISS': dict(xanchor='right', yanchor='top', xshift=-10),
        'Lunar Gateway': dict(xanchor='left', yanchor='bottom', xshift=10),
        'Tiangong': dict(xanchor='right', yanchor='top', xshift=-10),
        'Skylab': dict(xanchor='left', yanchor='top', xshift=10),
        'Salyut-1': dict(xanchor='right', yanchor='bottom', xshift=-10)
    }
    
    for i, name in enumerate(names):
        position = label_positions.get(name, dict(xanchor='left', yanchor='bottom', xshift=10))
        fig.add_annotation(
            x=volumes[i],
            y=crews[i],
            text=name,
            showarrow=False,
            **position,
            font=dict(size=12, color='#333')
        )
    
    # Update layout
    fig.update_layout(
        title="Space Station Capacity vs Size",
        xaxis=dict(
            title="Total Volume (cubic meters)",
            type="log",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[np.log10(x_min), np.log10(x_max)],
            ticktext=[f"{x:,.0f}" for x in [100, 200, 500, 1000, 2000, 5000, 10000]],
            tickvals=[np.log10(x) for x in [100, 200, 500, 1000, 2000, 5000, 10000]]
        ),
        yaxis=dict(
            title="Number of Astronauts",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[0, 70]
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=50, r=20, t=50, b=50),
        hovermode='closest',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=12)
        )
    )
    
    # Add legend items
    for label, color in [('Actual Station', '#FF5252'), 
                        ('Planned Station', '#FFAB40'), 
                        ('Conceptual Design', '#2979FF')]:
        fig.add_trace(go.Scatter(
            x=[None], y=[None],
            mode='markers',
            name=label,
            marker=dict(size=10, color=color),
            showlegend=True
        ))
    
    # Save as HTML
    fig.write_html(
        'assets/plots/space_station_capacity.html',
        config={'responsive': True, 'displayModeBar': False},
        include_plotlyjs=True,
        full_html=False
    )
    
    return fig

def create_volume_per_astronaut_plot():
    # Extract data for plotting
    names = [station['name'] for station in SPACE_STATIONS]
    total_volumes = [station['total_volume'] for station in SPACE_STATIONS]
    habitable_volumes = [station['habitable_volume'] for station in SPACE_STATIONS]
    crews = [station['crew'] for station in SPACE_STATIONS]
    habitable_volume_per_astronaut = [vol/crew for vol, crew in zip(habitable_volumes, crews)]
    colors = get_station_colors(SPACE_STATIONS)
    
    # Calculate marker sizes (log scale for better visualization)
    marker_sizes = [np.log10(vol) * 10 for vol in total_volumes]
    
    # Create figure
    fig = go.Figure()
    
    # Add scatter plot
    fig.add_trace(go.Scatter(
        x=habitable_volume_per_astronaut,
        y=crews,
        mode='markers',
        name='Space Stations',
        marker=dict(
            size=marker_sizes,
            color=colors,
            line=dict(width=1, color='black'),
            opacity=0.8
        ),
        text=[f"{name}<br>Habitable Volume per Astronaut: {vol_per_ast:,.2f} m³<br>Total Volume: {total_vol:,.2f} m³<br>Habitable Volume: {hab_vol:,.2f} m³<br>Pressurised Volume: {station['pressurised_volume']:,.2f} m³<br>Crew: {crew}" 
              for name, vol_per_ast, total_vol, hab_vol, crew, station in zip(names, habitable_volume_per_astronaut, total_volumes, habitable_volumes, crews, SPACE_STATIONS)],
        hoverinfo='text'
    ))
    
    # Add station name labels
    for i, name in enumerate(names):
        fig.add_annotation(
            x=habitable_volume_per_astronaut[i],
            y=crews[i],
            text=name,
            showarrow=False,
            xanchor='left',
            yanchor='bottom',
            xshift=10,
            yshift=-5,
            font=dict(size=12, color='#333')
        )
    
    # Update layout
    fig.update_layout(
        title="Space Station Capacity vs Habitable Volume per Astronaut",
        xaxis=dict(
            title="Habitable Volume per Astronaut (cubic meters)",
            type="linear",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)'
        ),
        yaxis=dict(
            title="Number of Astronauts",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=50, r=20, t=50, b=50),
        hovermode='closest',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=12)
        )
    )
    
    # Add legend items
    for label, color in [('Actual Station', '#FF5252'), 
                        ('Planned Station', '#FFAB40'), 
                        ('Conceptual Design', '#2979FF')]:
        fig.add_trace(go.Scatter(
            x=[None], y=[None],
            mode='markers',
            name=label,
            marker=dict(size=10, color=color),
            showlegend=True
        ))
    
    # Save as HTML
    fig.write_html(
        'assets/plots/space_station_volume_per_astronaut.html',
        config={'responsive': True, 'displayModeBar': False},
        include_plotlyjs=True,
        full_html=False
    )
    
    return fig

def create_multidimensional_bubble_chart():
    # Extract data for plotting
    names = [station['name'] for station in SPACE_STATIONS]
    total_volumes = [station['total_volume'] for station in SPACE_STATIONS]
    habitable_volumes = [station['habitable_volume'] for station in SPACE_STATIONS]
    crews = [station['crew'] for station in SPACE_STATIONS]
    habitable_volume_per_astronaut = [vol/crew for vol, crew in zip(habitable_volumes, crews)]
    colors = get_station_colors(SPACE_STATIONS)
    
    # Calculate marker sizes (reduced size for better fit)
    marker_sizes = [np.log10(vol) * 12 for vol in total_volumes]
    
    # Create figure
    fig = go.Figure()
    
    # Separate indices for each category
    current_indices = [i for i, station in enumerate(SPACE_STATIONS) if station['is_real']]
    planned_indices = [i for i, station in enumerate(SPACE_STATIONS) if station['is_planned']]
    concept_indices = [i for i, station in enumerate(SPACE_STATIONS) if not station['is_real'] and not station['is_planned']]
    
    # Add current stations
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[i] for i in current_indices],
        y=[crews[i] for i in current_indices],
        mode='markers',
        name='Current',
        marker=dict(
            size=[marker_sizes[i] for i in current_indices],
            color='#FF5252',  # Red for current stations
            line=dict(width=1, color='black'),
            opacity=0.8
        ),
        text=[f"{names[i]}<br>Habitable Volume per Astronaut: {habitable_volume_per_astronaut[i]:,.2f} m³<br>Total Volume: {total_volumes[i]:,.2f} m³<br>Habitable Volume: {habitable_volumes[i]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[i]}" 
              for i in current_indices],
        hoverinfo='text'
    ))
    
    # Add planned stations
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[i] for i in planned_indices],
        y=[crews[i] for i in planned_indices],
        mode='markers',
        name='Planned',
        marker=dict(
            size=[marker_sizes[i] for i in planned_indices],
            color='#FFAB40',  # Orange for planned stations
            line=dict(width=1, color='black'),
            opacity=0.8
        ),
        text=[f"{names[i]}<br>Habitable Volume per Astronaut: {habitable_volume_per_astronaut[i]:,.2f} m³<br>Total Volume: {total_volumes[i]:,.2f} m³<br>Habitable Volume: {habitable_volumes[i]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[i]}" 
              for i in planned_indices],
        hoverinfo='text'
    ))
    
    # Add concept stations (with donut shape)
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[i] for i in concept_indices],
        y=[crews[i] for i in concept_indices],
        mode='markers',
        name='Concepts',
        marker=dict(
            size=[marker_sizes[i] for i in concept_indices],
            color='#2979FF',  # Blue for concept stations
            line=dict(width=2, color='black'),
            opacity=0.8,
            symbol='circle-open'  # Donut shape for artificial gravity stations
        ),
        text=[f"{names[i]}<br>Habitable Volume per Astronaut: {habitable_volume_per_astronaut[i]:,.2f} m³<br>Total Volume: {total_volumes[i]:,.2f} m³<br>Habitable Volume: {habitable_volumes[i]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[i]}" 
              for i in concept_indices],
        hoverinfo='text'
    ))
    
    # Add station name labels with improved positioning
    label_positions = {
        'von Braun': dict(xanchor='right', yanchor='bottom', xshift=-10),
        'Hexagonal Station': dict(xanchor='left', yanchor='bottom', xshift=10),
        'ISS': dict(xanchor='right', yanchor='top', xshift=-10),
        'Lunar Gateway': dict(xanchor='left', yanchor='bottom', xshift=10),
        'Tiangong': dict(xanchor='right', yanchor='top', xshift=-10),
        'Skylab': dict(xanchor='left', yanchor='top', xshift=10),
        'Salyut-1': dict(xanchor='right', yanchor='bottom', xshift=-10)
    }
    
    for i, name in enumerate(names):
        position = label_positions.get(name, dict(xanchor='left', yanchor='bottom', xshift=10))
        fig.add_annotation(
            x=habitable_volume_per_astronaut[i],
            y=crews[i],
            text=name,
            showarrow=False,
            **position,
            font=dict(size=12, color='#333')
        )
    
    # Update layout with improved spacing and no title
    fig.update_layout(
        xaxis=dict(
            title="Habitable Volume per Astronaut (cubic meters)",
            type="linear",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[25, 105],
            dtick=10
        ),
        yaxis=dict(
            title="Crew Capacity (number of astronauts)",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[-2, 70],
            dtick=10
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=60, r=30, t=30, b=60),
        hovermode='closest',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=12),
            itemwidth=40,
            itemsizing='constant'
        ),
        width=800,
        height=600,
        showlegend=True
    )
    
    # Save as HTML
    fig.write_html(
        'assets/plots/space_station_multidimensional.html',
        config={'responsive': True, 'displayModeBar': False},
        include_plotlyjs=True,
        full_html=False
    )
    
    return fig

if __name__ == "__main__":
    create_space_station_plot()
    create_volume_per_astronaut_plot()
    create_multidimensional_bubble_chart() 