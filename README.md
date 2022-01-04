# DjangoService

I have used MYSQL in this Project.
Create a table by this query or run django migrate command
"CREATE TABLE `eventservice_event` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `created` datetime(6) NOT NULL, `modified` datetime(6) NULL, `event_type` smallint NOT NULL, `triggered_browser` varchar(50) NOT NULL);"

Process to run the project:

1->Create a virtual env
2->Activate that virtual env
3->git clone https://github.com/cAtAlYsT-14/DjangoService.git
4->cd DjangoService/
5->git checkout django_service
6->pip install -r requirements/requirements.txt 
7-> Add the db credentials in the .env file
8->./manage.py migrate
9->./manage.py runserver

10-> You are now good to go!

