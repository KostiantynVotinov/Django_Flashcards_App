from django.db import models

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class Card(models.Model):
    question = models.CharField(max_length=100)  # Поле для збереження питання на картці
    answer = models.CharField(max_length=100)  # Поле для збереження відповіді на картці
    box = models.IntegerField(  # Поле для визначення номера коробки, в якій знаходиться картка
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)  # Поле для збереження дати створення картки

    def __str__(self):
        return self.question

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]  # Визначення нової коробки залежно від вирішення питання

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self

