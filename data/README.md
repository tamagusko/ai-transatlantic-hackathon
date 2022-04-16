# Data dict used to develop the MVP

- delivery_id (int): date (Ymd format) and id of the product to be delivered.
- status (str): status of the product: deposit, transit, delivery, delivered, locker.
- client (int): id to identify the client.
- delivery_type (str): type of delivery chosen: home or locker.
- adress (str): delivery address, can be the home or locker.
- phone (str): contact.
- email (str): contact email.
- history (str): changes during delivery: home -> locker, client absent, refused.

Example:

| delivery_id | status    | client | delivery_type | adress    | phone       | email             | history |
|-------------|-----------|--------|---------------|-----------|-------------|-------------------|---------|
| 202204151  | transit   | 1      | home          | address 1 | 912 345 678 | email@gmail.com   |         |
| 202204152  | delivered | 2      | locker        | address 2 | 913 345 678 | client2@sapo.pt   |         |
| 202204153  | deposit   | 3      | home          | address 3 | 922 345 678 | client3@gmail.com | refused |
