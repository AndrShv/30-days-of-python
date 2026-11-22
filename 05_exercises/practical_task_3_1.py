raw_transactions = [
    "tx_01,user_101,150.50,success",
    "tx_02,user_102,99.00,failed",
    "tx_01,user_101,150.50,success",
    "tx_03,user_103,300.00,success",
    "tx_04,user_101,50.00,success",
    "tx_05,user_104,broken_data,success",
]


def process_payments(transactions_list):
    processed_tx_ids = set()
    user_balances = {}

    for tx in transactions_list:
        tx_id, user_id, amount, status = tx.split(",")
        if tx_id in processed_tx_ids:
            continue
        if "success" in status:
            try:
                floated_amount = float(amount)
                user_balances[user_id] = (
                    user_balances.get(user_id, 0.0) + floated_amount
                )
                processed_tx_ids.add(tx_id)
            except ValueError as e:
                print(f"Ошибка конвертации суммы для транзакции {tx_id}: {e}")
                continue
    return user_balances


balances = process_payments(raw_transactions)
print("Итоговые балансы пользователей:")
print(balances)
