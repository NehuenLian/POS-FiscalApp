from typing import Tuple

from src.data_access.repositories.check_stock_dao import CheckStockDAO
from src.data_access.session_manager import session_scope
from src.utils.logger import business_logger, console_logger


class CheckStock:
    def __init__(self):
        pass

    def search_product(self, barcode: str) -> Tuple[int, str, str, int]:
        with session_scope() as session:
            query = CheckStockDAO(session)
            product_id, product_barcode, product_name, available_quantity = query.select_name_quantity(barcode)
            console_logger.info(f"Product obtained: {product_name}")

            return product_id, product_barcode, product_name, available_quantity