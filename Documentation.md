# Oct 26 Intial Setup & Exploration
## Setting up the AWS account
Since I had created an account before (which is automatically deleted after 6 months for free tiers), there will be no free credits for the new account I just created, although the free tier seems to support my intention of using IoT Greengrass V2, so long as I keep it to no more than three devices with some other restricitons.
## Exploring the IoT Greengrass 
It is said that IoT Greengrass can run on Mac OS by running AWS IoT Greengrass with no Greengrass Lambda containerization at the group level in a Docker container as documented on [this page](https://aws.amazon.com/greengrass/faqs/).

Following tutorial on [this page](https://docs.aws.amazon.com/iot/latest/developerguide/using-laptop-as-device.html), and following this tutorial here is the items that I did (skipped some that I have configured from using AWS CLI previously):
- Install the AWS IoT Device SDK for Python, [ref](https://docs.aws.amazon.com/iot/latest/developerguide/using-laptop-as-device.html)
  - Create AWS IoT resources, which includes creating an IoT policy and "a thing object", [ref](https://docs.aws.amazon.com/iot/latest/developerguide/create-iot-resources.html)
