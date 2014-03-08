from product.models import Object

def get_objects(request):
    ln = Object.objects.all()

    return {'objects_list': ln} 