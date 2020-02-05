# Fake News Detector
Simple Machine Learning project for learning purposes only.
First of all the script access the URL the user sends by an argument and using web scraping, it is able to get the full text of the news and give it to the model say if it is a real or fake news!
The model is built using Python and Passive Aggressive Classification.

## Downloading it
To access the repository files, all you need to do is clone it using git:

```
git clone https://github.com/gabrielassisdepaula/fake-news-detector.git
```

or download it through the Github GUI

## How to use it
First of all you need to have Python installed in your computer, if you dont't have you can download it [here](https://www.python.org/downloads/).

Now, with Python installed, a few packages are required to run the script.
You can install them through the command:

```
pip install argparse beautifulsoup4 urllib3 numpy pandas scikit-learn
```

or through this command in your preferred conda virtual environment:

```
> conda install argparse beautifulsoup4 urllib3 numpy pandas scikit-learn
```

Now that you have the requirements, open the main.py file and in line 25, insert the path to where the "news.csv" file is in your computer.

After that is done, you are good to go, open you terminal and type

> python main.py -u [insert here the link of the news you want to check]

Wait a little bit and you will receive telling you if the news is real or fake!

## Technologies Used
* [Python 3.7.6](https://www.python.org/)

## Packages
* [Argparse](https://docs.python.org/3/library/argparse.html)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Scikit-Learn](https://scikit-learn.org/stable/)
* [Urllib](https://docs.python.org/3/library/urllib.html)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Notes
The script still under development to be more embracing, for now it will only work with BBC news.

## Authors
* **Gabriel Assis** - Estudante de Informática - [gabrielassisdepaula](https://github.com/gabrielassisdepaula)

## License
This project is licensed under the MIT License - read the [LICENSE](LICENSE) for more details.
