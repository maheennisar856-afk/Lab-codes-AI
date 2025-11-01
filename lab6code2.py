# Smart Light Reflex Agent

def smart_light_agent(presence, light_level):
    """
    Rules:
    - If person present and light level is low → Turn ON
    - If no person or light level is high → Turn OFF
    - Otherwise → Keep light as is
    """
    if presence and light_level == "low":
        return "Turn ON the light"
    elif not presence or light_level == "high":
        return "Turn OFF the light"
    else:
        return "Keep the light as is"


# Simulate different conditions
scenarios = [
    (True, "low"),
    (True, "medium"),
    (True, "high"),
    (False, "low"),
    (False, "high")
]

print("SMART LIGHT AGENT SIMULATION\n")
for i, (presence, light) in enumerate(scenarios, start=1):
    action = smart_light_agent(presence, light)
    print(f"Scenario {i}: Presence={presence}, Light Level='{light}' → Action: {action}")
