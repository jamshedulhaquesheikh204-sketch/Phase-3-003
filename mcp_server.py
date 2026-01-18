from mcp.server import FastMCP
from mcp_tools.todo_tools import add_task as add_task_impl, list_tasks as list_tasks_impl, complete_task as complete_task_impl, update_task as update_task_impl, delete_task as delete_task_impl

mcp = FastMCP()

@mcp.tool()
def add_task(user_id: str, title: str, description: str = None):
    """
    Add a new task for the user.

    Args:
        user_id: The ID of the user
        title: The title of the task
        description: Optional description of the task

    Returns:
        Dictionary containing the created task information
    """
    return add_task_impl(user_id=user_id, title=title, description=description)

@mcp.tool()
def list_tasks(user_id: str, status: str = "all"):
    """
    List tasks for the user.

    Args:
        user_id: The ID of the user
        status: Optional status filter ('all', 'pending', 'completed')

    Returns:
        List of task dictionaries
    """
    return list_tasks_impl(user_id=user_id, status=status)

@mcp.tool()
def complete_task(user_id: str, task_id: str):
    """
    Mark a task as completed.

    Args:
        user_id: The ID of the user
        task_id: The ID of the task to update

    Returns:
        Dictionary containing the updated task information
    """
    return complete_task_impl(user_id=user_id, task_id=task_id, completed=True)

@mcp.tool()
def update_task(user_id: str, task_id: str, title: str = None, description: str = None):
    """
    Update a task for the user.

    Args:
        user_id: The ID of the user
        task_id: The ID of the task to update
        title: New title (optional)
        description: New description (optional)

    Returns:
        Dictionary containing the updated task information
    """
    return update_task_impl(user_id=user_id, task_id=task_id, title=title, description=description)

@mcp.tool()
def delete_task(user_id: str, task_id: str):
    """
    Delete a task for the user.

    Args:
        user_id: The ID of the user
        task_id: The ID of the task to delete

    Returns:
        Dictionary confirming deletion
    """
    return delete_task_impl(user_id=user_id, task_id=task_id)