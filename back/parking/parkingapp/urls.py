from enum import Enum

from django.urls import path

from .views.floor_view import FloorViewSet
from .views.parking_view import ParkingViewSet
from .views.reservation_view import ReservationViewSet
from .views.spot_view import SpotViewSet
from .views.login_view import LoginView


class DrfMethods(Enum):

    LIST = {"get": "list"}
    RETRIEVE = {"get": "retrieve"}
    CREATE = {"post": "create"}
    UPDATE = {"put": "update"}
    DESTROY = {"delete": "destroy"}

    CRUD = {
        "post": "create",
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }

    GET_PUT_AND_DELETE = {
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    }
    LIST_AND_CREATE = {"get": "list", "post": "create"}

    POST = {"post": "create"}

urlpatterns = [
    # Auth
    path('login', LoginView.as_view(), name='login'),

    # Management
    path(
        'parkings',
        ParkingViewSet.as_view(DrfMethods.LIST.value),
        name='parkings'
    ),
    path(
        'parkings/<uuid:pk>',
        ParkingViewSet.as_view(DrfMethods.RETRIEVE.value),
        name='parking'
    ),
    path(
        'floors',
        FloorViewSet.as_view(DrfMethods.LIST.value),
        name='floors'
    ),
    path(
        'spots',
        SpotViewSet.as_view(DrfMethods.LIST.value),
        name='spots'
    ),
    path(
        'reservations',
        ReservationViewSet.as_view(DrfMethods.LIST_AND_CREATE.value),
        name='reservations'
    ),
    path(
        'reservations/<uuid:pk>',
        ReservationViewSet.as_view(DrfMethods.GET_PUT_AND_DELETE.value),
        name='reservations'
    )
]