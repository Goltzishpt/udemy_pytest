![Static Badge](https://img.shields.io/badge/python%203.11.4)


# Project
This project is a collection of sample tests using the Playwright
library with the Pytest framework, which are written in Python and run
on Chrome, Safari (Webkit), and Firefox browsers. The tests cover multiple 
configurations for iPhone 12 Pro and Pixel 5, and cover various functional 
scenarios.


## Preview
The tests in this project use the TestMe-TCM app(https://github.com/Ypurek/TestMe-TCM).
Please install this app separately before running the tests.

- Clone the repository: 
``` bash Copy code
git clone https://github.com/Ypurek/TestMe-TCM
```

- Navigate to the project directory:
``` bash Copy code
cd TestMe-TCM
```
- Install the required dependencies: 
``` bash Copy code
pip install -r requirements.txt
```

- Run the project

``` bash Copy code
python manage.py runserver
```

* Please use the following login credentials for the TestMe-TCM app:
- alice
- bob
- charlie
- password: Qamania123


## Installation Guide

To install the project, follow these steps:

- Clone the repository: 
``` Copy code
git clone https://github.com/Goltzishpt/udemy_pytest
```
- Navigate to the project directory: 
``` bash Copy code
cd udemy_pytest
```
- Install the required dependencies: 
``` bash Copy code
pip install -r requirements.txt
```

- Download and install Chrome, Safari, and Firefox browsers.


## Running the Tests

To run the tests, use the following command in the terminal:

``` bash Copy code
pytest tests
```


## Configuration
You can change the following parameters in the project's settings:

### settings.py:
* **BROWSER_OPTIONS:** A dictionary containing the following options:
    + **geolocation:** Dict with latitude and longitude
* **USER:** A dictionary containing the following options:
    + **login**: alice or bob or charlie
    + **password:** Qamania123
### pytest.ini
* **addopts:**
    + **--base_url:** The default value is http://127.0.0.1:8000 
    + **--device:** Choose the required device from  https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json
      + By default, the tests run on an iPhone 12 Pro and a Pixel 5. 
      However, you can customize this parameter in the **fixtures** to run 
      tests on any device separately. To do so, modify the **conftest.py** file.
    + **--browser:** firefox, chromium or webkit
      + By default, the tests run on Firefox, Chromium and Webkit together. 
        However, you can customize this parameter in the **fixtures** to run 
        tests on any device separately. To do so, modify the **conftest.py** file.

