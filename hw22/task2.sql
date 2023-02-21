SELECT purchase.id, purchase.date, users.first_name, users.last_name FROM purchase
JOIN users ON users.id = purchase.user_id