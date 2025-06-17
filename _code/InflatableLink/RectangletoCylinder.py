import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import matplotlib.animation as animation

class InflatableCylinder:
    def __init__(self, flat_width, flat_length, wall_thickness, young_modulus):
        """
        Initialize flat rectangular panel that will become a cylinder
        
        Parameters:
        flat_width: width of flat rectangle (becomes circumference)
        flat_length: length of flat rectangle (stays as cylinder length)
        wall_thickness: material thickness
        young_modulus: material stiffness (Pa)
        """
        self.flat_width = flat_width
        self.flat_length = flat_length
        self.wall_thickness = wall_thickness
        self.E = young_modulus
        
        # Initial cylinder geometry (no pressure)
        self.initial_radius = flat_width / (2 * np.pi)
        self.initial_circumference = flat_width
        self.length = flat_length
        
        # Current state
        self.current_radius = self.initial_radius
        self.current_pressure = 0
        
    def apply_pressure(self, pressure):
        """Calculate new cylinder dimensions under pressure"""
        self.current_pressure = pressure
        
        if pressure == 0:
            self.current_radius = self.initial_radius
            return
            
        # Hoop stress: σ_h = P*r/t
        # Hoop strain: ε_h = σ_h/E = P*r/(E*t)
        # New radius: r_new = r*(1 + ε_h) = r*(1 + P*r/(E*t))
        
        # This creates a nonlinear equation: r_new = r_initial*(1 + P*r_new/(E*t))
        # Solve iteratively
        r = self.initial_radius
        for _ in range(10):  # Simple iteration
            strain_hoop = pressure * r / (self.E * self.wall_thickness)
            r = self.initial_radius * (1 + strain_hoop)
            
        self.current_radius = r
        
    def get_stresses(self):
        """Calculate hoop and axial stresses"""
        if self.current_pressure == 0:
            return 0, 0
            
        # Thin-wall pressure vessel equations
        hoop_stress = self.current_pressure * self.current_radius / self.wall_thickness
        axial_stress = self.current_pressure * self.current_radius / (2 * self.wall_thickness)
        
        return hoop_stress, axial_stress
    
    def get_strains(self):
        """Calculate hoop and axial strains"""
        hoop_stress, axial_stress = self.get_stresses()
        
        # For thin cylinder: ε_hoop = σ_hoop/E, ε_axial = σ_axial/E
        hoop_strain = hoop_stress / self.E
        axial_strain = axial_stress / self.E
        
        return hoop_strain, axial_strain

def visualize_transformation(cylinder, pressures):
    """Visualize flat panel → cylinder transformation"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # Subplot 1: Flat panel
    ax1.set_title("1. Flat Panel (Initial)")
    ax1.add_patch(Rectangle((0, 0), cylinder.flat_width, cylinder.flat_length, 
                           fill=False, edgecolor='blue', linewidth=2))
    ax1.set_xlim(-0.5, cylinder.flat_width + 0.5)
    ax1.set_ylim(-0.5, cylinder.flat_length + 0.5)
    ax1.set_xlabel("Width (becomes circumference)")
    ax1.set_ylabel("Length")
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    # Subplot 2: Cylinder cross-section
    ax2.set_title("2. Cylinder Cross-Section")
    colors = ['blue', 'orange', 'red', 'purple']
    
    for i, pressure in enumerate(pressures):
        cylinder.apply_pressure(pressure)
        circle = Circle((0, 0), cylinder.current_radius, 
                       fill=False, edgecolor=colors[i], linewidth=2,
                       label=f'P = {pressure/1000:.1f} kPa')
        ax2.add_patch(circle)
    
    max_radius = max([cylinder.current_radius for p in pressures 
                     for _ in [cylinder.apply_pressure(p)]])
    ax2.set_xlim(-max_radius*1.2, max_radius*1.2)
    ax2.set_ylim(-max_radius*1.2, max_radius*1.2)
    ax2.set_xlabel("Radius (m)")
    ax2.set_ylabel("Radius (m)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_aspect('equal')
    
    # Subplot 3: Stress vs Pressure
    ax3.set_title("3. Stress vs Pressure")
    pressure_range = np.linspace(0, max(pressures), 50)
    hoop_stresses = []
    axial_stresses = []
    
    for p in pressure_range:
        cylinder.apply_pressure(p)
        h_stress, a_stress = cylinder.get_stresses()
        hoop_stresses.append(h_stress)
        axial_stresses.append(a_stress)
    
    ax3.plot(pressure_range/1000, np.array(hoop_stresses)/1e6, 'r-', 
             label='Hoop Stress', linewidth=2)
    ax3.plot(pressure_range/1000, np.array(axial_stresses)/1e6, 'b-', 
             label='Axial Stress', linewidth=2)
    ax3.set_xlabel("Pressure (kPa)")
    ax3.set_ylabel("Stress (MPa)")
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Subplot 4: Radius vs Pressure
    ax4.set_title("4. Deformation vs Pressure")
    radii = []
    for p in pressure_range:
        cylinder.apply_pressure(p)
        radii.append(cylinder.current_radius)
    
    ax4.plot(pressure_range/1000, radii, 'g-', linewidth=2)
    ax4.axhline(y=cylinder.initial_radius, color='g', linestyle='--', 
                alpha=0.7, label='Initial radius')
    ax4.set_xlabel("Pressure (kPa)")
    ax4.set_ylabel("Radius (m)")
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def demonstrate_concepts():
    """Run the demonstration"""
    print("=== Inflatable Cylinder Simulation ===")
    print()
    
    # Material properties (example: rubber-like material)
    young_modulus = 5e6  # Pa (5 MPa - flexible material)
    wall_thickness = 0.002  # 2mm
    
    # Geometry
    flat_width = 1.0  # 1m wide rectangle
    flat_length = 0.5  # 0.5m long rectangle
    
    # Create cylinder
    cylinder = InflatableCylinder(flat_width, flat_length, wall_thickness, young_modulus)
    
    print(f"Initial flat panel: {flat_width}m × {flat_length}m")
    print(f"Initial cylinder radius: {cylinder.initial_radius:.3f}m")
    print(f"Material: E = {young_modulus/1e6:.1f} MPa, t = {wall_thickness*1000:.1f}mm")
    print()
    
    # Test different pressures
    test_pressures = [0, 5000, 10000, 15000]  # Pa
    
    print("Pressure Analysis:")
    print("Pressure (kPa) | Radius (m) | Hoop Stress (MPa) | Axial Stress (MPa)")
    print("-" * 70)
    
    for pressure in test_pressures:
        cylinder.apply_pressure(pressure)
        hoop_stress, axial_stress = cylinder.get_stresses()
        
        print(f"{pressure/1000:10.1f} | {cylinder.current_radius:8.3f} | "
              f"{hoop_stress/1e6:13.2f} | {axial_stress/1e6:14.2f}")
    
    print()
    print("Key Insights:")
    print("1. Hoop stress = 2 × Axial stress (thin cylinder theory)")
    print("2. As pressure increases, radius increases (material stretches)")
    print("3. Higher radius → higher stress for same pressure")
    print("4. Material stiffness (E) controls how much expansion occurs")
    
    # Create visualization
    fig = visualize_transformation(cylinder, test_pressures)
    plt.show()
    
    return cylinder

# Run the demonstration
if __name__ == "__main__":
    cylinder = demonstrate_concepts()