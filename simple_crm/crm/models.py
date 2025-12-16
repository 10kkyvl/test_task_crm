from django.db import models
from django.db.models.fields import related


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class Client(TimeStampedModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)
    email = models.EmailField(unique=True, max_length=100)

    def __str__(self) -> str:
        return self.name


class Deal(TimeStampedModel):
    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In progress"
        WON = "won", "Won"
        LOST = "lost", "Lost"

    client = models.ForeignKey(Client, related_name="deals", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    def __str__(self) -> str:
        return f"{self.title} ({self.client})"


class Note(TimeStampedModel):
    deal = models.ForeignKey(Deal, related_name="notes", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return f"Note #{self.pk} for {self.deal}"
