EVENT_CHOICES = (
    (1, 'Checkout'),
    (2, 'Subscribe-init'),
    (3, 'Subscribe-success'),
    (4, 'Unsubscribe')
)

RESPONSE_TYPE = {
    1 : 'Checkout Done!',
    2 : 'Subscribed',
    3 : 'Subscribed',
    4 : 'Unsubscribed'
}