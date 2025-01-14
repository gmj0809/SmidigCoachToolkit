# Wip Checker

# Define tasks and their states
tasks = [
    {"task_id": 1, "name": "Task A", "status": "To Do"},
    {"task_id": 2, "name": "Task B", "status": "In Progress"},
    {"task_id": 3, "name": "Task C", "status": "Done"},
    {"task_id": 4, "name": "Task D", "status": "In Progress"},
    {"task_id": 5, "name": "Task E", "status": "In Progress"},
    {"task_id": 6, "name": "Task F", "status": "In Progress"},
] 

# Define WIP limit
WIP_LIMIT = 3

# Count tasks in "In Progress"
in_progress_count = sum(1 for task in tasks if ["status"] == "In Progress")

# Print the count and check against WIP limit
print(f"Number of tasks in progress: {in_progress_count}")
if in_progress_count > WIP_LIMIT:
    print(f"⚠️ Warning: WIP limit exceeded! Limit: {WIP_LIMIT}, Current: {in_progress_count}")
else:
    print("✅ WIP is within the limit.")
