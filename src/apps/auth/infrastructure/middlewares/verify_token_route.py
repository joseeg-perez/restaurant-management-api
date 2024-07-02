from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from ..providers.jwt_service import JwtService

class verifyTokenRoute(APIRoute):
    def getRouteHandler(self):
        originalRoute = super().getRouteHandler()
        
        async def verify_token_middleware(request: Request):
            bearerToken = request.headers.get("Authorization")
            if token is None:
                return JSONResponse(status_code=401, content={"error": "Unauthorized"})
            token = bearerToken.split("Bearer ")[1]
            responseValidated = JwtService.validateToken(token, False)
            
            if responseValidated is not None:
                return await originalRoute(request)
            else:
                return responseValidated
        return verify_token_middleware