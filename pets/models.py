from django.db import models


class PetGenre(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20, choices=PetGenre.choices, default=PetGenre.DEFAULT
    )
    group = models.ForeignKey(
        "groups.Group", on_delete=models.PROTECT, related_name="pets"
    )

    def __repr__(self) -> str:
        return (
            f" pet - [{self.id}] {self.name}, {self.age} age , {self.weight} weight. "
        )
