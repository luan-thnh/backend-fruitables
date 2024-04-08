from rest_framework import views
from rest_framework.permissions import AllowAny
from django.http import Http404
from .models import Order, OrderDetail
from .serializers import OrderSerializer, OrderDetailSerializer
from products.models import Product
from backend_ecommerce.helpers import custom_response, parse_request  # Assuming these are defined correctly

class OrderAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return custom_response('Get all orders successfully!', 'Success', serializer.data, 200)
        except Order.DoesNotExist:
            return custom_response('Orders not found!', 'Error', None, 404)
        except Exception as e:
            return custom_response('Failed to retrieve orders!', 'Error', str(e), 500)

    def post(self, request):
        try:
            data = parse_request(request)
            user = User.objects.get(id=data['user_id'])
            order = Order.objects.create(
                receiver_name=data['receiver_name'],
                receiver_phone=data['receiver_phone'],
                receiver_address=data['receiver_address'],
                description=data['description'],
                user_id=user
            )
            serializer = OrderSerializer(order)
            return custom_response('Create order successfully!', 'Success', serializer.data, 201)
        except Exception as e:
            return custom_response('Failed to create order!', 'Error', str(e), 400)

class OrderDetailAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get_object(self, id_slug):
        try:
            return Order.objects.get(id=id_slug)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, id_slug):
        try:
            order = self.get_object(id_slug)
            serializer = OrderSerializer(order)
            return custom_response('Get all order details successfully!', 'Success', serializer.data, 200)
        except Order.DoesNotExist:
            return custom_response('Order not found!', 'Error', None, 404)
        except Exception as e:
            return custom_response('Failed to retrieve order details!', 'Error', str(e), 500)

    def put(self, request, id_slug):
        try:
            data = parse_request(request)
            order = self.get_object(id_slug)
            serializer = OrderSerializer(order, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update order successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update order failed', 'Error', serializer.errors, 400)
        except Order.DoesNotExist:
            return custom_response('Order not found!', 'Error', None, 404)
        except Exception as e:
            return custom_response('Failed to update order!', 'Error', str(e), 500)

    def delete(self, request, id_slug):
        try:
            order = self.get_object(id_slug)
            order.delete()
            return custom_response('Delete order successfully!', 'Success', {"order_id": id_slug}, 204)
        except Order.DoesNotExist:
            return custom_response('Order not found!', 'Error', None, 404)
        except Exception as e:
            return custom_response('Failed to delete order!', 'Error', str(e), 500)

class OrderDetailWithProductAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, order_id_slug):
        try:
            order_details = OrderDetail.objects.filter(order_id=order_id_slug).all()
            serializer = OrderDetailSerializer(order_details, many=True)
            return custom_response('Get all order details successfully!', 'Success', serializer.data, 200)
        except OrderDetail.DoesNotExist:
            return custom_response('Order details not found!', 'Error', None, 404)
        except Exception as e:
            return custom_response('Failed to retrieve order details!', 'Error', str(e), 500)

    def post(self, request, order_id_slug):
        try:
            data = parse_request(request)
            order = Order.objects.get(id=data['order_id'])
            product = Product.objects.get(id=data['product_id'])
            order_detail = OrderDetail.objects.create(
                amount=data['amount'],
                price=data['price'],
                discount=data['discount'],
                order_id=order,
                product_id=product
            )
            serializer = OrderDetailSerializer(order_detail)
            return custom_response('Create order detail successfully!', 'Success', serializer.data, 201)
        except Exception as e:
            return custom_response('Failed to create order detail!', 'Error', str(e), 400)

class OrderDetailWithProductDetailAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, order_id_slug, id_slug):
        try:
            order_detail = OrderDetail.objects.get(order_id=order_id_slug, id=id_slug)
            serializer = OrderDetailSerializer(order_detail)
            return custom_response('Get order detail successfully!', 'Success', serializer.data, 200)
        except OrderDetail.DoesNotExist:
            return custom_response('Order detail not found!', 'Error', None, 404)
        except Exception as e:
            return custom_response('Failed to retrieve order detail!', 'Error', str(e), 500)

    def put(self, request, order_id_slug, id_slug):
        try:
            data = parse_request(request)
            order_detail = OrderDetail.objects.get(id=id_slug)
            serializer = OrderDetailSerializer(order_detail, data=data)
            if serializer.is_valid():
                serializer.save()
                return custom_response('Update order detail successfully!', 'Success', serializer.data, 200)
            else:
                return custom_response('Update order detail failed', 'Error', serializer.errors, 400)
        except OrderDetail.DoesNotExist:
            return custom_response('Order detail not found!', 'Error', None, 404)
        except Exception as e:
            return custom_response('Failed to update order detail!', 'Error', str(e), 500)

    def delete(self, request, order_id_slug, id_slug):
        try:
            order_detail = OrderDetail.objects.get(id=id_slug)
            order_detail.delete()
            return custom_response('Delete order detail successfully!', 'Success', {"order_detail_id": id_slug}, 204)
        except OrderDetail.DoesNotExist:
            return custom_response('Order detail not found!', 'Error', None, 404)
        except Exception as e:
            return custom_response('Failed to delete order detail!', 'Error', str(e), 500)
