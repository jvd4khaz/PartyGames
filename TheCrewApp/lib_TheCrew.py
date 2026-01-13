import random

def get_mission_data(mission_num):
    """
    Returns the metadata for a specific mission.
    """
    # Simplified mission database for the logic engine
    missions = {
        1: {"title": "Team Building", "tasks": 1, "narrative": "Search for the unknown 9th planet begins."},
        2: {"title": "Control Technique", "tasks": 2, "narrative": "Coordinating mental connections."},
        3: {"title": "Energy Supply", "tasks": 2, "tokens": ["1", "2"], "narrative": "Mathematical background required."},
        # ... more missions can be added here
    }
    return missions.get(mission_num, missions[1])

def generate_task_cards(count):
    """
    Randomly generates a set of task cards from the 36 available color cards.
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    available_cards = [f"{s} {v}" for s in suits for v in range(1, 10)]
    
    random.shuffle(available_cards)
    return available_cards[:count]

def format_mission_output(mission_info, task_cards):
    """
    Formats the mission details into a readable string.
    """
    output = []
    output.append("=" * 40)
    output.append(f"MISSION {mission_info['title'].upper()}")
    output.append("-" * 40)
    output.append(f"Narrative: {mission_info['narrative']}")
    output.append("-" * 40)
    output.append("TASKS TO COMPLETE:")
    
    tokens = mission_info.get('tokens', [])
    for i, card in enumerate(task_cards):
        token_str = f" [Token: {tokens[i]}]" if i < len(tokens) else ""
        output.append(f" - {card}{token_str}")
    
    output.append("=" * 40)
    return "\n".join(output)

