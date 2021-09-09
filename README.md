# AutomateJobMenu

A bot that get jobs from Indeed ( link, tittle, company, location, and salary), it can be modified to a different job board. 

## Description

Developed in Selenium and BeautifulSoup, it uses a modified chromedriver,  undetected_chromedriver.v2 ,  to avoid bot detection

## Getting Started

### To Install

```
pip install undetected-chromedriver
```
```
pip install selenium
```
```
pip install beautifulsoup4
```
## Easy setup
* Change job title and desired location in main.py to run 

## Required for a diferent site
* Import the modified chrome driver
* Create a new bot using the IndeedBot class with such driver, job, location, and random time
* To turn the IndeedBot into a different site bot, change xpaths.

# Important 
### It can avoid most bot detections measures, but it can still fail if is being abused. It is fast enough, but it does not use multithreading. Low speeds are recommended.


## Authors

Developed by: harry-dev.one


## License

Be free to use it, just do not abuse it.
