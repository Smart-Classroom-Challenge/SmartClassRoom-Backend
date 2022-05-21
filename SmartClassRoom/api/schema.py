import graphene
from graphene_django import DjangoObjectType
from .models import Classroom, MeasurementStation, Measurement, EntranceEvent, ConnectionHistory


class ClassroomType(DjangoObjectType):
    class Meta:
        model = Classroom
        fields = ('id', 'updated_on', 'room_number', 'name', 'description')


class MeasurementStationType(DjangoObjectType):
    class Meta:
        model = MeasurementStation
        fields = ('id', 'fk_classroom', 'active')


class MeasurementType(DjangoObjectType):
    class Meta:
        model = Measurement
        fields = ('id', 'insert_time', 'co2', 'temperature', 'humidity', 'motion', 'light')


class EntranceEventType(DjangoObjectType):
    class Meta:
        model = EntranceEvent
        fields = ('id', 'insert_time', 'fk_measurement_station')


class ConnectionHistoryType(DjangoObjectType):
    class Meta:
        model = ConnectionHistory
        fields = ('id', 'insert_time', 'fk_measurement_station', 'ip_address', 'bluetooth_connected',
                  'wlan_signal_strength', 'ping_backend', 'ping_broker', 'ping_grafana')


class Query(graphene.ObjectType):
    classrooms = graphene.List(ClassroomType)
    measurementStation = graphene.List(MeasurementStationType)
    entranceevenet = graphene.List(EntranceEventType)
    connectionhistory = graphene.List(ConnectionHistoryType)
    measurement = graphene.List(MeasurementType)

    def resolve_classrooms(root, info, **kwargs):
        # Querying a list
        return Classroom.objects.all()

    def resolve_measurementStation(root, info, **kwargs):
        return MeasurementStation.objects.all()

    def resolve_entranceevenet(root, info, **kwargs):
        return EntranceEvent.objects.all()

    def resolve_connectionhistory(root, info, **kwargs):
        return ConnectionHistory.objects.all()

    def resolve_measurement(root, info, **kwargs):
        return Measurement.objects.all()


schema = graphene.Schema(query=Query)
