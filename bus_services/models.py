from django.db import models

class BusService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Route(models.Model):
    route_number = models.CharField(max_length=50)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    bus_service = models.ForeignKey(BusService, on_delete=models.CASCADE)

class Stop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
