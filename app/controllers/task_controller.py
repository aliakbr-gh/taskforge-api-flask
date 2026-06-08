from app.services.task_service import (
    create_task
)
from app.utils.api_response import ApiResponse

def create_task_controller(data, user_id):
    title = data.get("title")
    description = data.get("description")

    if not title:
        return ApiResponse.error_response("Title is required", 400)

    task = create_task(user_id, title, description)

    return ApiResponse.success_response(
        message="Task created",
        data={
            "id": task.id,
            "title": task.title,
            "description": task.description
        }
    )