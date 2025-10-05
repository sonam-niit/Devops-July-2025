## Performance Testing

**Soak Testing**

- Endurance Testing
- Here you test your application which is exposed to normal or moderate load for given period of time
- You can detect Issues:
    1. Memory Leaks
    2. Database Connection Leakage
    3. Performance Degradation over a time
    4. Slow Response time to time
- 100 users sends req conti. for 8 hours

**Stress Testing**

- send more & more request to your application beyond its capacity to check how it fails or recovers.
- detect problems like:
    1. Breaking point of app
    2. how it recovers or fails when its high traffic
    3. how error handling done when there is a huge pressure

- Ramp up for 5000 users in 30 seconds to see the server fails or not.

------- Stress Testing with Locust will do in next session ----------