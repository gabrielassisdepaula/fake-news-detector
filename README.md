# Fake News Detector
Simple Machine Learning project for learning purposes only.
The model is built using Passive Aggressive Classification through a dataset that is used to train it.
The model is pretty accurate having scores between 92 and 94%.

## How to use it
To begin with, a few packages are required to run the script.
You can install then through the command:

> pip install beautifulsoup4 urllib3 numpy pandas scikit-learn

or through this command in your preferred conda virtual environment:

> conda install beautifulsoup4 urllib3 numpy pandas scikit-learn

Now that you have the requirements, open the main.py file and in line 25, insert the path to where the "news.csv" file is in your computer.

After that is done, you are good to go, open you terminal and type

> python main.py -u [insert here the link of the news you want to check]

Wait a little bit and you will receive telling you if the news is real or fake!

### Notes
The script still under development to be more embracing, for now it will only work with BBC news.
