"""
ems_algorithm.py

Rule-based Energy Management System for a hybrid microgrid.

System components:
- PV generation
- Wind generation
- Battery energy storage
- Generator
- Grid connection
- Critical and non-critical loads
"""


def energy_management_system(
    pv_power,
    wind_power,
    load_demand,
    battery_soc,
    grid_available,
    electricity_price
):
    """
    Rule-based EMS decision algorithm.

    Parameters:
        pv_power (float): PV power generation in kW
        wind_power (float): Wind power generation in kW
        load_demand (float): Total load demand in kW
        battery_soc (float): Battery state of charge in %
        grid_available (bool): Grid status
        electricity_price (float): Electricity price value

    Returns:
        dict: EMS operation decision
    """

    renewable_power = pv_power + wind_power

    soc_min = 20
    soc_max = 90
    low_price_limit = 1.5

    decision = {
        "renewable_power": renewable_power,
        "battery_action": "Idle",
        "grid_action": "Not used",
        "generator_action": "Not used",
        "critical_load_status": "Supplied",
        "non_critical_load_status": "Supplied",
        "system_status": ""
    }

    # Case 1: Renewable energy is enough
    if renewable_power >= load_demand:
        decision["system_status"] = "Load supplied by renewable energy"

        if battery_soc < soc_max:
            decision["battery_action"] = "Charging with surplus renewable energy"
        else:
            decision["battery_action"] = "Idle, battery is full"

    # Case 2: Renewable energy is not enough
    else:
        remaining_load = load_demand - renewable_power

        if battery_soc > soc_min:
            decision["battery_action"] = "Discharging to support the load"
            remaining_load -= 20
        else:
            decision["battery_action"] = "Battery SOC is low"

        if remaining_load > 0 and grid_available:
            decision["grid_action"] = "Grid support is used"
            decision["system_status"] = "Renewable energy, battery and grid are used"

        elif remaining_load > 0 and not grid_available:
            decision["generator_action"] = "Generator is activated"
            decision["system_status"] = "Grid outage, generator support is used"

            if remaining_load > 40:
                decision["non_critical_load_status"] = "Disconnected"
                decision["system_status"] = (
                    "Critical loads are supplied, non-critical loads are disconnected"
                )

    # Optional low-price charging strategy
    if grid_available and electricity_price <= low_price_limit and battery_soc < soc_max:
        decision["battery_action"] = "Charging from grid due to low electricity price"

    return decision


# Example operation
if __name__ == "__main__":
    result = energy_management_system(
        pv_power=35,
        wind_power=20,
        load_demand=80,
        battery_soc=65,
        grid_available=True,
        electricity_price=2.0
    )

    print("Energy Management System Decision")
    print("---------------------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
