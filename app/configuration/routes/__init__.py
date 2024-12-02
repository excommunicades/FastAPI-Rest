from app.configuration.routes.routes import Routes
from app.internal.routes.products import products

__routes__ = Routes(routers=(products.router, ))
