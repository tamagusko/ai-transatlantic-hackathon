# MVP

This MVP has to prove that our idea can be applied in the future. Therefore, we have to prove the adopted concepts. If possible, with real tests on a reduced scale.

![Structure](projectStructure.png)

## To develop:


- sendSMS.py: Sends an sms using Twilio API.
- monitor.py: If the client's response is no(n) to an SMS or call, it directs the order to a locker closer to the customer.
- sendMail.py: send an email notifying of day delivery (sends when it leaves the warehouse).
- makeCall.py: 15 minutes before delivery, call the customer and ask if he can receive the order, answer y or n. In the future, identify the client's response with NLP.
- coordinates.py: with an address returns the coordinates (lat and long).
- closestLocker.py: with the coordinates, it returns the closest available locker (you have to evaluate the size of the order).
- processingData.py: Process customer data to transform addresses into coordinates.
- shortestRoute: Calculates the shortest route between customers based on travel times. Still, it returns the actual distance between these customers.
- genAlgorithmBestRoute.py: Optimization algorithm with genetic algorithm to calculate the best delivery route. This algorithm updates whenever it has a response from the client.
- createInstance: Creates an instance with the distances between all deliveries based on the addresses of deliveries to customers. This instance is an n x n matrix where n = number of locations for delivery.
- boxMeasurement.py: Using the Luxonis camera, take the measurements of the box. Using the Luxonis camera, take the measurements of the box. This will be done at the warehouse.
- Plot Graph Results: Develop createGraph.py and plotRoute.py to show the routes created based on the optimization algorithm.
- Front-end: Dashboard for visualization of results and control by logistic operators.
- Develop a front-end with a table of deliveries and status. Clicking on the delivery opens its details.
- Develop a map to view locations, deliveries, and lockers.


## Activities:

1. ~~Create a data structure for the MVP.~~ @tamagusko
2. ~~Draw solution diagram.~~ @tamagusko
3. ~~Fix concept diagram.~~ @ArmandoDauer
4. ~~Frontend draft - Dashboard.~~ @Neha
5. boxMeasurement.py. @Jovial
6. ~~First pitch (20220419 - 17H).~~ @ArmandoDauer
7. ~~Optimization algorithm (genAlgorithmBestRoute.py).~~ @ArmandoDauer
8. ~~Code sendSMS.py.~~ @tamagusko
9. monitor.py @tamagusko (not implemented)
10. ~~createGraph.py~~ @tamagusko
11. ~~shortestRoute~~ @tamagusko
12. ~~processingData~~ @tamagusko
13. ~~createInstance~~ @tamagusko
14. ~~Code sendMail.py~~ @tamagusko
15. ~~Code makeCall.py.~~ @tamagusko
16. ~~code coordinates.py.~~ @tamagusko
17. code closestLocker.py. @tamagusko
18. ~~Plot graph results (createGraph.py + plotRoute.py).~~ @tamagusko
19. Integrate all modules on the front-end @tamagusko @Neha (not implemented)
20. ~~First pitch~~
21. Finalize the MVP to present (until 24/02 8h).
22. Final Pitch (until 24/02 14h) @Matheus and Armando

