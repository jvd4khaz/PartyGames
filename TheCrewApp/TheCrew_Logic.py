import random
from lib_TheCrew import get_mission_data, generate_task_cards, format_mission_output

# Configuration
PLAYER_COUNT = 4
CURRENT_MISSION = 1

# 1. Fetch data for the current mission
mission_info = get_mission_data(CURRENT_MISSION)

# 2. Generate random task cards for the mission
task_cards = generate_task_cards(mission_info['tasks'])

# 3. Produce and print the final output
output = format_mission_output(mission_info, task_cards)
print(output)

