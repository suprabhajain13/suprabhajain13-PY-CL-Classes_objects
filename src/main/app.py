# app.py

from lab import create_bulb

if __name__ == "__main__":
    container = []  # List to store created lightbulbs
    counter = 0

    # Example usage
    bulb1 = create_bulb(True)  # Turn on the lightbulb
    container.append(bulb1)
    print("Lightbulb 1 created.")
    print(bulb1.get_description())

    bulb2 = create_bulb(False)  # Turn off the lightbulb
    container.append(bulb2)
    print("Lightbulb 2 created.")
    print(bulb2.get_description())
