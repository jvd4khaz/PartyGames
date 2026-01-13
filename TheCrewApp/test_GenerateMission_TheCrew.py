from lib_TheCrew import generate_task_cards

def test_task_generation():
    """
    Test that the task generator produces the correct number of unique cards.
    """
    print("Running test: test_task_generation...")
    
    # Test count
    count = 5
    tasks = generate_task_cards(count)
    
    if len(tasks) == count:
        print(f"SUCCESS: Generated exactly {count} tasks.")
    else:
        print(f"FAILURE: Generated {len(tasks)} tasks instead of {count}.")

    # Test uniqueness
    if len(set(tasks)) == count:
        print("SUCCESS: All tasks are unique.")
    else:
        print("FAILURE: Duplicate tasks found.")

    print(f"Sample output: {tasks}")

if __name__ == "__main__":
    test_task_generation()

