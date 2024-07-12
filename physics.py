import math


def calculate_buoyancy(V, density_fluid):
    # buoyant force = p * V * g
    buoyant_force = density_fluid * V * 9.81
    return buoyant_force


def will_it_float(V, mass):
    # density = mass / volume and since volume and acceleration due to gravity remain constant for the same object, whether or not the object will float will be determined by the density of the object. If it is less than the fluid, then the buoyant force will be greater than the object's weight and it floats. If the density is greater than the water, the buoyant force of the water is less than the object's weight and it sinks.

    # If 0 is assigned as a value, then the object does not have volume
    if V == 0:
        raise ValueError("Error: Division by Zero")
    else:
        if mass / V < 1000:
            return True
        elif mass / V == 1000:
            return "Neutrally Buoyant"
        else:
            return False


def calculate_pressure(depth):
    pressure = 1000 * 9.81 * depth
    return pressure


def calculate_acceleration(F, m):
    acceleration = F / m
    return acceleration


def calculate_angular_acceleration(tau, I):
    angular_acceleration = tau / I
    return angular_acceleration


def calculate_torque(F_magnitude, F_direction, r):
    F_direction = (F_direction * math.pi()) / 180

    torque = F_magnitude * r * math.sin(F_direction)
    return torque


def calculate_moment_of_inertia(m, r):
    moment_of_inertia = m * (r**2)
    return moment_of_inertia


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    auv_acceleration = (F_magnitude * math.cos(F_angle)) / mass
    return f"{auv_acceleration} m/s/s"


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    torque = F_magnitude * thruster_distance * math.sin(F_angle)

    angular_acceleration = torque / inertia
    return f"{angular_acceleration} rad/s/s"
