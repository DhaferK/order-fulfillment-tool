def economic_order_quantity(demand, holding_cost, order_cost):
    # Calculate EOQ
    eoq = ((2 * demand * order_cost) / holding_cost) ** 0.5
    return eoq

