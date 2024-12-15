import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from django.core.exceptions import ValidationError

from robots.models import Robot

@csrf_exempt
def create_robot(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requetst are allowed"}, status=405)
    
    try:
        data = json.loads(request.body)

        required_fields = ["model", "version", "created"]
        for field in required_fields:
            if field not in data:
                return JsonResponse({"error": f"Missing required field: {field}"}, status=400)
        
        try:
            created_datetime = datetime.strptime(data["created"], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return JsonResponse({"error": "Invalid datetime format for 'created'. Expected format: YYYY-MM-DD HH:MM:SS."}, status=400)

        robot = Robot(
            model=data["model"],
            version=data["version"],
            created=created_datetime
        )

        robot.full_clean()
        robot.save()
        return JsonResponse({"message": "Robot created successfully.", "robot_id": robot.id}, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format."}, status=400)
    except ValidationError as e:
        return JsonResponse({"error": "Validation error.", "details": e.message_dict}, status=400)
    except Exception as e:
        return JsonResponse({"error": "An unexpected error occurred.", "details": str(e)}, status=500)