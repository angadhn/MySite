import plotly.graph_objects as go
import numpy as np
import math

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
    # Starship (SpaceX)
    {'name': 'Starship', 'total_volume': 1000, 'pressurised_volume': 1000, 'habitable_volume': 1000, 'crew': 100, 'is_real': False, 'has_gravity': False},
    
    # Planned station
    {'name': 'Gateway', 'total_volume': 183, 'pressurised_volume': 183, 'habitable_volume': 125, 'crew': 4, 'is_real': False, 'has_gravity': False},
    
    # Conceptual designs
    {'name': 'von Braun wheel', 'total_volume': 6217.85, 'pressurised_volume': 4800, 'habitable_volume': 3600, 'crew': 80, 'is_real': False, 'has_gravity': True},
    {'name': 'Space Base', 'total_volume': 5921, 'pressurised_volume': 3600, 'habitable_volume': 3600, 'crew': 100, 'is_real': False, 'has_gravity': True},
    {'name': 'Hexagonal Station', 'total_volume': 1274.3, 'pressurised_volume': 980, 'habitable_volume': 980, 'crew': 36, 'is_real': False, 'has_gravity': True},
    {
        'name': '2035 Vast Station',
        'total_volume': 2160,  # Using pressurized volume as total volume
        'pressurised_volume': 2160,
        'habitable_volume': 950,
        'crew': 40,
        'is_real': False,
        'has_gravity': True
    },
    {
        'name': 'Gateway\'s von Braun',
        'total_volume': 12000,
        'pressurised_volume': 11906250,
        'habitable_volume': 8000000,
        'crew': 1400,
        'is_real': False,
        'has_gravity': True
    },
    {
    'name': 'Stanford Torus',
    'total_volume': 69220470,  # Correct volume in cubic meters
    'pressurised_volume': 69220470,  # Assuming entire torus is pressurized
    'habitable_volume': 34610235,  # Estimated 50% of total volume as habitable
    'crew': 10000,  # Original NASA design specification
    'is_real': False,
    'has_gravity': True  # Via rotation
    },
    {
    'name': "O'Neill Cylinder",
    'total_volume': 1636828970203,  # Volume in cubic meters
    'pressurised_volume': 1604092390799,  # 98% of total volume
    'habitable_volume': 1227621727652,  # 75% of total volume as habitable
    'crew': 1000000,  # Keeping original crew estimate
    'is_real': False,
    'has_gravity': True  # Via rotation
    },
    {
    'name': "O'Neill Cylinder (pair)",
    'total_volume': 3273657940405,  # Volume in cubic meters
    'pressurised_volume': 3208184781597,
    'habitable_volume': 2455243455304,  # 75% of total volume as habitable
    'crew': 2000000,  # Doubled crew estimate
    'is_real': False,
    'has_gravity': True  # Via rotation
    }
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
    excluded_stations = []  # Now excluding MORL and LORL
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
    
    # Add rectangular regions for different space structure categories
    # Superstructures region (130+ m³/person, 140+ crew)
    fig.add_shape(
        type="rect",
        x0=0, y0=0,
        x1=130, y1=140,
        fillcolor="rgba(128, 0, 128, 0.08)",
        line=dict(color="purple", width=2),
        layer="below"
    )
    # Spaceships region (100-130 m³/person, 50-140 crew)
    fig.add_shape(
        type="rect",
        x0=0, y0=0,
        x1=110, y1=110,
        fillcolor="rgba(0, 0, 255, 0.08)",
        line=dict(color="blue", width=2),
        layer="below"
    )
    # Space Stations region (0-100 m³/person, 0-50 crew)
    fig.add_shape(
        type="rect",
        x0=0, y0=0,
        x1=100, y1=50,
        fillcolor="rgba(0, 255, 0, 0.1)",
        line=dict(color="green", width=2),
        layer="below"
    )

    # Add region labels
    fig.add_annotation(
        x=11.5, y=35,
        text="Space<br>Stations",
        showarrow=False,
        font=dict(color="green", size=12),
        bgcolor="rgba(255, 255, 255, 0.8)",
        bordercolor="green",
        borderwidth=1,
        borderpad=4
    )

    fig.add_annotation(
        x=13, y=55,
        text="Spaceships",
        showarrow=False,
        font=dict(color="blue", size=12),
        bgcolor="rgba(255, 255, 255, 0.8)",
        bordercolor="blue",
        borderwidth=1,
        borderpad=4
    )
    fig.add_annotation(
        x=15, y=115,
        text="Superstructures",
        showarrow=False,
        font=dict(color="purple", size=12),
        bgcolor="rgba(255, 255, 255, 0.8)",
        bordercolor="purple",
        borderwidth=1,
        borderpad=4
    )
    
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
                           if station['name'] in ['Stanford Torus', "O'Neill Cylinder", "Gateway's von Braun"]]
    
    # Add real stations (green)
    fig.add_trace(go.Scatter(
        x=[habitable_volume_per_astronaut[plot_indices.index(i)] for i in real_indices],
        y=[crews[plot_indices.index(i)] for i in real_indices],
        mode='markers',
        name='Real Stations',
        legendgroup='real_stations',
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
        legendgroup='planned_0g_stations',
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
        legendgroup='ag_stations',
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
    stanford_torus_per_person = stanford_torus['habitable_volume'] / stanford_torus['crew']
    
    # Format values with appropriate significant figures
    stanford_formatted = f"{stanford_torus_per_person/1000:.1f}K"  # Format as K for thousands
    
    fig.add_trace(go.Scatter(
        x=[110],  # Changed to 110
        y=[120],
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
        hovertext=f"{stanford_torus['name']}<br>Habitable Volume per Astronaut: {stanford_formatted} m³<br>Total Volume: {stanford_torus['total_volume']:,.2f} m³<br>Habitable Volume: {stanford_torus['habitable_volume']:,.2f} m³<br>Pressurised Volume: {stanford_torus['pressurised_volume']:,.2f} m³<br>Crew: {stanford_torus['crew']:,}"
    ))
    
    # Add O'Neill Cylinder as a megastructure with fixed position
    oneill_cylinder_index = next(i for i, station in enumerate(SPACE_STATIONS) if station['name'] == "O'Neill Cylinder")
    oneill_cylinder = SPACE_STATIONS[oneill_cylinder_index]
    oneill_cylinder_per_person = oneill_cylinder['habitable_volume'] / oneill_cylinder['crew']
    
    # Format values with appropriate significant figures
    oneill_formatted = f"{oneill_cylinder_per_person/1000000:.1f}M"  # Format as M for millions
    
    fig.add_trace(go.Scatter(
        x=[120],  # Changed to 120
        y=[130],
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
        hovertext=f"{oneill_cylinder['name']}<br>Habitable Volume per Astronaut: {oneill_formatted} m³<br>Total Volume: {oneill_cylinder['total_volume']:,.2f} m³<br>Habitable Volume: {oneill_cylinder['habitable_volume']:,.2f} m³<br>Pressurised Volume: {oneill_cylinder['pressurised_volume']:,.2f} m³<br>Crew: {oneill_cylinder['crew']:,}"
    ))
    
    # Add Gateway's von Braun as a megastructure
    gateway_vb_index = next(i for i, station in enumerate(SPACE_STATIONS) if station['name'] == "Gateway's von Braun")
    gateway_vb = SPACE_STATIONS[gateway_vb_index]
    gateway_vb_per_person = gateway_vb['habitable_volume'] / gateway_vb['crew']
    
    # Format values with appropriate significant figures
    gateway_vb_formatted = f"{gateway_vb_per_person/1000:.1f}K"  # Format as K for thousands
    
    fig.add_trace(go.Scatter(
        x=[115],  # Position between the other megastructures
        y=[110],
        mode='markers',
        name='Megastructure',
        legendgroup='megastructure',
        showlegend=False,  # Hide this trace from the legend
        marker=dict(
            size=30,
            color='#9C27B0',
            line=dict(width=3, color='black'),
            opacity=0.9,
            symbol='star'
        ),
        hoverinfo='text',
        hovertext=f"{gateway_vb['name']}<br>Habitable Volume per Astronaut: {gateway_vb_formatted} m³<br>Total Volume: {gateway_vb['total_volume']:,.2f} m³<br>Habitable Volume: {gateway_vb['habitable_volume']:,.2f} m³<br>Pressurised Volume: {gateway_vb['pressurised_volume']:,.2f} m³<br>Crew: {gateway_vb['crew']:,}"
    ))
    
    # Add station name labels with improved positioning
    label_positions = {
        'Salyut-1': dict(xanchor='right', yanchor='bottom', xshift=-15, yshift=-10),
        'von Braun wheel': dict(xanchor='left', yanchor='bottom', xshift=15, yshift=15),
        'Hexagonal Station': dict(xanchor='left', yanchor='middle', xshift=25, yshift=0),
        'ISS': dict(xanchor='left', yanchor='bottom', xshift=15, yshift=5),
        'Gateway': dict(xanchor='right', yanchor='bottom', xshift=-15, yshift=12),
        'Tiangong': dict(xanchor='left', yanchor='middle', xshift=25, yshift=0),
        'Skylab': dict(xanchor='left', yanchor='bottom', xshift=15, yshift=5),
        'Haven-1': dict(xanchor='center', yanchor='bottom', xshift=0, yshift=15),
        'LORL': dict(xanchor='left', yanchor='top', xshift=15, yshift=-10),
        'MORL': dict(xanchor='left', yanchor='top', xshift=15, yshift=-10)
    }
    
    # Create text labels with the same legend groups
    # Real stations text
    real_station_names = [SPACE_STATIONS[i]['name'] for i in real_indices]
    real_x = [habitable_volume_per_astronaut[plot_indices.index(i)] for i in real_indices]
    real_y = [crews[plot_indices.index(i)] for i in real_indices]
    real_text_positions = [label_positions.get(name, dict(xshift=15, yshift=5)) for name in real_station_names]

    # Planned 0-g stations text
    planned_0g_station_names = [SPACE_STATIONS[i]['name'] for i in planned_0g_indices]
    planned_0g_x = [habitable_volume_per_astronaut[plot_indices.index(i)] for i in planned_0g_indices]
    planned_0g_y = [crews[plot_indices.index(i)] for i in planned_0g_indices]
    planned_0g_text_positions = [label_positions.get(name, dict(xshift=15, yshift=5)) for name in planned_0g_station_names]

    # Add text for planned 0-g stations
    for i, name in enumerate(planned_0g_station_names):
        xanchor = planned_0g_text_positions[i].get('xanchor', 'left')
        
        # Calculate better text positioning
        text_x = planned_0g_x[i]
        text_y = planned_0g_y[i]
        
        # Adjust position based on the station name
        if name == 'Gateway':
            text_position = 'top left'  # Changed to top center
            text_y += 4  # Move up even more
        elif name == 'Haven-1':
            text_position = 'top center'  # Keep top center
            text_y += 4  # Move up more
        elif name == 'Haven-2':
            text_position = 'top right'
            text_y += 3  # Move up slightly
            text_x += 3  # Move right slightly
        elif name == 'LORL':
            text_position = 'middle right'
            text_x += 4  # Move right more
            text_y -= 3  # Move down slightly
        elif name == 'MORL':
            text_position = 'top center'
            text_x += 0  # No horizontal shift
            text_y += 5  # Move up more to place it above the circle
        elif name == 'Starship':
            text_position = 'top right'
            text_x += 4  # Move right more
            text_y += -5  # Move up more
        else:
            text_position = 'middle right' if xanchor == 'left' else 'middle left'
        
        fig.add_trace(go.Scatter(
            x=[text_x],
            y=[text_y],
            text=[name],
            mode='text',
            showlegend=False,
            legendgroup='planned_0g_stations',
            textposition=text_position,
            textfont=dict(
                color='#F44336',
                size=12
            ),
            hoverinfo='skip',
            texttemplate='<span style="background-color: rgba(255,255,255,0.7); padding: 2px 4px; border-radius: 2px;">%{text}</span>'
        ))

    # Add text for real stations
    for i, name in enumerate(real_station_names):
        xanchor = real_text_positions[i].get('xanchor', 'left')
        
        # Calculate better text positioning
        text_x = real_x[i]
        text_y = real_y[i]
        
        # Adjust position based on the station name
        if name == 'ISS':
            text_position = 'middle right'  # Changed to middle right
            text_x += 4  # Move right more
        elif name == 'Skylab':
            text_position = 'bottom right'
            text_x += 4  # Move right slightly
        elif name == 'Tiangong':
            text_position = 'middle right'  # Changed to middle right
            text_x += 3.5  # Move right more
            text_y += -2  # Move up more
        elif name == 'Salyut-1':
            text_position = 'bottom left'
            text_x -= 3  # Move left slightly
        else:
            text_position = 'middle right' if xanchor == 'left' else 'middle left'
        
        fig.add_trace(go.Scatter(
            x=[text_x],
            y=[text_y],
            text=[name],
            mode='text',
            showlegend=False,
            legendgroup='real_stations',
            textposition=text_position,
            textfont=dict(
                color='#4CAF50',
                size=12
            ),
            hoverinfo='skip',
            texttemplate='<span style="background-color: rgba(255,255,255,0.7); padding: 2px 4px; border-radius: 2px;">%{text}</span>'
        ))

    # Artificial gravity stations text
    ag_station_names = [SPACE_STATIONS[i]['name'] for i in ag_indices]
    ag_x = [habitable_volume_per_astronaut[plot_indices.index(i)] for i in ag_indices]
    ag_y = [crews[plot_indices.index(i)] for i in ag_indices]
    ag_text_positions = [label_positions.get(name, dict(xshift=15, yshift=5)) for name in ag_station_names]

    # Add text for artificial gravity stations
    for i, name in enumerate(ag_station_names):
        xanchor = ag_text_positions[i].get('xanchor', 'left')
        
        # Calculate better text positioning
        text_x = ag_x[i]
        text_y = ag_y[i]
        
        # Adjust position based on the station name
        if name == 'von Braun wheel':
            text_position = 'top center'
            text_y += 7  # Move up even more
        elif name == 'Hexagonal Station':
            text_position = 'bottom right'
            text_x += 2  # Move right more
            text_y -= 4  # Move down more
        elif name == '2035 Vast Station':
            text_position = 'top right'
            text_y += 5  # Move up more
            text_x += 2  # Move right slightly
        elif name == 'Space Base':
            text_position = 'top left'
            text_x -= 3  # Move left more
            text_y += 5  # Move up more
        else:
            text_position = 'middle right' if xanchor == 'left' else 'middle left'
        
        fig.add_trace(go.Scatter(
            x=[text_x],
            y=[text_y],
            text=[name],
            mode='text',
            showlegend=False,
            legendgroup='ag_stations',
            textposition=text_position,
            textfont=dict(
                color='#2979FF',
                size=12
            ),
            hoverinfo='skip',
            texttemplate='<span style="background-color: rgba(255,255,255,0.7); padding: 2px 4px; border-radius: 2px;">%{text}</span>'
        ))

    # Add megastructure stations text
    megastructure_station_names = [SPACE_STATIONS[i]['name'] for i in megastructure_indices]

    # Add text for megastructure stations  
    for i, name in enumerate(megastructure_station_names):
        # Calculate positioning based on the station name
        if name == "Gateway's von Braun":
            text_x = 115  # Position to the left of the star
            text_y = 100
            text_position = 'middle right'
            name = "Gateway's<br>von Braun"
        elif name == "O'Neill Cylinder":
            text_x = 94  # Position to the left of the star
            text_y = 132  # Above the star
            text_position = 'middle right'
        elif name == "Stanford Torus":
            text_x = 87  # Position to the left
            text_y = 114  # Middle
            text_position = 'middle right'
        else:
            # Default positioning if we add more megastructures in the future
            text_x = 110
            text_y = 110
            text_position = 'middle right'
        
        fig.add_trace(go.Scatter(
            x=[text_x],
            y=[text_y],
            text=[name],
            mode='text',
            showlegend=False,
            legendgroup='megastructure',
            textposition=text_position,
            textfont=dict(
                color='#9C27B0',
                size=14,
                family='Arial Black'
            ),
            hoverinfo='skip',
            texttemplate='<span style="background-color: rgba(255,255,255,0.7); padding: 3px 6px; border-radius: 3px;">%{text}</span>'
        ))

    # Update layout with improved spacing and fixed axis range
    fig.update_layout(
        xaxis=dict(
            title="Habitable Volume per Astronaut (cubic meters per person)",
            type="linear",  # Using linear scale
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[5, 130],  # Changed range to 5-130
            tickmode='array',
            tickvals=[20, 40, 60, 80, 100, 110, 120],
            ticktext=["20", "40", "60", "80", "100", stanford_formatted, oneill_formatted],
        ),
        yaxis=dict(
            title="Crew Capacity (number of astronauts)",
            gridcolor='rgba(0,0,0,0)',
            zerolinecolor='rgba(0,0,0,0)',
            range=[-2, 140],  # Increased upper limit to 140
            dtick=10,
            ticktext=["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "1,000", "10,000", "1M"],
            tickvals=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
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
        'assets/plots/spaceship-engineering/spaceship-region.html',
        config={
            'responsive': True,
            'displayModeBar': False,
            'showTips': True
        },
        include_plotlyjs=True,
        full_html=False
    )
    
    # Save as PNG
    fig.write_image('assets/imgs/spaceship-engineering/spaceship-region.png', width=800, height=600, scale=2)
    
    return fig

if __name__ == "__main__":
    create_multidimensional_bubble_chart()