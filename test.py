import questionary

options = [
    {"name": "Option 1", "checked": False},
    {"name": "Option 2", "checked": False},
    {"name": "Option 3", "checked": False},
    {"name": "Option 4", "checked": False}
]

selected_options = questionary.checkbox(
    "Select options:",
    choices=options
).ask()

print("Selected options:")
for option in selected_options:
    print("- {}".format(option))
