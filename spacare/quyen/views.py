from rest_framework.generics import ListCreateAPIView

from spacare.quyen.models import Quyen
from spacare.quyen.serializers import QuyenSerializer


class LisCreateQuyenView(ListCreateAPIView):
    model = Quyen
    serializer_class = QuyenSerializer
    queryset = Quyen.objects.all()
