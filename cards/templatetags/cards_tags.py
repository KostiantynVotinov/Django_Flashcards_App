from django import template

from cards.models import BOXES, Card

register = template.Library()


@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    # Створюємо порожній список `boxes`
    boxes = []
    # Проходимо по кожному номеру коробки у `BOXES`
    for box_num in BOXES:
        # Рахуємо кількість карток для поточної коробки
        card_count = Card.objects.filter(box=box_num).count()
        # Створюємо словник з номером коробки та кількістю карток
        boxes.append({"number": box_num, "card_count": card_count})

    # Повертаємо словник `boxes` разом з шаблоном `"cards/box_links.html"`
    return {"boxes": boxes}
