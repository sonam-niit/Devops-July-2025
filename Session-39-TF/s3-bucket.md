# Introduction to S3 Bucket

- S3- S(simple) S(storage) S(services)
- where we can store any kind of data, we can access from anywhere

1. Create S3 Bucket

    - Aws Console -> S3 Service
    - create bucket -> give some unique name which is not taken by someone
    - go with the default options
    - just enable versioning
    - create bucket

2. Upload object to bucket

    - add files
    - select some image and check the details once it is uploaded
    - its converted into s3 object
    - check object details
    - if try to access object with provided url 
    - you can see access denied

3. Bucket policy

    - provide permission to access object
    - bucket - permisson - uncheck block all public access first
    - save changes 
    - bucket policy --> edit
    - [Policy Generator Link](https://awspolicygen.s3.amazonaws.com/policygen.html)
    - select S3 Bucket Policy
    - Principle: type *
    - Action: GetObject
    - Add Bucket ARN number followed by /*
    - add statement and create policy
    - copy code and paste insidebucket policy and save 
    - now again try to access objects

4. Static Website Hosting using S3 bucket

    - upload some index.html file inside s3 bucket
    - properties -> scroll down to last
    - static website hosting -> enable --> index.html as file
    - Save
    - you can see the URL generated try to access and the website is hosted on s3 bucket

5. Bucket Versioning

    - if you have enabled bucket versioning
    - then try to upload the same or modified file again
    - inside bucket there is an option show version
    - click on that and you can see same file with version details
    

