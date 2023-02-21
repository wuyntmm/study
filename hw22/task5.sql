SELECT COUNT(*) AS amount FROM purchase
JOIN books ON books.id = purchase.book_id WHERE books.author = 'Rowling'