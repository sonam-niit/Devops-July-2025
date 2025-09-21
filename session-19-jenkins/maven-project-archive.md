# Set up jenkins plugin for Maven and archieve Setup

1. setting --> manage jenkins
2. plugins --> available plugins
3. search for Maven --> click on Maven Integration option --> install
4. to verify if plugin installed successfully or not
5. Jenkins dashboard -> new item -> Maven Project
6. create project -> description --> poll scm --> H/20 * * * *
7. Git --> add Repo link --> give branch name: main

[Java Sample Test](https://github.com/sonam-niit/SampleJavaMevan-Jenkins.git)

8. Maven Goals: clean install
9. Post-build Actions --> Archive the artifacts
10. Files to archieve: target/*.jar
11. build now.
12. once build successful check test dashboard also you can download jar file from the artifacts.