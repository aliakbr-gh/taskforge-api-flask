class ApiResponse:
    def __init__(self, success=True, message="", data=None, error=None, status_code=200):
        self.success = success
        self.message = message
        self.data = data
        self.error = error
        self.status_code = status_code

    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "error": self.error
        }

    @staticmethod
    def success_response(message="Success", data=None, status_code=200):
        return ApiResponse(
            success=True,
            message=message,
            data=data,
            status_code=status_code
        )

    @staticmethod
    def error_response(message="Error", status_code=400):
        return ApiResponse(
            success=False,
            message=message,
            error="e",
            status_code=status_code
        )