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
    {'name': 'von Braun', 'total_volume': 6217.85, 'pressurised_volume': 4800, 'habitable_volume': 3600, 'crew': 80, 'is_real': False, 'is_planned': False, 'has_gravity': True},
    # {'name': 'Space Base', 'total_volume': 1274325, 'pressurised_volume': 980000, 'crew': 87.5, 'is_real': False, 'is_planned': False, 'has_gravity': True},
    {'name': 'Hexagonal Station', 'total_volume': 1274.3, 'pressurised_volume': 980, 'habitable_volume': 980, 'crew': 36, 'is_real': False, 'is_planned': False, 'has_gravity': True},
    {
        'name': 'Stanford Torus',
        'total_volume': 870000,  # Approximate volume in cubic meters
        'pressurised_volume': 870000,
        'habitable_volume': 650000,  # Estimated 75% of total volume as habitable
        'crew': 10000,
        'is_real': False,
        'is_planned': False,
        'has_gravity': True
    },
    {
        'name': "O'Neill Cylinder",
        'total_volume': 1600000000,  # Approximate volume in cubic meters
        'pressurised_volume': 1600000000,
        'habitable_volume': 1200000000,  # Estimated 75% of total volume as habitable
        'crew': 1000000,
        'is_real': False,
        'is_planned': False,
        'has_gravity': True
    },
]

def get_station_colors(data):
    """Helper function to get colors based on station type"""
    colors = []
    for station in data:
        if station['is_real']:
            colors.append('#4CAF50')  # Green for real stations (works in both light/dark modes)
        elif station['is_planned']:
            colors.append('#F44336')  # Red for planned stations (works in both light/dark modes)
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
    for label, color in [('Actual Station', '#4CAF50'), 
                        ('Planned Station', '#F44336'), 
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
    for label, color in [('Actual Station', '#4CAF50'), 
                        ('Planned Station', '#F44336'), 
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
    # Filter out the mega-stations for plotting
    excluded_stations = []  # No longer excluding O'Neill Cylinder
    plot_indices = [i for i, station in enumerate(SPACE_STATIONS) if station['name'] not in excluded_stations]
    
    # Extract data for plotting (only for included stations)
    names = [SPACE_STATIONS[i]['name'] for i in plot_indices]
    total_volumes = [SPACE_STATIONS[i]['total_volume'] for i in plot_indices]
    habitable_volumes = [SPACE_STATIONS[i]['habitable_volume'] for i in plot_indices]
    crews = [SPACE_STATIONS[i]['crew'] for i in plot_indices]
    habitable_volume_per_astronaut = [vol/crew for vol, crew in zip(habitable_volumes, crews)]
    
    # Calculate marker sizes (reduced size for better fit)
    marker_sizes = [np.log10(vol) * 12 for vol in total_volumes]
    
    # Create figure
    fig = go.Figure()
    
    # Separate indices for each category (using filtered indices)
    current_indices = [i for i, station in enumerate(SPACE_STATIONS) if station['is_real'] and station['name'] not in excluded_stations]
    planned_indices = [i for i, station in enumerate(SPACE_STATIONS) if station['is_planned'] and station['name'] not in excluded_stations]
    concept_indices = [i for i, station in enumerate(SPACE_STATIONS) if not station['is_real'] and not station['is_planned'] and station['name'] not in excluded_stations and station['name'] not in ['Stanford Torus', "O'Neill Cylinder"]]
    
    # Add current stations
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[plot_indices.index(i)] for i in current_indices],
        y=[crews[plot_indices.index(i)] for i in current_indices],
        mode='markers',
        name='Current',
        marker=dict(
            size=[marker_sizes[plot_indices.index(i)] for i in current_indices],
            color='#4CAF50',  # Green for current stations (works in both light/dark modes)
            line=dict(width=1, color='black'),
            opacity=0.8
        ),
        text=[f"{SPACE_STATIONS[i]['name']}<br>Habitable Volume per Astronaut: {habitable_volumes[plot_indices.index(i)]/crews[plot_indices.index(i)]:,.2f} m³<br>Total Volume: {total_volumes[plot_indices.index(i)]:,.2f} m³<br>Habitable Volume: {habitable_volumes[plot_indices.index(i)]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[plot_indices.index(i)]}" 
              for i in current_indices],
        hoverinfo='text'
    ))
    
    # Add planned stations
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[plot_indices.index(i)] for i in planned_indices],
        y=[crews[plot_indices.index(i)] for i in planned_indices],
        mode='markers',
        name='Planned',
        marker=dict(
            size=[marker_sizes[plot_indices.index(i)] for i in planned_indices],
            color='#F44336',  # Red for planned stations (works in both light/dark modes)
            line=dict(width=1, color='black'),
            opacity=0.8
        ),
        text=[f"{SPACE_STATIONS[i]['name']}<br>Habitable Volume per Astronaut: {habitable_volumes[plot_indices.index(i)]/crews[plot_indices.index(i)]:,.2f} m³<br>Total Volume: {total_volumes[plot_indices.index(i)]:,.2f} m³<br>Habitable Volume: {habitable_volumes[plot_indices.index(i)]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[plot_indices.index(i)]}" 
              for i in planned_indices],
        hoverinfo='text'
    ))
    
    # Add concept stations (with donut shape)
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[plot_indices.index(i)] for i in concept_indices],
        y=[crews[plot_indices.index(i)] for i in concept_indices],
        mode='markers',
        name='Concepts',
        marker=dict(
            size=[marker_sizes[plot_indices.index(i)] for i in concept_indices],
            color='#2979FF',  # Blue for concept stations
            line=dict(width=2, color='black'),
            opacity=0.8,
            symbol='circle-open'  # Donut shape for artificial gravity stations
        ),
        text=[f"{SPACE_STATIONS[i]['name']}<br>Habitable Volume per Astronaut: {habitable_volumes[plot_indices.index(i)]/crews[plot_indices.index(i)]:,.2f} m³<br>Total Volume: {total_volumes[plot_indices.index(i)]:,.2f} m³<br>Habitable Volume: {habitable_volumes[plot_indices.index(i)]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[plot_indices.index(i)]}" 
              for i in concept_indices],
        hoverinfo='text'
    ))
    
    # Add Stanford Torus as a superstructure
    stanford_torus_index = next(i for i, station in enumerate(SPACE_STATIONS) if station['name'] == 'Stanford Torus')
    stanford_torus = SPACE_STATIONS[stanford_torus_index]
    
    fig.add_trace(go.Scatter(
        x=[stanford_torus['habitable_volume'] / stanford_torus['crew']],
        y=[110],  # Place at y=110 for the superstructure category
        mode='markers',
        name='Superstructure',  # Changed from Megastructure to Superstructure
        marker=dict(
            size=30,  # Larger size to emphasize
            color='#9C27B0',  # Purple for superstructure
            line=dict(width=3, color='black'),
            opacity=0.9,
            symbol='star'  # Star shape for superstructure
        ),
        text=f"{stanford_torus['name']}<br>Habitable Volume per Astronaut: {stanford_torus['habitable_volume']/stanford_torus['crew']:,.2f} m³<br>Total Volume: {stanford_torus['total_volume']:,.2f} m³<br>Habitable Volume: {stanford_torus['habitable_volume']:,.2f} m³<br>Pressurised Volume: {stanford_torus['pressurised_volume']:,.2f} m³<br>Crew: {stanford_torus['crew']:,}",
        hoverinfo='text'
    ))
    
    # Add O'Neill Cylinder as a megastructure at fixed x=120
    oneill_cylinder_index = next(i for i, station in enumerate(SPACE_STATIONS) if station['name'] == "O'Neill Cylinder")
    oneill_cylinder = SPACE_STATIONS[oneill_cylinder_index]
    
    fig.add_trace(go.Scatter(
        x=[120],  # Fixed x position
        y=[120],  # Place at y=120 for the megastructure category
        mode='markers',
        name='Megastructure',  # Different name to avoid duplicate legend
        marker=dict(
            size=35,  # Slightly larger size to emphasize
            color='#9C27B0',  # Purple for megastructure
            line=dict(width=3, color='black'),
            opacity=0.9,
            symbol='star'  # Star shape for megastructure
        ),
        text=f"{oneill_cylinder['name']}<br>Habitable Volume per Astronaut: {oneill_cylinder['habitable_volume']/oneill_cylinder['crew']:,.2f} m³<br>Total Volume: {oneill_cylinder['total_volume']:,.2f} m³<br>Habitable Volume: {oneill_cylinder['habitable_volume']:,.2f} m³<br>Pressurised Volume: {oneill_cylinder['pressurised_volume']:,.2f} m³<br>Crew: {oneill_cylinder['crew']:,}",
        hoverinfo='text'
    ))
    
    # Add station name labels with improved positioning (only for included stations)
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
    
    # Add label for Stanford Torus
    fig.add_annotation(
        x=stanford_torus['habitable_volume'] / stanford_torus['crew'],
        y=110,
        text="Stanford Torus",
        showarrow=False,
        xanchor='right',
        yanchor='top',
        xshift=-10,
        yshift=10,
        font=dict(size=14, color='#9C27B0', family='Arial Black')
    )
    
    # Add label for O'Neill Cylinder
    fig.add_annotation(
        x=120,
        y=120,
        text="O'Neill Cylinder",
        showarrow=False,
        xanchor='right',
        yanchor='top',
        xshift=-10,
        yshift=10,
        font=dict(size=14, color='#9C27B0', family='Arial Black')
    )
    
    # Update layout with improved spacing and no title
    fig.update_layout(
        xaxis=dict(
            title="Habitable Volume per Astronaut (cubic meters)",
            type="linear",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[25, 130],  # Extended to accommodate megastructure label
            dtick=10,
            # Add a special tick for the megastructure category
            ticktext=["25", "35", "45", "55", "65", "75", "85", "95", "105", "Megastructure"],
            tickvals=[25, 35, 45, 55, 65, 75, 85, 95, 105, 120]
        ),
        yaxis=dict(
            title="Crew Capacity (number of astronauts)",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[-2, 130],  # Extended to accommodate megastructures
            dtick=10,
            # Add special ticks for the superstructure and megastructure categories
            ticktext=["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "Superstructure", "Megastructure"],
            tickvals=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
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

def create_megastructure_comparison():
    # Select specific stations to compare
    selected_stations = ['Skylab', 'ISS', 'von Braun', 'Stanford Torus', "O'Neill Cylinder"]
    station_data = [s for s in SPACE_STATIONS if s['name'] in selected_stations]
    
    # Extract data for plotting
    names = [station['name'] for station in station_data]
    total_volumes = [station['total_volume'] for station in station_data]
    habitable_volumes = [station['habitable_volume'] for station in station_data]
    crews = [station['crew'] for station in station_data]
    habitable_volume_per_astronaut = [vol/crew for vol, crew in zip(habitable_volumes, crews)]
    
    # Create figure
    fig = go.Figure()
    
    # Add scatter plot for each category
    for i, station in enumerate(station_data):
        is_gravity = station['has_gravity']
        color = '#4CAF50' if station['is_real'] else '#2979FF'  # Green for real, Blue for concepts
        
        fig.add_trace(go.Scatter(
            x=[habitable_volume_per_astronaut[i]],
            y=[crews[i]],
            mode='markers',
            name=station['name'],
            marker=dict(
                size=25,  # Fixed size for all markers
                color=color,
                line=dict(width=2, color='black'),
                opacity=0.8,
                symbol='circle-open' if is_gravity else 'circle'
            ),
            text=f"{names[i]}<br>Habitable Volume per Astronaut: {habitable_volume_per_astronaut[i]:,.2f} m³<br>Total Volume: {total_volumes[i]:,.2f} m³<br>Habitable Volume: {habitable_volumes[i]:,.2f} m³<br>Pressurised Volume: {station['pressurised_volume']:,.2f} m³<br>Crew: {crews[i]}",
            hoverinfo='text'
        ))
    
    # Add station name labels with improved positioning
    label_positions = {
        'von Braun': dict(xanchor='right', yanchor='middle', xshift=-30),
        'ISS': dict(xanchor='left', yanchor='middle', xshift=30),
        'Skylab': dict(xanchor='right', yanchor='middle', xshift=-30),
        'Stanford Torus': dict(xanchor='right', yanchor='middle', xshift=-30),
        "O'Neill Cylinder": dict(xanchor='right', yanchor='middle', xshift=-30)
    }
    
    for i, name in enumerate(names):
        position = label_positions.get(name, dict(xanchor='left', yanchor='middle', xshift=30))
        fig.add_annotation(
            x=habitable_volume_per_astronaut[i],
            y=crews[i],
            text=name,
            showarrow=False,  # Remove arrows
            **position,
            font=dict(size=12, color='white'),
            bgcolor='rgba(50, 50, 50, 0.8)',  # Dark semi-transparent background
            bordercolor='rgba(255, 255, 255, 0.3)',
            borderwidth=1,
            borderpad=4,
            opacity=0.8
        )
    
    # Update layout
    fig.update_layout(
        xaxis=dict(
            title="Habitable Volume per Astronaut (cubic meters)",
            type="linear",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            showgrid=True,
            dtick=200,
            range=[0, 1400]
        ),
        yaxis=dict(
            title="Crew Capacity (number of astronauts)",
            type="log",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            showgrid=True,
            dtick=1,
            range=[0, 6]
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=60, r=100, t=30, b=60),  # Increased right margin further
        hovermode='closest',
        showlegend=False,
        width=800,
        height=600
    )
    
    # Save as HTML
    fig.write_html(
        'assets/plots/space_station_megastructure.html',
        config={'responsive': True, 'displayModeBar': False},
        include_plotlyjs=True,
        full_html=False
    )
    
    return fig

if __name__ == "__main__":
    create_space_station_plot()
    create_volume_per_astronaut_plot()
    create_multidimensional_bubble_chart()
    create_megastructure_comparison() 