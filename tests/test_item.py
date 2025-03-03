"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_total_price():
    item = Item("Computer mouse", 500, 4)
    assert item.calculate_total_price() == 2000

def test_apply_discount(monkeypatch):
    item = Item("Keyboard", 1200, 2)
    monkeypatch.setattr(Item, "pay_rate", 0.9)  # Меняем только в этом тесте
    item.apply_discount()
    assert item.price == 1080


def test_item_all():
    Item.all = []  # Очищаем список перед тестом
    item1 = Item("phone", 1000, 3)
    item2 = Item("laptop", 2000, 2)

    assert len(Item.all) == 2

def test_default_pay_rate():
    item = Item("monitor", 3000, 1)
    assert item.pay_rate == 1.0