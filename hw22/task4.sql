SELECT purchase.user_id, COUNT(*) AS purchase_count FROM purchase GROUP BY purchase.user_id