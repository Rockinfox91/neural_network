# Neural Network

A home-made neural network project in python.

The goal here is to implement an ANNs (Artificial Neural Networks). To do so, we will firstly
try to make a single neuron, then learn how to connect them together and finally, train our
network on a data set to see how good it is and what to improve.

## Installation

To install, open in console (or Powershell on Windows) and copy : 

````shell
git clone https://github.com/Rockinfox91/neural_network.git
cd neural_network/
````

Then, for good measure, it's always good to make a VirtualEnvironment (check [documentation](https://docs.python.org/3/library/venv.html#how-venvs-work)), if you don't have 
the venv library install on your python, do :
````shell
python -m pip install virtualenv
````

Then, once it's downloaded :

````shell
python -m venv ./.venv/
./venv/Scripts/activate
````

You are now in the Virtual Environment, but there is no library installed. To get them, install with the command :
````shell
python -m pip install --upgrade pip
pip install -r "requirements.txt"
````

Be careful if you use PyCharm or any other IDE, to use the interpreter found in the .venv/Scripts/python.exe !

Now, you can launch the main file :

````shell
python ./src/main.py
````

## Explanation

