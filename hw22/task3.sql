SELECT users.id, users.first_name, users.last_name, books.title  FROM purchase
JOIN users ON users.id = purchase.user_id
JOIN books ON books.id = purchase.book_id
ORDER BY users.id