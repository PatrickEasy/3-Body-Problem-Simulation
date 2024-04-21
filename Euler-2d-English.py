import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Planet:
    def __init__(self, x, y, radius, color, mass, vx=0, vy=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.vx = vx
        self.vy = vy
        self.orbit = [(x, y)]

def update_position(planet, dt):
    planet.x += planet.vx * dt
    planet.y += planet.vy * dt

def update_velocity(planet, force, dt):
    ax = force[0] / planet.mass
    ay = force[1] / planet.mass
    planet.vx += ax * dt
    planet.vy += ay * dt

def gravitational_force(planet1, planet2):
    G = 1.0
    dx = planet2.x - planet1.x
    dy = planet2.y - planet1.y
    distance_squared = dx**2 + dy**2
    distance = math.sqrt(distance_squared)
    force_magnitude = G * planet1.mass * planet2.mass / distance_squared
    force_x = force_magnitude * dx / distance
    force_y = force_magnitude * dy / distance
    return (force_x, force_y)

def simulate(planets, dt):
    for planet in planets:
        net_force = [0, 0]
        for other_planet in planets:
            if planet != other_planet:
                force = gravitational_force(planet, other_planet)
                net_force[0] += force[0]
                net_force[1] += force[1]
        update_velocity(planet, net_force, dt)
    for planet in planets:
        update_position(planet, dt)
        planet.orbit.append((planet.x, planet.y))

def animate(frame):
    global planets
    dt = 0.01
    simulate(planets, dt)
    ax.clear()
    
    # Add Cartesian axis lines
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    
    for planet in planets:
        ax.scatter(planet.x, planet.y, color=planet.color, s=planet.radius*100, label=f'{planet.color} Planet')
        updated_points = list(zip(*planet.orbit))
        ax.plot(updated_points[0], updated_points[1], color=planet.color, linewidth=2)

# Create Planet instances with initial coordinates and velocities
v = 1
L = 1
planet_A = Planet(-L/2, 0, 0.1, 'red', 2, v, 0)
planet_B = Planet(L/2, 0, 0.2, 'green', 2, -v / 2, v * math.sqrt(3) / 2)
planet_C = Planet(0, L * math.sqrt(3) / 2, 0.1, 'blue', 1, -v / 2, -v * math.sqrt(3) / 2)
#planet_D = Planet(0, -L * math.sqrt(3) / 2, 0.1, 'yellow', 1, v / 2, -v * math.sqrt(3) / 2)
#planet_E = Planet(L * math.sqrt(3) / 2, 0, 0.1, 'purple', 1, -v * math.sqrt(3) / 2, -v / 2)
planets = [planet_A, planet_B, planet_C]

# Set up the animation
fig, ax = plt.subplots()
ani = FuncAnimation(fig, animate, frames=range(100), interval=50)

# Display the animation
plt.show()
