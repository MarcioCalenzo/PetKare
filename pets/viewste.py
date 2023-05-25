from rest_framework.views import APIView, Response, Request, status
from rest_framework.pagination import PageNumberPagination
from .serializers import PetSerializer
from .models import Pet
from groups.models import Group
from traits.models import Trait


class PetView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()

        result_page = self.paginate_queryset(pets, request)

        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        # print("oi")
        # print(request.data)
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group = serializer.validated_data.pop("group")

        group_exist = Group.objects.filter(
            scientific_name__icontains=group["scientific_name"]
        )

        group_obj = (
            group_exist.first()
            if group_exist.exists()
            else Group.objects.create(scientific_name=group["scientific_name"].lower())
        )

        traits = serializer.validated_data.pop("traits")
        pet_obj = Pet.objects.create(**serializer.validated_data, group=group_obj)
        # print(traits)

        for trait in traits:
            # trait_name_lower = trait["trait_name"].lower()
            trait_exist = Trait.objects.filter(name__iexact=trait["trait_name"]).first()

            if not trait_exist:
                trait_obj = Trait.objects.create(name=trait["trait_name"])

        pet_obj.traits.add(trait_obj)

        serializer = PetSerializer(pet_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)
