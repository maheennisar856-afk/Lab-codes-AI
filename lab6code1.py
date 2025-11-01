import random
import time

# Step 1: Define the environment with three rooms
environment = {
    "A": random.choice(["Clean", "Dirty"]),
    "B": random.choice(["Clean", "Dirty"]),
    "C": random.choice(["Clean", "Dirty"])
}

# Step 2: Initialize agent properties
agent_location = random.choice(["A", "B", "C"])
clean_counter = 0

print("Initial Environment State:", environment)
print(f"Agent starting in Room {agent_location}\n")

# Step 3: Agent behavior loop
for step in range(10):  # limit steps for readability
    print(f"Step {step + 1}: Agent is in Room {agent_location}")

    # Sense and act
    if environment[agent_location] == "Dirty":
        print(f"🧹 Cleaning Room {agent_location}...")
        environment[agent_location] = "Clean"
        clean_counter += 1
    else:
        print(f"✅ Room {agent_location} is already clean.")

    # Step 4: Decide where to move next
    if all(status == "Clean" for status in environment.values()):
        print("✨ All rooms are clean! Moving randomly...")
        agent_location = random.choice(["A", "B", "C"])
    else:
        # Move to next room in order (A→B→C→A)
        next_room = {"A": "B", "B": "C", "C": "A"}
        agent_location = next_room[agent_location]

    # Display current environment state
    print("Current Environment:", environment)
    print("🧮 Clean Counter:", clean_counter)
    print("-" * 40)
    time.sleep(1)

# Step 5: Display final summary
print("\nFinal Environment State:", environment)
print("Total Clean Actions Performed:", clean_counter)
