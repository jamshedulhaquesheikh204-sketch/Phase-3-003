"""Test script for MCP server functionality"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mcp_server import add_task, list_tasks, complete_task, update_task, delete_task

def test_mcp_functions():
    print("Testing MCP server functions...")
    
    # Test adding a task
    user_id = "test_user_123"
    result = add_task(user_id=user_id, title="Test Task", description="This is a test task")
    print(f"Add task result: {result}")
    
    task_id = result.get("id") if isinstance(result, dict) and "id" in result else result.get("task_id")
    
    if task_id:
        # Test listing tasks
        tasks = list_tasks(user_id=user_id)
        print(f"List tasks result: {tasks}")
        
        # Test updating task
        update_result = update_task(user_id=user_id, task_id=task_id, title="Updated Test Task")
        print(f"Update task result: {update_result}")
        
        # Test completing task
        complete_result = complete_task(user_id=user_id, task_id=task_id)
        print(f"Complete task result: {complete_result}")
        
        # Test deleting task
        delete_result = delete_task(user_id=user_id, task_id=task_id)
        print(f"Delete task result: {delete_result}")
    else:
        print("Failed to get task ID from add_task result")

if __name__ == "__main__":
    test_mcp_functions()