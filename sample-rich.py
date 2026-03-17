# from rich.console import Console
# from rich.panel import Panel
# from rich.prompt import Prompt, FloatPrompt
# from rich.table import Table

# console = Console()

# # ================= FUNCTIONS =================

# def celc_to_far(c): return (c * 9/5) + 32
# def far_to_celc(f): return (f - 32) * 5/9
# def celc_to_kelvin(c): return c + 273.15
# def kelvin_to_celc(k): return k - 273.15
# def far_to_kelvin(f): return (f - 32) * 5/9 + 273.15
# def kelvin_to_far(k): return (k - 273.15) * 9/5 + 32

# def feet_to_meter(f): return f * 0.3048
# def meter_to_feet(m): return m / 0.3048

# def kg_to_pound(kg): return kg * 2.20462
# def pound_to_kg(lb): return lb / 2.20462


# # ================= UI =================

# console.print(Panel.fit("🔥 UNIT CONVERTER PRO 🔥", style="bold cyan"))

# main_table = Table(title="Main Menu", style="bold magenta")
# main_table.add_column("Option", justify="center")
# main_table.add_column("Type", justify="center")

# main_table.add_row("1", "Temperature 🌡️")
# main_table.add_row("2", "Height 📏")
# main_table.add_row("3", "Weight ⚖️")

# console.print(main_table)

# choice = int(Prompt.ask("👉 Choose conversion type (1/2/3)"))

# # ================= TEMPERATURE =================

# if choice == 1:
#     table = Table(title="Temperature Conversion", style="bold green")
#     table.add_column("Option", justify="center")
#     table.add_column("Conversion", justify="center")

#     table.add_row("1", "Celsius → Fahrenheit")
#     table.add_row("2", "Fahrenheit → Celsius")
#     table.add_row("3", "Celsius → Kelvin")
#     table.add_row("4", "Kelvin → Celsius")
#     table.add_row("5", "Fahrenheit → Kelvin")
#     table.add_row("6", "Kelvin → Fahrenheit")

#     console.print(table)

#     c = int(Prompt.ask("👉 Choose option"))

#     if c == 1:
#         val = FloatPrompt.ask("Enter Celsius")
#         res = celc_to_far(val)
#         console.print(f"✨ Result: [bold yellow]{res} °F[/]")

#     elif c == 2:
#         val = FloatPrompt.ask("Enter Fahrenheit")
#         res = far_to_celc(val)
#         console.print(f"✨ Result: [bold yellow]{res} °C[/]")

#     elif c == 3:
#         val = FloatPrompt.ask("Enter Celsius")
#         res = celc_to_kelvin(val)
#         console.print(f"✨ Result: [bold yellow]{res} K[/]")

#     elif c == 4:
#         val = FloatPrompt.ask("Enter Kelvin")
#         res = kelvin_to_celc(val)
#         console.print(f"✨ Result: [bold yellow]{res} °C[/]")

#     elif c == 5:
#         val = FloatPrompt.ask("Enter Fahrenheit")
#         res = far_to_kelvin(val)
#         console.print(f"✨ Result: [bold yellow]{res} K[/]")

#     elif c == 6:
#         val = FloatPrompt.ask("Enter Kelvin")
#         res = kelvin_to_far(val)
#         console.print(f"✨ Result: [bold yellow]{res} °F[/]")


# # ================= HEIGHT =================

# elif choice == 2:
#     table = Table(title="Height Conversion", style="bold blue")
#     table.add_column("Option", justify="center")
#     table.add_column("Conversion", justify="center")

#     table.add_row("1", "Feet → Meter")
#     table.add_row("2", "Meter → Feet")

#     console.print(table)

#     c = int(Prompt.ask("👉 Choose option"))

#     if c == 1:
#         val = FloatPrompt.ask("Enter Feet")
#         res = feet_to_meter(val)
#         console.print(f"✨ Result: [bold yellow]{res} m[/]")

#     elif c == 2:
#         val = FloatPrompt.ask("Enter Meter")
#         res = meter_to_feet(val)
#         console.print(f"✨ Result: [bold yellow]{res} ft[/]")


# # ================= WEIGHT =================

# elif choice == 3:
#     table = Table(title="Weight Conversion", style="bold red")
#     table.add_column("Option", justify="center")
#     table.add_column("Conversion", justify="center")

#     table.add_row("1", "KG → Pound")
#     table.add_row("2", "Pound → KG")

#     console.print(table)

#     c = int(Prompt.ask("👉 Choose option"))

#     if c == 1:
#         val = FloatPrompt.ask("Enter KG")
#         res = kg_to_pound(val)
#         console.print(f"✨ Result: [bold yellow]{res} lb[/]")

#     elif c == 2:
#         val = FloatPrompt.ask("Enter Pound")
#         res = pound_to_kg(val)
#         console.print(f"✨ Result: [bold yellow]{res} kg[/]")

# else:
#     console.print("[bold red]❌ Invalid choice[/]")