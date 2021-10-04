import random

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from colors.models import ColorSpace


class GetColorsAPI(generics.GenericAPIView):
    permission_classes = []
    queryset = ColorSpace.objects.all()

    def get(self, request, *args, **kwargs):
        spaces = list(ColorSpace.objects.all())
        size = int(request.GET.get('size', '5'))

        response_data = []
        for i in range(size):
            space = spaces[random.randint(0, len(spaces) - 1)]
            space_data = {
                'type': space.name,
            }
            for field in space.fields.all():
                space_data.update({
                    field.name: random.randint(field.min_value, field.max_value)
                })

            response_data.append(space_data)

        return Response(response_data)
