# Deployment Stratergies

1. Blue-Green Deployment

- blue (current deployment): this version currently serving your traffic
- Green (New Release): new version of app to deploy

- at a time only one environment can serve traffic.

2. canary Deployment

- Prepares two versions
- Current Version (stable) - v1
- New Version (canary) - v2
- Both versions are deployed to production but only a portion of traffic goes to v2

- Traffic routing
    1. 95% users - v1
    2. 5% users - v2
- we can check load balancers, services etc..
- monitor them

- if all good then gradually increase traffic
- 5% -- 20% -- 50% -- 100%

- incase of any issues you can rollout to v1 immediately
