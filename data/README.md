# Data dict used to develop the MVP

* product_id (int): date (Ymd format) and id of the product to be delivered.
* status (str): status of the product: deposit, transit, delivery, delivered, locker.
* delivery_type (str): type of delivery chosen: home or locker.
* adress (str): delivery address, can be the home or locker.
* client (int): id to identify the client.
* phone (int): contact.
* history (str): changes during delivery: home -> locker, client absent, refused.


Example:

| product_id | status    | delivery_type | adress             | client   | phone       | history |
|------------|-----------|---------------|--------------------|----------|-------------|---------|
| 20220415_1 | transit   | home          | customer address 1 | client_1 | 912 345 678 |         |
| 20220415_2 | delivered | locker        | customer address 2 | client_2 | 913 345 678 |         |
| 20220415_3 | deposit   | home          | customer address 2 | client_3 | 922 345 678 | refused |
