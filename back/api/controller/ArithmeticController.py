from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.services.Operator import Operator


class ArithmeticController(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        _result = ''
        try:
            first = request.data['first']
            second = request.data['second']
            operation = request.data['operation']

            _result = Operator(operation).calc([first, second])

        except MultiValueDictKeyError:
            _result = 'Заполните все поля или введите правильный оператор'

        except Exception as e:
            _result = str(e)

        return Response(_result)

