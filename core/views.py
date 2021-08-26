from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import Category, SubCategory, Product
from core.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer

# Create your views here.

@api_view(['GET'])
def home(request):
    return HttpResponse("The Server is Up and Running!")


@api_view(['GET'])
def getAllCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getAllSubCategories(request):
    try:
        category = request.data.get('category')

        if not category:
            res = {
                "Wrong Input": "category is required."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            category_obj = Category.objects.get(name=category)
        except:
            res = {
                    "Category does not exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        sub_category = SubCategory.objects.filter(category=category_obj)

        serializer = SubCategorySerializer(sub_category, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getAllProductsForCategory(request):
    try:
        category = request.data.get('category')

        if not category:
            res = {
                "Wrong Input": "category is required."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            category_obj = Category.objects.get(name=category)
        except:
            res = {
                    "Category does not exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        sub_category_objs = SubCategory.objects.filter(category=category_obj)

        product_objs = Product.objects.filter(sub_category__in=sub_category_objs)

        serializer = ProductSerializer(product_objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getAllProductsForSubCategory(request):
    try:
        sub_category = request.data.get('sub_category')

        if not sub_category:
            res = {
                "Wrong Input": "sub_category is required."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            sub_category_obj = SubCategory.objects.get(name=sub_category)
        except:
            res = {
                    "Category does not exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        product = Product.objects.filter(sub_category=sub_category_obj)

        serializer = ProductSerializer(product, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def postProduct(request):
    try:
        category = request.data.get('category')
        sub_category = request.data.get('sub_category')
        name = request.data.get('name')

        if not sub_category or not category:
            res = {
                "Wrong Input": "sub_category and category are required."
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            category_obj = Category.objects.get(name=category)
        except:
            res = {
                    "Category does not exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            sub_category_obj = SubCategory.objects.get(name=sub_category)
        except:
            res = {
                    "Sub-Category does not exist": "Please check your inputs."
                }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if category_obj != sub_category_obj.category:
            res = {
                "Input Mismatch": "Input Category and Input Sub-Category's category are not matching"
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        try:
            if Product.objects.get(sub_category=sub_category_obj, name=name):
                res = {
                        "Input Error": "Product for the provided category and sub-category already exists."
                    }
                return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            pass

        product = Product.objects.create(
            sub_category=sub_category_obj,
            name=name
        )

        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        res = {
            "Exception" : str(e)
        }
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
