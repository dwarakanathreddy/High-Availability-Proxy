# HAP-practice
this folder is for the ha proxy practice

## Steps to follow
----------------------
1. start ec2 instance in aws and open up proper security groups
2. install docker on to the instance 
3. have the files in the directoy and build a docker image
4. use the following command to run the image with environment variable "sudo docker run -p 8080:80 -e appid=2 haproxy_demo"
5. install HA Proxy
6. create cfg file for the HA proxy configuration.
7. run the HAProxy using the command "sudo haproxy -f test_demo.cfg"
