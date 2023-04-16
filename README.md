# Mage_Battlegrounds_Documentation
![image](https://user-images.githubusercontent.com/45697319/232301439-2f26e640-7c30-4bfe-a41e-a07f130833e7.png)

<h1><center>Case Study</center></h1>

## Objective:

The goal with this example is to simulate an e-commerce platform for computers and video games.

### Features to be considered:

* 3 computer brands of your choice
* 3 video game console brands
* Prices per computer, per console for each brand with their respective commission
* Consider the 5 most important cities in your country of residence
* Consider all payment methods you wish to use
* Consider source of conversion (Advertising, Influencers, Organic)
* Consider all order statuses you want
* Choose the number of stores per city you want, with their respective coordinates

<img width="382" alt="image" src="https://user-images.githubusercontent.com/45697319/232307457-a19e9a78-0685-4b01-b502-fab71aa1a706.png">


**Lets Do it !! 🚀**

# 📃 Overview :

1. [Infrastructure](https://github.com/alexbonella/Mage_Battlegrounds_Documentation#infrastructure)
2. [Demo](https://github.com/alexbonella/Mage_Battlegrounds_Documentation/blob/main/README.md#-demo)
3. [Python Script simulation](https://github.com/alexbonella/Mage_Battlegrounds_Documentation#python-script-simulation)
4. [Send Kafka Topics](https://github.com/alexbonella/Mage_Battlegrounds_Documentation#send-kafka-topics)
5. [Mage Zone](https://github.com/alexbonella/Mage_Battlegrounds_Documentation#mage-zone)
6. [Apache Druid Deploy](https://github.com/alexbonella/Mage_Battlegrounds_Documentation#apache-druid-deploy)
7. [Grafana](https://github.com/alexbonella/Mage_Battlegrounds_Documentation#grafana)

# Infrastructure
![Infra_Kinseis_AWS - copia drawio](https://user-images.githubusercontent.com/45697319/232306813-e6e151bf-01eb-4e2e-b1cf-c4853cef9632.png)
# 🎮 Demo
![DemoGif](https://github.com/alexbonella/Mage_Battlegrounds_Documentation/blob/main/Media_files/kafka-mage_z28BiI5y.gif
)

# Python Script simulation

I wanted to simulate with Python the streaming data of my e-commerce platform for computers and video games keeping in mind that I have 1000 unique user, we can go to access to code here :

* [Go to the Notebook](https://github.com/alexbonella/Mage_Battlegrounds_Documentation/blob/main/Ecommerce_Simulation/Ecommerce_Simulation_Hackacton_Mage.ipynb)
* [Go to utils.py](https://github.com/alexbonella/Mage_Battlegrounds_Documentation/blob/main/Ecommerce_Simulation/utils.py)
## Sample purchase records

<img width="259" alt="image" src="https://user-images.githubusercontent.com/45697319/232308179-8fb8f1aa-dde3-4407-be12-b2fa5204720b.png">

# Send Kafka Topics

I've created 2 Kaftka topics in order to analysis purchase behavior of our customer  :

* **topic_purchase_records:** This topic receive the raw purchase records 
* **topic_druid_grafana_new:** This topic receive the **```topic_purchase_records```** records in order to enrich records to send into the new kafka topic

<img width="516" alt="image" src="https://user-images.githubusercontent.com/45697319/232314270-e16aff64-1c88-469a-9fb8-9642bcad05c2.png">

# Mage Zone

I've created 2 Streaming pipelines in order to enrich my Kafka topics and to store new records into S3 Buckets  :

* **Kafka_transform:** This pipeline is in charge to edit the created_at field in order t create  2 new columns Date(YYYY-MM--DD) and Hour
* **Store_s3_bucket:** This pipeline is in charge to send parquet files into the S3 Bucket .

```
connector_type: amazon_s3
bucket: mage-hackaton
prefix: purchase
file_type: parquet
buffer_size_mb: 5
buffer_timeout_seconds: 100
```

![transform](https://github.com/alexbonella/Mage_Battlegrounds_Documentation/blob/main/Media_files/kafka_transofmr.png)
![store_s3](https://github.com/alexbonella/Mage_Battlegrounds_Documentation/blob/main/Media_files/store_s3.png)



# Apache Druid Deploy

I've deployed Apache Druid into an EC2 instance in order to connect with the Kafka topic stream and finally be able to analysis as easy as quickly my purchase records .

Here I want to share with you an [article](https://datexland.medium.com/how-to-deploy-apache-druid-on-aws-ec2-instance-50af955edef) that I wrote recently about How can I deploy Apache Druid into EC2 instances

* EC2 Instances :  **```t2.xlarge```** - [Go Pricing](https://github.com/alexbonella/Mage_Battlegrounds_Documentation/blob/main/Media_files/EC2_Pricing.png)

![Druid action](https://miro.medium.com/v2/resize:fit:786/1*ZGpZLHqwTKHhX5zmPpEIEQ.gif)

# Grafana
<img width="625" alt="image" src="https://user-images.githubusercontent.com/45697319/232315116-1ecd99bd-7634-4b83-a9f6-052cef2f009e.png">

# License

[![License Mit](https://img.shields.io/badge/License-Mit-green)](https://github.com/alexbonella/Mage_Battlegrounds_Documentation/blob/main/LICENSE)

# Sponsor me

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/donate/?hosted_button_id=GBVXVLXMETRHE)


# Contributions : 

* [![Medium](https://img.shields.io/badge/Medium-Blog-black)](https://datexland.medium.com/)
* [![Udemy](https://img.shields.io/badge/Udemy-Course-purple)](https://bit.ly/41cZfHD)
* [![AWS-Community Builder](https://img.shields.io/badge/AWS-Community%20Builder-orange)](https://aws.amazon.com/es/developer/community/community-builders/community-builders-directory/?cb-cards.sort-by=item.additionalFields.cbName&cb-cards.sort-order=asc&awsf.builder-category=cb-type%23data&awsf.location=location%23latam&awsf.year=year%232022)
* [![Youtube-Talks](https://img.shields.io/badge/Youtube-Talks-red)](https://www.youtube.com/watch?v=8pECZZ6l8-4&t=3669s)

# Connect with me: 

 [![LinkedIn](https://img.shields.io/badge/-LinkedIn-3b5998)](https://www.linkedin.com/in/alexanderbolano)
 [![Kaggle](https://img.shields.io/badge/-Kaggle-blue)](https://www.kaggle.com/alexbonella)
 [![Stackoverflow](https://img.shields.io/badge/-Stackoverflow-ff7c55)](https://stackoverflow.com/users/10906576/alexbonella)
 [![Twitter](https://img.shields.io/badge/-@datexland-1DA1F2)](https://twitter.com/datexland)
