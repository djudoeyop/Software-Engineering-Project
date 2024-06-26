from . import orders, order_details, recipes, sandwiches, resources, users, reviews, promos

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)

    users.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    promos.Base.metadata.create_all(engine)