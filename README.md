# Signature-Based-Query-Filtering-Using-Relational-Algebra
0. Copy the project zip file to linux machine and extract

1. Install docker cli

2. Add mysql-server image to docker (found in the same folder)
# docker load -i mysql-server.tar

3. Add qconv image to docker (found in the same folder)
# docker load -i qconv_cont.tar

4. Run the containers
# docker run -it -d --name Qconv majpro/qconv:handmade
# docker run --name mysql2 -d -p 3306:3306 mysql/mysql-server:custom

5. Enter root shell
$ sudo -i

6. Enter the path where the project zip was extracted
# cd /path/to/extract/Backend/query_checker

7. Add execution privelege to init.bash and run
# chmod 777 init.bash
# ./init.bash
(it starts the containers automatically and creates virtual environment)

8. Change source to venv
# source yourenv/bin/activate

9. Install python sql connector
# pip install mysql-connector-python

10. Now execute the service.py script
# python service.py
this will create a socket which will listen for queries

11. Open a new teminal from preset and run sqli-demo
# python app.py
this will run a flask server at localhost click the link to follow the demo page

12. Try to login in using valid credentials
username: admin
password: root@123
this will succeed to the dashboard and displays the api key for the user

13. You can also try malicious input like
username: admin"--
password: ***
this will trigger an alert stating that "Potential Sql injection detected. Login blocked"
