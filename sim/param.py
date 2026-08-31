# vehicle param — v0.1


# -----------------------------
# Physical constants
# -----------------------------

g = 9.81              # gravitational acceleration [m/s^2]


# -----------------------------
# Vehicle
# -----------------------------

mass = 0.250          # total drone mass [kg]
wheelbase = 0.135     # motor-to-motor diagonal [m]


# -----------------------------
# Propulsion
# -----------------------------

num_motors = 4
thrust_to_weight = 5.0
weight = mass * g
total_max_thrust = thrust_to_weight * weight
max_thrust_per_motor = total_max_thrust / num_motors


# -----------------------------
# Display
# -----------------------------

if __name__ == "__main__":

    print("Micro-drone parameters")
    print("----------------------")
    print(f"Mass:                  {mass:.3f} kg")
    print(f"Wheelbase:             {wheelbase:.3f} m")
    print(f"Weight:                {weight:.3f} N")
    print(f"Target T/W:            {thrust_to_weight:.1f}")
    print(f"Total max thrust:      {total_max_thrust:.3f} N")
    print(f"Max thrust per motor:  {max_thrust_per_motor:.3f} N")

# -----------------------------
# Rotational inertia
# -----------------------------

Ix = 1.8e-4       # moment of inertia about x / roll axis [kg*m^2]
Iy = 1.8e-4       # moment of inertia about y / pitch axis [kg*m^2]
Iz = 3.6e-4       # moment of inertia about z / yaw axis [kg*m^2]