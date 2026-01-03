# Backups

- Disaster Recovery Backups are very Important

- EBS Snapshots
- Elastic Block Store - Its a Storage Providedby AWS to attach extra space to instance
- This is not getting deleted in case if you delete you Instance As well.
- By Default what volume is coming that will be deleted with instance. but for that you can take Backup using Snapshots

- Go to EC2-EBS- Snapshot - Create Snapshot - select volume which backup you want to take and create Snapshot (Manual Process of Backup)

- For Restore create new Volume and select Snapshot so you can restore it.

- If you want to attach Restored Volume to your instance.
- Select volume & attach to your instance.

**Create Volume**

- You can also create your extra Volume By Click on Create Volume
- Make sure you volume zone and instance zome must be same
- then only you can attach volume to that instance.
- Also you can detach volume from instance.

## EBS SnapShot Automation

- Best and Recommended way for Backup
- AWS DLM (Data Lifecycle Manager)

**What it is doing?**

- Automatically creates backup
- Retains
- deletes old EBS snapshots

**Steps to Create That**

1. AWS Console- EC2 - EBS - LifeCycle Manager
2. Create LifeCycle Policy (Default Policy)
3. EBS Snapshot select, target Volume
4. Tags: Key: Backup & Value: true
5. Schedule: select Daily
6. Retention: Keep last 7 days or 30 days
7. Create (Fully Automated Backup system)

### Activities

- create Instance
- Create Volume
- attach volume to that instance
- detach Volume
- Create Snapshot for the volume created
- delete that volume and again try to restore by create ne volume from snapshot

- Create Automated Backup Policy

- Last, delete all resources

## S3 Bucket Backup

1. Enable Versioning

- S3 - Bucket - Properties - Versioning - Enable
- Now Delete not gone
- but Old Versions Remains same
- Which is considered as a Basic Backup of S3 Bucket

2. Another Way of Backup is SRR (Same Region Replication)

- CRR (Cross Region Replication) - DR possible (Disaster Recovery)

- Create SRR

    1. create bucket: sonamapp-prod-bucket: enable versioning
    2. create backup backet: sonamapp-backup-bucket - enable versioning
    3. prod-bucket --> management --> Replication Rule
    4. Create Replication Rule -> Status Enabled
    5. Source Bucket: Apply to all objects in Bucket
    6. Destination: Choose Bucket in this account and select the backup bucket which is created.
    7. IAM role: create New Role (it will create new role as per req)
    8. Extra Info: Select Destination Storage class (by default its standard you can change it to glacier for Cheaper rate)
    9. Addition Option: Select Delete Marker, Replica Modification Sync
    10. Save.
    11. Once you save It will ask you to replicate existing Objects
    12. Say yes if you want to take the backup of old objects as well.
    13. Say yes then you need to continue with batch operation for olad object else you can skip

- Once Its configured
- Upload one object in prod bucket and then check in Backup bucket
- Also, delete from Production and check again in Backup
- Also, check versions so you can see delete Marker