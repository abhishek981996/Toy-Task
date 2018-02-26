# Toy Task

Its a graph ploted case study and their relation with each other, which is shown in a bubble and line format using
Highchart

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequities for Unix

This project backend is build with django.So we need to install it first.
In order to remove conflict of our project with your running system we will use virtual environment in this project.

You need to have python and Mysql already installed and running in your Unix system.If not install them using the official 
websites


#### Install pip first

```
sudo apt-get install python-pip
```

#### Then install virtualenv using pip

```
pip install virtualenv 

```

#### If throws error for root permission :

```
sudo pip install virtualenv
```

#### Now create a virtual environment

```
virtualenv source
```

#### Active your virtual environment:

```
source source/bin/activate
```

### Clone this git repo

```
git clone https://github.com/abhishek981996/Toy-Task.git
```

go inside the repo using cd.

```
cd Toy-Task
```

#### Install all other dependencies

```
pip install -r requirement.txt
```





'''
python manage.py seed toy --number=15
'''