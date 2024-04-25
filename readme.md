# RabbitMQ Python Tutorial

This project is a simple implementation of RabbitMQ in Python. It includes a sender ([send.py](send.py)) that sends a message and a receiver ([receive.py](receive.py)) that receives and prints the message.

This tutorial is courtesy of:
https://www.rabbitmq.com/tutorials/tutorial-one-python

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3
- RabbitMQ
- Pika Python package

### Installing

1. Clone the repository
```
git clone https://github.com/kimintime/RabbitMq---Hello-World.git
```

2. Navigate to the project directory
```
cd your-repo-name
```

3. Create a virtual environment and activate it
```
python3 -m venv env
source env/bin/activate
```

4. Install the dependencies
```
pip3 install -r requirements.txt
```

## Running the Application
1. Start the RabbitMQ server

2. Run the receiver script
```
python3 receive.py
```

3. Run the sender script
```
python3 send.py
```

## Quit the application
- `ctrl-c` to exit the 'receive.py'
- Remember to shut down the rabbitmq server