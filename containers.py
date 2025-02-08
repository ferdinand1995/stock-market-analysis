from dependency_injector import containers, providers
from services.stock_service import StockService

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    
    stock_service = providers.Singleton(
        StockService,
    )