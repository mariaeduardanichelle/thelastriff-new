from core.models import Guitarra, Pedido


def test_guitarra_str():
    guitarra = Guitarra(
        marca='Fender',
        modelo='Stratocaster',
        preco=2000.00,
    )
    assert str(guitarra) == 'Fender - Stratocaster'