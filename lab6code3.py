import random
import time

class ThermostatAgent:
    def __init__(self):
        self.memory = []       # store last few temperature readings
        self.current_temp = random.randint(18, 26)  # start temperature

    def sense_temperature(self):
        # simulate small random change
        self.current_temp += random.choice([-1, 0, 1])
        self.memory.append(self.current_temp)
        if len(self.memory) > 5:  # keep last 5 readings
            self.memory.pop(0)
        return self.current_temp

    def predict_trend(self):
        if len(self.memory) < 2:
            return "stable"
        diff = self.memory[-1] - self.memory[0]
        if diff > 2:
            return "rising"
        elif diff < -2:
            return "falling"
        else:
            return "stable"

    def act(self):
        trend = self.predict_trend()
        temp = self.current_temp

        if temp < 20 or (temp <= 21 and trend == "falling"):
            action = "Turn ON heater"
        elif temp > 24 or (temp >= 23 and trend == "rising"):
            action = "Turn ON cooler"
        else:
            action = "Maintain temperature"

        print(f"Temperature = {temp}°C | Trend = {trend} | Action = {action}")


# Run simulation
agent = ThermostatAgent()
print("\nTHERMOSTAT AGENT SIMULATION\n")
for i in range(10):
    agent.sense_temperature()
    agent.act()
    time.sleep(0.5)
