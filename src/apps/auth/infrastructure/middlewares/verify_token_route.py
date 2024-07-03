from fastapi import Request, HTTPException
from fastapi.routing import APIRoute
from ..providers.jwt_service import JwtService

class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()
        async def verify_token_middleware(request: Request):
            if "Authorization" not in request.headers:
                raise HTTPException(status_code=401, detail="Unauthorized")
            token = request.headers["Authorization"].split(" ")[1]
            validation_response = JwtService.validateToken(token, output=False)
            if validation_response is None:
                return await original_route(request)
            else:
                raise HTTPException(status_code=401, detail="Invalid token")
        return verify_token_middleware