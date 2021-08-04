from rest_framework.decorators import api_view

from cloudinary_app.my_image import MyImage
from cloudinary_app.serializers import MyImageSerializer

from rest_framework.response import Response

import cloudinary as cd
import cloudinary.api as ca
import cloudinary.uploader as up

import uuid
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

@api_view(["POST"])
def upload_categorized_img(request, *args, **kwargs):

    if (request.FILES.get('img', None) is not None):
        imgFile = request.FILES['img']
        img = up.upload(
            imgFile,
            folder = kwargs["folder"],
            public_id = uuid.uuid4(),
            overwrite = True,
            categorization = "google_tagging",
            auto_tagging = 0.6
        )
        return Response(MyImageSerializer(MyImage(img["url"], img["public_id"], img["width"], img["height"], img["bytes"] // 1024)).data)

    return Response("Nenhum arquivo enviado para o cloudinary!")


@api_view(["GET"])
def get_img_with_effect(request, *args, **kwargs):
    img = cd.CloudinaryImage(f"{kwargs['folder']}/{kwargs['id']}").image(transformation=[
        {'aspect_ratio': "1.0", 'gravity': "face", 'width': "0.6", 'zoom': "0.7", 'crop': "thumb"},
        {'radius': "max"},
        {'color': "brown", 'effect': "outline"},
        {'color': "grey", 'effect': "shadow", 'x': 30, 'y': 55}
    ])
    return Response(img[10:-3])

@api_view(["GET"])
def get_categorized_img(request, *args, **kwargs):
    dict = cd.Search().expression(request.GET.get("tag")).execute()
    images = []
    for _, v in dict.items():
        if isinstance(v, list):
            for img in v:
                images.append(MyImageSerializer(MyImage(img["url"], img["public_id"], img["width"], img["height"], img["bytes"] // 1024)).data)
    return Response(images)


@api_view(["DELETE"])
def delete_img(request, *args, **kwargs):
    up.destroy(kwargs["folder"] + "/" + kwargs["id"])
    return Response("Deletado com sucesso!")