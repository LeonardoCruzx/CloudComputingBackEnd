from rest_framework.decorators import api_view

from cloudinary_app.my_image import MyImage
from cloudinary_app.serializers import MyImageSerializer

from rest_framework.response import Response

import cloudinary.api as ca
# Create your views here.

@api_view(["GET"])
def get_all_imgs(request, *args, **kwargs):
    data = ca.resources(
        type = "upload",
        prefix = kwargs["folder"]
    )
    images = []
    for i in data["resources"]:
        images.append(MyImageSerializer(MyImage(i["url"], i["public_id"], i["width"], i["height"], i["bytes"] // 1024)).data)
    return Response(images)
