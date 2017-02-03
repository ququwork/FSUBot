# FSUBot

A bot which serves as the foundation for other bots for use on the Florida State University website. It is useful for automating tasks that are otherwise very menial and tedious. 

This project serves as a framework for creating bots which are designed for Florida State University websites. It handles logging into MyFSU automatically, and setting up ubiquitous attributes and functionality such as:

1. Standard argument parsing
1. Logging into MyFSU
1. Web browser driver handling.

## Where to Begin

### Package Installation

Install the `FSUBot` package using `pip`.

```bash
$ pip install fsubot
```

If you receive a error 13 and/or a permission error, prefer:
```bash
$ pip install fsubot --user
``` 
rather than:
```bash
sudo pip install fsubot
```

### Driver Installation

Download and install any driver from the following (I prefer `chromedriver`):

* Chrome: [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* Firefox: [geckodriver](https://github.com/mozilla/geckodriver/releases)
    * There has not been extensive testing using `geckodriver`, proceed with caution.

Ensure that the driver executable is located within your environment's `PATH` variable. There are many readily available guides on Google for how to do this.

### Bot Instantiation

If you instantiate your bot with the following: 

```python
fsu_dr = FSUBot(use_cli=True)
```

Then, you can pass in arguments like so:

```bash
$ python fsubot/bot.py --fsu-id abc13 --fsu-pw hunter2 --browser chrome --executable-path drivers/chromedriver
```

### Examples

* [Vindicta](https://github.com/seanpianka/Vindicta), my personal bot which automatically enrolls for desired courses.
* [EasyGradeBot](https://github.com/seanpianka/EasyGradeBot), my personal bot which traverses through a list of BlackBoard Smart View pages and downloads all submitted assignment's most recently submitted attempts.


### Page Navigation Information

After instantiating your bot, named `bot`, there are a few methods you can use for traversing the DOM and navigating to different pages.

#### Method 1

Use `bot.dr`, the accessible `selenium.webdriver` instance, and the [well-documented Selenium API](https://seleniumhq.github.io/selenium/docs/api/py/api.html).

#### Method 2

Use `bot.click_list` for large JSON lists. Here is the following format for those lists:

```JSON
{
    "pages": [
        {
            "title": "",
            "iframe": false,
            "xpath": "",
            "css_selector": ""
        },

        {
            "title": "",
            "iframe": false,
            "xpath": "",
            "css_selector": ""
        },

        {
            "title": "",
            "iframe": false,
            "xpath": "",
            "css_selector": ""
        },

        {
            "title": "",
            "iframe": false,
            "xpath": "",
            "css_selector": ""
        },

        {
            "title": "",
            "iframe": false,
            "xpath": "",
            "css_selector": ""
        },

        {
            "title": "",
            "iframe": false,
            "xpath": "",
            "css_selector": ""
        }
    ]
}
```

The elements will be sequentially passed to `bot._click` and clicked as if a real user was clicking them.

* `title` is used for logging purposes, to indicate when clicking an element has succeeded.
* `iframe` is used to specify if the following `css_selector` or `xpath` will resolve to an iframe, which should thusly be focused on (review Selenium's API for focusing on an iframe).
* `xpath` is used to specify the xpath for resolving an element to be clicked.
* `css_selector` is used to specify the CSS selector for resolving an element to be clicked.
