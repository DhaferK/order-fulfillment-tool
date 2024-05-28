def economic_order_quantity(demand, holding_cost, order_cost):
    """
    Calculate the Economic Order Quantity (EOQ).

    :param demand: Annual demand for the product
    :param holding_cost: Holding cost per unit per year
    :param order_cost: Cost per order
    :return: EOQ value
    """
    eoq = ((2 * demand * order_cost) / holding_cost) ** 0.5
    return eoq
