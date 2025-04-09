import plotly.graph_objects as go
import numpy as np

# Shared space station data
SPACE_STATIONS = [
    # Real historical stations
    {'name': 'Salyut-1', 'total_volume': 214, 'pressurised_volume': 99, 'habitable_volume': 90, 'crew': 3, 'is_real': True, 'has_gravity': False},
    {'name': 'MORL', 'total_volume': 254.85, 'pressurised_volume': 254.85, 'habitable_volume': 200, 'crew': 6, 'is_real': False, 'has_gravity': False},
    {'name': 'LORL', 'total_volume': 1905.85, 'pressurised_volume': 1905.85, 'habitable_volume': 1905.85, 'crew': 24, 'is_real': False, 'has_gravity': False},
    {'name': 'Haven-1', 'total_volume': 80, 'pressurised_volume': 80, 'habitable_volume': 45, 'crew': 4, 'is_real': False, 'has_gravity': False},
    {'name': 'Haven-2', 'total_volume': 1160, 'pressurised_volume': 1160, 'habitable_volume': 500, 'crew': 12, 'is_real': False, 'has_gravity': False},
    {'name': 'Skylab', 'total_volume': 499, 'pressurised_volume': 351.6, 'habitable_volume': 270, 'crew': 3, 'is_real': True, 'has_gravity': False},
    {'name': 'Tiangong', 'total_volume': 726.6 , 'pressurised_volume': 340, 'habitable_volume': 121, 'crew': 3, 'is_real': True, 'has_gravity': False},
    {'name': 'ISS', 'total_volume': 1200, 'pressurised_volume': 1005, 'habitable_volume': 388, 'crew': 7, 'is_real': True, 'has_gravity': False},
    
    # Planned station
    {'name': 'Gateway', 'total_volume': 183, 'pressurised_volume': 183, 'habitable_volume': 125, 'crew': 4, 'is_real': False, 'has_gravity': False},
    
    # Conceptual designs
    {'name': 'von Braun', 'total_volume': 6217.85, 'pressurised_volume': 4800, 'habitable_volume': 3600, 'crew': 80, 'is_real': False, 'has_gravity': True},
    {'name': 'Space Base', 'total_volume': 5921, 'pressurised_volume': 3600, 'habitable_volume': 3600, 'crew': 100, 'is_real': False, 'has_gravity': True},
    {'name': 'Hexagonal Station', 'total_volume': 1274.3, 'pressurised_volume': 980, 'habitable_volume': 980, 'crew': 36, 'is_real': False, 'has_gravity': True},
    {
        'name': '2035 AG Station',
        'total_volume': 2160,  # Using pressurized volume as total volume
        'pressurised_volume': 2160,
        'habitable_volume': 950,
        'crew': 40,
        'is_real': False,
        'has_gravity': True
    },
    {
        'name': 'Stanford Torus',
        'total_volume': 8233000,  # Approximate volume in cubic meters
        'pressurised_volume': 8233000,
        'habitable_volume': 8233000,  # Estimated 75% of total volume as habitable
        'crew': 10000,
        'is_real': False,
        'has_gravity': True
    },
    {
        'name': "O'Neill Cylinder",
        'total_volume': 1600000000,  # Approximate volume in cubic meters
        'pressurised_volume': 1600000000,
        'habitable_volume': 1200000000,  # Estimated 75% of total volume as habitable
        'crew': 1000000,
        'is_real': False,
        'has_gravity': True
    },
]

def get_station_colors(data):
    """Helper function to get colors based on station type"""
    colors = []
    for station in data:
        if station['is_real']:
            colors.append('#4CAF50')  # Green for real stations (works in both light/dark modes)
        elif station['has_gravity']:
            colors.append('#2979FF')  # Blue for artificial gravity stations
        else:
            colors.append('#F44336')  # Red for planned 0-g stations
    return colors

def create_multidimensional_bubble_chart():
    # Filter out the mega-stations and Salyut-1 for plotting
    excluded_stations = ['MORL', 'LORL']  # Now excluding MORL and LORL
    plot_indices = [i for i, station in enumerate(SPACE_STATIONS) if station['name'] not in excluded_stations]
    
    # Extract data for plotting (only for included stations)
    names = [SPACE_STATIONS[i]['name'] for i in plot_indices]
    total_volumes = [SPACE_STATIONS[i]['total_volume'] for i in plot_indices]
    habitable_volumes = [SPACE_STATIONS[i]['habitable_volume'] for i in plot_indices]
    crews = [SPACE_STATIONS[i]['crew'] for i in plot_indices]
    habitable_volume_per_astronaut = [vol/crew for vol, crew in zip(habitable_volumes, crews)]
    
    # Calculate marker sizes (reduced size for better fit)
    marker_sizes = [np.log10(vol) * 12 for vol in total_volumes]
    
    # Adjust size for Hexagonal Station specifically
    for i, name in enumerate(names):
        if name == 'Hexagonal Station':
            marker_sizes[i] *= 0.8  # Make Hexagonal Station marker 20% smaller
    
    # Create figure
    fig = go.Figure()
    
    # Separate indices for each category (using filtered indices)
    # 1. Real stations (green)
    real_indices = [i for i, station in enumerate(SPACE_STATIONS) if station['is_real'] and station['name'] not in excluded_stations]
    
    # 2. Planned 0-g stations (red)
    planned_0g_indices = [i for i, station in enumerate(SPACE_STATIONS) 
                         if not station['is_real'] and not station['has_gravity'] 
                         and station['name'] not in excluded_stations]
    
    # 3. Artificial gravity stations (blue donut)
    ag_indices = [i for i, station in enumerate(SPACE_STATIONS) 
                 if not station['is_real'] and station['has_gravity'] 
                 and station['name'] not in excluded_stations 
                 and station['name'] not in ['Stanford Torus', "O'Neill Cylinder"]]
    
    # 4. Megastructures (purple star)
    megastructure_indices = [i for i, station in enumerate(SPACE_STATIONS) 
                           if station['name'] in ['Stanford Torus', "O'Neill Cylinder"]]
    
    # Add real stations (green)
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[plot_indices.index(i)] for i in real_indices],
        y=[crews[plot_indices.index(i)] for i in real_indices],
        mode='markers',
        name='Real Stations',
        marker=dict(
            size=[marker_sizes[plot_indices.index(i)] for i in real_indices],
            color='#4CAF50',
            line=dict(width=1, color='black'),
            opacity=0.8
        ),
        hoverinfo='text',
        hovertext=[f"{SPACE_STATIONS[i]['name']}<br>Habitable Volume per Astronaut: {habitable_volumes[plot_indices.index(i)]/crews[plot_indices.index(i)]:,.2f} m³<br>Total Volume: {total_volumes[plot_indices.index(i)]:,.2f} m³<br>Habitable Volume: {habitable_volumes[plot_indices.index(i)]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[plot_indices.index(i)]}" 
                  for i in real_indices]
    ))
    
    # Add planned 0-g stations (red)
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[plot_indices.index(i)] for i in planned_0g_indices],
        y=[crews[plot_indices.index(i)] for i in planned_0g_indices],
        mode='markers',
        name='Planned 0-g Stations',
        marker=dict(
            size=[marker_sizes[plot_indices.index(i)] for i in planned_0g_indices],
            color='#F44336',
            line=dict(width=1, color='black'),
            opacity=0.8
        ),
        hoverinfo='text',
        hovertext=[f"{SPACE_STATIONS[i]['name']}<br>Habitable Volume per Astronaut: {habitable_volumes[plot_indices.index(i)]/crews[plot_indices.index(i)]:,.2f} m³<br>Total Volume: {total_volumes[plot_indices.index(i)]:,.2f} m³<br>Habitable Volume: {habitable_volumes[plot_indices.index(i)]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[plot_indices.index(i)]}" 
                  for i in planned_0g_indices]
    ))
    
    # Add artificial gravity stations (blue donut)
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[plot_indices.index(i)] for i in ag_indices],
        y=[crews[plot_indices.index(i)] for i in ag_indices],
        mode='markers',
        name='Artificial Gravity Concepts',
        marker=dict(
            size=[marker_sizes[plot_indices.index(i)] for i in ag_indices],
            color='#2979FF',
            line=dict(width=2, color='black'),
            opacity=0.8,
            symbol='circle-open'
        ),
        hoverinfo='text',
        hovertext=[f"{SPACE_STATIONS[i]['name']}<br>Habitable Volume per Astronaut: {habitable_volumes[plot_indices.index(i)]/crews[plot_indices.index(i)]:,.2f} m³<br>Total Volume: {total_volumes[plot_indices.index(i)]:,.2f} m³<br>Habitable Volume: {habitable_volumes[plot_indices.index(i)]:,.2f} m³<br>Pressurised Volume: {SPACE_STATIONS[i]['pressurised_volume']:,.2f} m³<br>Crew: {crews[plot_indices.index(i)]}" 
                  for i in ag_indices]
    ))
    
    # Add Stanford Torus as a megastructure
    stanford_torus_index = next(i for i, station in enumerate(SPACE_STATIONS) if station['name'] == 'Stanford Torus')
    stanford_torus = SPACE_STATIONS[stanford_torus_index]
    
    fig.add_trace(go.Scatter(
        x=[stanford_torus['habitable_volume'] / stanford_torus['crew']],
        y=[110],
        mode='markers',
        name='Megastructure',
        legendgroup='megastructure',
        marker=dict(
            size=30,
            color='#9C27B0',
            line=dict(width=3, color='black'),
            opacity=0.9,
            symbol='star'
        ),
        hoverinfo='text',
        hovertext=f"{stanford_torus['name']}<br>Habitable Volume per Astronaut: {stanford_torus['habitable_volume']/stanford_torus['crew']:,.2f} m³<br>Total Volume: {stanford_torus['total_volume']:,.2f} m³<br>Habitable Volume: {stanford_torus['habitable_volume']:,.2f} m³<br>Pressurised Volume: {stanford_torus['pressurised_volume']:,.2f} m³<br>Crew: {stanford_torus['crew']:,}"
    ))
    
    # Add O'Neill Cylinder as a megastructure at fixed x=120
    oneill_cylinder_index = next(i for i, station in enumerate(SPACE_STATIONS) if station['name'] == "O'Neill Cylinder")
    oneill_cylinder = SPACE_STATIONS[oneill_cylinder_index]
    
    fig.add_trace(go.Scatter(
        x=[120],
        y=[120],
        mode='markers',
        name='Megastructure',
        legendgroup='megastructure',
        showlegend=False,  # Hide this trace from the legend
        marker=dict(
            size=35,
            color='#9C27B0',
            line=dict(width=3, color='black'),
            opacity=0.9,
            symbol='star'
        ),
        hoverinfo='text',
        hovertext=f"{oneill_cylinder['name']}<br>Habitable Volume per Astronaut: {oneill_cylinder['habitable_volume']/oneill_cylinder['crew']:,.2f} m³<br>Total Volume: {oneill_cylinder['total_volume']:,.2f} m³<br>Habitable Volume: {oneill_cylinder['habitable_volume']:,.2f} m³<br>Pressurised Volume: {oneill_cylinder['pressurised_volume']:,.2f} m³<br>Crew: {oneill_cylinder['crew']:,}"
    ))
    
    # Add station name labels with improved positioning
    label_positions = {
        'Salyut-1': dict(xanchor='right', yanchor='bottom', xshift=-15, yshift=-10),
        'von Braun': dict(xanchor='left', yanchor='bottom', xshift=15, yshift=15),
        'Hexagonal Station': dict(xanchor='left', yanchor='middle', xshift=25, yshift=0),
        'ISS': dict(xanchor='left', yanchor='bottom', xshift=15, yshift=5),
        'Gateway': dict(xanchor='right', yanchor='bottom', xshift=-15, yshift=5),
        'Tiangong': dict(xanchor='left', yanchor='middle', xshift=25, yshift=0),
        'Skylab': dict(xanchor='left', yanchor='bottom', xshift=15, yshift=5),
        'Haven-1': dict(xanchor='center', yanchor='bottom', xshift=0, yshift=15)
    }
    
    # Add annotations for each station
    for i, name in enumerate(names):
        if name not in ['Stanford Torus', "O'Neill Cylinder"]:
            position = label_positions.get(name, dict(xanchor='left', yanchor='bottom', xshift=15, yshift=5))
            # Determine color based on station type
            if SPACE_STATIONS[plot_indices[i]]['is_real']:
                color = '#4CAF50'  # Green for real stations
            elif SPACE_STATIONS[plot_indices[i]]['has_gravity']:
                color = '#2979FF'  # Blue for artificial gravity stations
            else:
                color = '#F44336'  # Red for planned 0-g stations
                
            fig.add_annotation(
                x=habitable_volume_per_astronaut[i],
                y=crews[i],
                text=name,
                showarrow=False,
                **position,
                font=dict(
                    size=12,
                    color=color
                ),
                bgcolor='rgba(255, 255, 255, 0.7)',  # Semi-transparent white background
                borderpad=2
            )
    
    # Add label for Stanford Torus
    fig.add_annotation(
        x=stanford_torus['habitable_volume'] / stanford_torus['crew'],
        y=110,
        text="Stanford Torus",
        showarrow=False,
        xanchor='center',
        yanchor='bottom',
        yshift=10,
        font=dict(
            size=14,
            color='#9C27B0',
            family='Arial Black'
        ),
        bgcolor='rgba(255, 255, 255, 0.7)',  # Semi-transparent white background
        borderpad=2
    )
    
    # Add label for O'Neill Cylinder
    fig.add_annotation(
        x=120,
        y=120,
        text="O'Neill Cylinder",
        showarrow=False,
        xanchor='center',
        yanchor='bottom',
        yshift=10,
        font=dict(
            size=14,
            color='#9C27B0',
            family='Arial Black'
        ),
        bgcolor='rgba(255, 255, 255, 0.7)',  # Semi-transparent white background
        borderpad=2
    )
    
    # Update layout with improved spacing and no title
    fig.update_layout(
        xaxis=dict(
            title="Habitable Volume per Astronaut (cubic meters)",
            type="linear",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[5, 130],
            dtick=10,
            ticktext=["5", "15", "25", "35", "45", "55", "65", "75", "85", "95", "105", "1000+"],
            tickvals=[5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 120]
        ),
        yaxis=dict(
            title="Crew Capacity (number of astronauts)",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[-2, 130],
            dtick=10,
            ticktext=["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "10,000", "1M"],
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
        showlegend=True,
        # Add hover template configuration
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )
    
    # Save as HTML with updated config
    fig.write_html(
        'assets/plots/WiP1/space_station_multidimensional.html',
        config={
            'responsive': True,
            'displayModeBar': False,
            'showTips': True
        },
        include_plotlyjs=True,
        full_html=False
    )
    
    return fig

if __name__ == "__main__":
    create_multidimensional_bubble_chart()