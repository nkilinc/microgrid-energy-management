"""
dashboard.py

Simple dashboard and result visualization for the microgrid energy management project.
This file uses the EMS algorithm and shows sample system outputs.
"""

import matplotlib.pyplot as plt

from ems_algorithm import energy_management_system


def get_sample_data():
    """
    Creates sample hourly data for the microgrid system.
    """

    data = {
        "time": list(range(24)),

        "pv_power": [
            0, 0, 0, 0, 0, 5, 15, 28, 40, 52, 60, 65,
            62, 55, 45, 32, 18, 6, 0, 0, 0, 0, 0, 0
        ],

        "wind_power": [
            18, 20, 22, 21, 19, 18, 17, 16, 18, 20, 21, 23,
            24, 22, 20, 19, 21, 25, 28, 30, 27, 24, 22, 20
        ],

        "load_demand": [
            45, 42, 40, 38, 40, 48, 55, 70, 85, 95, 100, 105,
            110, 108, 100, 92, 88, 80, 72, 65, 60, 55, 50, 48
        ],

        "battery_soc": [
            75, 73, 71, 69, 68, 67, 66, 65, 64, 63, 62, 64,
            66, 68, 70, 69, 67, 65, 62, 60, 58, 56, 54, 52
        ],

        "grid_available": [
            True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True,
            False, False, False,
            True, True, True, True, True, True
        ],

        "electricity_price": [
            1.20, 1.15, 1.10, 1.10, 1.20, 1.35, 1.60, 1.90,
            2.20, 2.35, 2.40, 2.30, 2.25, 2.20, 2.10, 2.00,
            2.15, 2.30, 2.40, 2.20, 1.90, 1.60, 1.35, 1.25
        ]
    }

    return data


def run_ems_for_sample_data(data):
    """
    Runs the EMS algorithm for each hour.
    """

    decisions = []

    for i in range(len(data["time"])):
        decision = energy_management_system(
            pv_power=data["pv_power"][i],
            wind_power=data["wind_power"][i],
            load_demand=data["load_demand"][i],
            battery_soc=data["battery_soc"][i],
            grid_available=data["grid_available"][i],
            electricity_price=data["electricity_price"][i]
        )

        decisions.append(decision)

    return decisions


def plot_results(data):
    """
    Plots PV power, wind power, load demand and battery SOC.
    """

    plt.figure(figsize=(10, 5))
    plt.plot(data["time"], data["pv_power"], label="PV Power")
    plt.plot(data["time"], data["wind_power"], label="Wind Power")
    plt.plot(data["time"], data["load_demand"], label="Load Demand")
    plt.xlabel("Time (hour)")
    plt.ylabel("Power (kW)")
    plt.title("Microgrid Power Profile")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.plot(data["time"], data["battery_soc"], label="Battery SOC")
    plt.xlabel("Time (hour)")
    plt.ylabel("SOC (%)")
    plt.title("Battery State of Charge")
    plt.legend()
    plt.grid(True)
    plt.show()


def print_decisions(data, decisions):
    """
    Prints EMS decisions for each hour.
    """

    for i, decision in enumerate(decisions):
        print(f"\nHour: {data['time'][i]}")
        print(f"PV Power: {data['pv_power'][i]} kW")
        print(f"Wind Power: {data['wind_power'][i]} kW")
        print(f"Load Demand: {data['load_demand'][i]} kW")
        print(f"Battery SOC: {data['battery_soc'][i]} %")
        print(f"Grid Available: {data['grid_available'][i]}")
        print("EMS Decision:")
        print(f"  Battery Action: {decision['battery_action']}")
        print(f"  Grid Action: {decision['grid_action']}")
        print(f"  Generator Action: {decision['generator_action']}")
        print(f"  Critical Load: {decision['critical_load_status']}")
        print(f"  Non-critical Load: {decision['non_critical_load_status']}")
        print(f"  System Status: {decision['system_status']}")


if __name__ == "__main__":
    sample_data = get_sample_data()
    ems_decisions = run_ems_for_sample_data(sample_data)

    print_decisions(sample_data, ems_decisions)
    plot_results(sample_data)
