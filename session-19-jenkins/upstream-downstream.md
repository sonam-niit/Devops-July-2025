# Start one job from another

1. create freestyle project
2. name - DownStreamJob , description etc..
3. set one build step and write simple shell command
```bash
echo "Job 2 started after Job1"
echo "Job 2 completed successfully"
```
4. save the configuration

# Create another Job which will start above Job

1. create freestyle project
2. name - UpStreamJob , description etc..
3. set one build step and write simple shell command
```bash
echo "This is my first Job to execute"
echo " job 1 completed successfully"
```
4. Post Build Actions --> Projects to build --> give the name of above created project (DownStreamJob)
5. select Trigger only if build is stable
6. save the configuration
7. build now and you can see DownStreamJob started by UpStreamJob