from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from main.models import MARK_CHOICES, Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        ser = ProductDetailsSerializer(product)
        return Response(ser.data)


class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        get_object_or_404(Product, id=product_id)
        mark = request.GET.get('mark')
        reviews = Review.objects.filter(product_id=product_id)

        if mark:
            try:
                mark = int(mark)
            except ValueError:
                return Response({"error": "Параметр 'mark' должен быть числом"}, status=400)
            reviews = reviews.filter(product_id=product_id, mark=mark)

        ser = ReviewSerializer(reviews, many=True)
        return Response(ser.data)
