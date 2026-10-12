"""Calculate heat loss through a wall.

Uses the steady-state conduction formula:

    Q = U * A * (T_inside - T_outside)

where
    Q  - heat loss [W]
    U  - thermal transmittance of the wall [W/(m^2*K)]
    A  - wall area [m^2]
    T  - temperature [degrees C]
"""

T_INSIDE = 20.0     # degrees C
T_OUTSIDE = -13.0   # degrees C
DEFAULT_U = 0.28    # W/(m^2*K), typical insulated wall


def heat_loss(width, height, u_value=DEFAULT_U,
              t_inside=T_INSIDE, t_outside=T_OUTSIDE):
    """Return heat loss in watts through a wall of the given size in metres."""
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive.")
    if u_value <= 0:
        raise ValueError("U-value must be positive.")
    area = width * height
    return u_value * area * (t_inside - t_outside)


def read_positive(prompt, default=None):
    while True:
        text = input(prompt).strip().replace(",", ".")
        if not text and default is not None:
            return default
        try:
            value = float(text)
        except ValueError:
            print("  Please enter a number.")
            continue
        if value <= 0:
            print("  Value must be greater than 0.")
            continue
        return value


def main():
    print("Heat loss through a wall")
    print(f"Inside: {T_INSIDE:g} °C, outside: {T_OUTSIDE:g} °C\n")

    width = read_positive("Wall width [m]: ")
    height = read_positive("Wall height [m]: ")
    u_value = read_positive(
        f"Wall U-value [W/m²K] (Enter for {DEFAULT_U}): ", DEFAULT_U)

    q = heat_loss(width, height, u_value)
    area = width * height

    print()
    print(f"Wall area:        {area:.2f} m²")
    print(f"Temperature diff: {T_INSIDE - T_OUTSIDE:.1f} K")
    print(f"Heat loss:        {q:.1f} W")
    print(f"Energy per day:   {q * 24 / 1000:.2f} kWh")


if __name__ == "__main__":
    main()
