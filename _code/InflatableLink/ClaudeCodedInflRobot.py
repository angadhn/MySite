import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class InflatablePendulum:
    """
    Simple first-principles model of pressure-driven pendulum motion.
    
    Key idea: Pressure creates asymmetric forces -> net moment -> rotation
    """
    
    def __init__(self, length=1.0, mass=0.1, moment_arm_coeff=0.1):
        self.L = length  # pendulum length
        self.m = mass    # mass of inflatable link
        self.g = 9.81    # gravity
        self.k_moment = moment_arm_coeff  # how efficiently pressure creates moment
        
        # Pressure dynamics parameters  
        self.pressure_threshold = 10.0  # pressure needed to start motion (Pa)
        self.max_pressure = 100.0       # maximum sustainable pressure
        
    def pressure_to_moment(self, pressure, theta):
        """
        Convert internal pressure to bending moment.
        
        This is the key relationship you want to characterize experimentally!
        
        Simple model: moment is proportional to (pressure - threshold)
        when pressure exceeds threshold, zero otherwise.
        """
        if pressure < self.pressure_threshold:
            return 0.0
        
        # Effective pressure above threshold
        p_eff = pressure - self.pressure_threshold
        
        # Moment arm depends on current angle (geometric nonlinearity)
        moment_arm = self.k_moment * np.cos(theta)
        
        # Net moment (this is what you'd measure experimentally)
        return p_eff * moment_arm
    
    def pendulum_dynamics(self, state, t, pressure_input):
        """
        Equation of motion for pressure-driven pendulum.
        
        state = [theta, theta_dot]
        """
        theta, theta_dot = state
        
        # External moment from pressure
        M_pressure = self.pressure_to_moment(pressure_input(t), theta)
        
        # Gravitational restoring moment
        M_gravity = -self.m * self.g * self.L * np.sin(theta)
        
        # Simple damping
        M_damping = -0.1 * theta_dot
        
        # Total moment
        M_total = M_pressure + M_gravity + M_damping
        
        # Angular acceleration (assuming point mass)
        I = self.m * self.L**2  # moment of inertia
        theta_ddot = M_total / I
        
        return [theta_dot, theta_ddot]
    
    def simulate(self, pressure_profile, time_span, initial_conditions=[0.0, 0.0]):
        """Simulate the pressure-driven pendulum motion."""
        
        # Solve the differential equation
        solution = odeint(self.pendulum_dynamics, initial_conditions, 
                         time_span, args=(pressure_profile,))
        
        return {
            'time': time_span,
            'theta': solution[:, 0],
            'theta_dot': solution[:, 1],
            'tip_x': self.L * np.sin(solution[:, 0]),
            'tip_y': -self.L * np.cos(solution[:, 0])
        }

def step_pressure_input(t):
    """Step pressure input - sudden inflation."""
    return 50.0 if t > 1.0 else 0.0

def ramp_pressure_input(t):
    """Gradual pressure increase."""
    return min(60.0, 20.0 * t) if t > 0.5 else 0.0

    def visualize_pendulum(self, result, pressure_profile, save_animation=False):
        """
        Create animated visualization of the inflatable pendulum.
        
        Shows:
        - Pivot point (black dot)
        - Inflatable link (thickness varies with pressure)
        - Tip mass (red circle) 
        - Trajectory trace
        - Pressure indicator
        """
        from matplotlib.animation import FuncAnimation
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Setup pendulum animation (left plot)
        ax1.set_xlim(-1.5, 1.5)
        ax1.set_ylim(-1.5, 0.5)
        ax1.set_aspect('equal')
        ax1.grid(True, alpha=0.3)
        ax1.set_title('Inflatable Pendulum Actuator')
        ax1.set_xlabel('X position (m)')
        ax1.set_ylabel('Y position (m)')
        
        # Static elements
        pivot_point = ax1.plot(0, 0, 'ko', markersize=8, label='Pivot')[0]
        
        # Dynamic elements (will be updated in animation)
        actuator_line, = ax1.plot([], [], 'b-', linewidth=1, label='Inflatable Link')
        tip_mass, = ax1.plot([], [], 'ro', markersize=8, label='Tip Mass')
        trajectory, = ax1.plot([], [], 'r--', alpha=0.5, linewidth=1, label='Trajectory')
        
        ax1.legend(loc='upper right')
        
        # Setup pressure plot (right plot)
        ax2.plot(result['time'], [pressure_profile(t) for t in result['time']], 'g-', linewidth=2)
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Pressure (Pa)')
        ax2.set_title('Pressure Input Profile')
        ax2.grid(True, alpha=0.3)
        
        # Add vertical line to track time
        time_line = ax2.axvline(x=0, color='red', linestyle='--', alpha=0.7)
        
        # Store trajectory points for tracing
        trajectory_x, trajectory_y = [], []
        
        def animate(frame):
            # Current time and state
            t_current = result['time'][frame]
            x_tip = result['tip_x'][frame]
            y_tip = result['tip_y'][frame]
            
            # Current pressure and actuator properties
            current_pressure = pressure_profile(t_current)
            
            # Actuator thickness based on pressure (visual feedback)
            base_thickness = 2
            pressure_ratio = min(1.0, current_pressure / self.max_pressure)
            thickness = base_thickness + 4 * pressure_ratio
            
            # Color intensity based on pressure
            color_intensity = 0.3 + 0.7 * pressure_ratio
            actuator_color = (0, 0, color_intensity)
            
            # Update actuator link
            actuator_line.set_data([0, x_tip], [0, y_tip])
            actuator_line.set_linewidth(thickness)
            actuator_line.set_color(actuator_color)
            
            # Update tip mass
            tip_mass.set_data([x_tip], [y_tip])
            
            # Update trajectory trace
            trajectory_x.append(x_tip)
            trajectory_y.append(y_tip)
            # Keep only recent history for cleaner visualization
            if len(trajectory_x) > 200:
                trajectory_x.pop(0)
                trajectory_y.pop(0)
            trajectory.set_data(trajectory_x, trajectory_y)
            
            # Update time line in pressure plot
            time_line.set_xdata([t_current, t_current])
            
            # Add pressure text indicator
            ax1.set_title(f'Inflatable Pendulum (P = {current_pressure:.1f} Pa, t = {t_current:.2f}s)')
            
            return actuator_line, tip_mass, trajectory, time_line
        
        # Create animation
        anim = FuncAnimation(fig, animate, frames=len(result['time']), 
                           interval=50, blit=False, repeat=True)
        
        if save_animation:
            anim.save('inflatable_pendulum.gif', writer='pillow', fps=20)
            print("Animation saved as 'inflatable_pendulum.gif'")
        
        plt.tight_layout()
        plt.show()
        return anim

def visualize_actuator_concept():
    """
    Static visualization showing the concept of asymmetric inflation.
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # State 1: Deflated
    ax1.add_patch(plt.Rectangle((-0.1, -1), 0.2, 1, facecolor='lightblue', 
                               edgecolor='black', alpha=0.7))
    ax1.plot(0, 0, 'ko', markersize=8)  # Pivot
    ax1.plot(0, -1, 'ro', markersize=8)  # Tip
    ax1.set_xlim(-0.8, 0.8)
    ax1.set_ylim(-1.2, 0.2)
    ax1.set_aspect('equal')
    ax1.set_title('Deflated\n(Hangs Straight)')
    ax1.grid(True, alpha=0.3)
    
    # State 2: Partially inflated (asymmetric)
    # Simulate aeroMorph-style asymmetric inflation
    theta_bend = np.pi/8  # Small bend angle
    segments = np.linspace(0, 1, 20)
    
    for i, s in enumerate(segments):
        # Asymmetric thickness (thicker on one side)
        thickness_left = 0.08 + 0.05 * s * np.sin(np.pi * s)
        thickness_right = 0.08 + 0.02 * s
        
        y = -s
        x_center = 0.1 * s * np.sin(theta_bend * s)
        
        # Draw asymmetric cross-section
        ax2.plot([x_center - thickness_left, x_center + thickness_right], [y, y], 
                'b-', linewidth=3, alpha=0.7)
    
    ax2.plot(0, 0, 'ko', markersize=8)  # Pivot
    tip_x = 0.1 * np.sin(theta_bend)
    tip_y = -1
    ax2.plot(tip_x, tip_y, 'ro', markersize=8)  # Tip
    ax2.arrow(0.2, -0.5, 0.1, 0.05, head_width=0.05, head_length=0.03, 
             fc='red', ec='red')
    ax2.text(0.35, -0.45, 'Bending\nMoment', fontsize=10, color='red')
    ax2.set_xlim(-0.8, 0.8)
    ax2.set_ylim(-1.2, 0.2)
    ax2.set_aspect('equal')
    ax2.set_title('Inflating\n(Creates Moment)')
    ax2.grid(True, alpha=0.3)
    
    # State 3: Fully actuated
    theta_final = np.pi/4
    x_final = np.sin(theta_final)
    y_final = -np.cos(theta_final)
    
    # Draw curved actuator
    angles = np.linspace(0, theta_final, 20)
    radii = np.linspace(0, 1, 20)
    for i, (angle, radius) in enumerate(zip(angles, radii)):
        thickness = 0.15 + 0.05 * np.sin(np.pi * i / 20)
        x = radius * np.sin(angle)
        y = -radius * np.cos(angle)
        ax3.plot(x, y, 'bo', markersize=thickness*30, alpha=0.7)
    
    ax3.plot(0, 0, 'ko', markersize=8)  # Pivot
    ax3.plot(x_final, y_final, 'ro', markersize=8)  # Tip
    
    # Show trajectory arc
    arc_angles = np.linspace(0, theta_final, 50)
    arc_x = np.sin(arc_angles)
    arc_y = -np.cos(arc_angles)
    ax3.plot(arc_x, arc_y, 'r--', alpha=0.5, linewidth=2)
    
    ax3.set_xlim(-0.8, 0.8)
    ax3.set_ylim(-1.2, 0.2)
    ax3.set_aspect('equal')
    ax3.set_title('Fully Actuated\n(Large Deflection)')
    ax3.grid(True, alpha=0.3)
    
    plt.suptitle('Inflatable Pendulum Actuator Concept\n(AeroMorph-Style Asymmetric Inflation)', 
                fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# Example simulation with visualization
if __name__ == "__main__":
    # Create pendulum model
    pendulum = InflatablePendulum(length=1.0, mass=0.1, moment_arm_coeff=0.05)
    
    # Time vector
    t = np.linspace(0, 5, 1000)
    
    # Show the concept first
    print("Showing actuator concept...")
    visualize_actuator_concept()
    
    # Simulate with step input
    result_step = pendulum.simulate(step_pressure_input, t)
    
    # Create animated visualization
    print("Creating animated simulation...")
    anim = pendulum.visualize_pendulum(result_step, step_pressure_input, save_animation=False)
    
    # Plot analysis results
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    
    # Pressure inputs
    ax1.plot(t, [step_pressure_input(ti) for ti in t], 'r-', label='Step')
    ax1.plot(t, [ramp_pressure_input(ti) for ti in t], 'b-', label='Ramp')
    ax1.set_ylabel('Pressure (Pa)')
    ax1.set_title('Pressure Inputs')
    ax1.legend()
    ax1.grid(True)
    
    # Angular response
    result_ramp = pendulum.simulate(ramp_pressure_input, t)
    ax2.plot(result_step['time'], np.degrees(result_step['theta']), 'r-', label='Step')
    ax2.plot(result_ramp['time'], np.degrees(result_ramp['theta']), 'b-', label='Ramp')
    ax2.set_ylabel('Angle (degrees)')
    ax2.set_title('Angular Response')
    ax2.legend()
    ax2.grid(True)
    
    # Tip trajectory (step input)
    ax3.plot(result_step['tip_x'], result_step['tip_y'], 'r-')
    ax3.set_xlabel('X position')
    ax3.set_ylabel('Y position') 
    ax3.set_title('Tip Trajectory (Step Input)')
    ax3.axis('equal')
    ax3.grid(True)
    
    # Phase plot
    ax4.plot(np.degrees(result_step['theta']), result_step['theta_dot'], 'r-', label='Step')
    ax4.plot(np.degrees(result_ramp['theta']), result_ramp['theta_dot'], 'b-', label='Ramp')
    ax4.set_xlabel('Angle (degrees)')
    ax4.set_ylabel('Angular velocity (rad/s)')
    ax4.set_title('Phase Plot')
    ax4.legend()
    ax4.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # Print some insights
    print("Key insights from the simulation:")
    print(f"- Step input creates oscillatory motion with peak angle: {np.degrees(np.max(result_step['theta'])):.1f}°")
    print(f"- Ramp input creates more controlled motion with peak angle: {np.degrees(np.max(result_ramp['theta'])):.1f}°")
    print("\nThe crucial function to characterize experimentally is pressure_to_moment()!")
    print("This captures how your aeroMorph actuator converts pressure to bending moment.")