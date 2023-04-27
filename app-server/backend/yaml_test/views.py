from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#class OpenAPISchemaView(APIView):
#    permission_classes = [permissions.AllowAny]
#
#    @swagger_auto_schema(
#        responses={
#            200: openapi.Response(
#                description="OpenAPI schema",
#                content={"application/json": {"schema": openapi.Schema(type="object")}},
#            )
#        }
#    )
#    def get(self, request, format=None):
#        generator = SchemaGenerator(
#            title="Your API Title", description="Your API description"
#        )
#        schema = generator.get_schema(request=request)
#        return Response(schema)
# Create your views here.
