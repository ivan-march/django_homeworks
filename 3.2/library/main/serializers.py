from rest_framework import serializers
from .models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orders_count'] = instance.order_set.count()
        return representation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        books = instance.books.all()
        representation['books'] = [
            {
                'author': book.author,
                'title': book.title,
                'year': book.year
            }
            for book in books
        ]
        return representation
