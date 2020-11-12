[![Contributors][contributors-shield]][1]
[![Forks][forks-shield]][0]
[![Stargazers][stars-shield]][0]
[![Issues][issues-shield]][0]
[![MIT License][license-shield]][None]
[![LinkedIn][linkedin-shield]]["https://linkedin.com/in/louis-millette"]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Recipe Script</h3>
  <p align="center">
    A script for finding recipes online, given a list of ingredients.  Runs conveniently inside a terminal.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Here's what you'll need to get started
* python 3 installed locally
* virtualenv
* git
* an API key for spoontacular


### Installation

1. Get a free API Key for spoontacular, if you don't already have one [spoontacular](https://spoonacular.com/food-api)
2. Clone the repo
```sh
git clone https://github.com/louismillette/recipe_script.git
```
3. Create a virtualenv in the script directory.  I always call mine virt but any name works
```sh
virtualenv virt
```
4. Activate the virtualenv inside your console.
	- Go into the virtualenv, Scripts directory
	- Drag the 'Activate' file that matches your operating system into your open terminal
5. Install the requirements from the main project directory
```sh
pip install -r requirements.txt
```
4. Create a file called 'secrets.txt' inside the Food directory of the project files.  Paste your API key in the file AS IS.  Don't assign it a variable, just paste it in.

<!-- USAGE EXAMPLES -->
## Usage

1. Run the tests.py file to make sure everything is working on your system
```sh
python tests.py
```

2. Run the main script
```sh
python main.py
```

<!-- MARKDOWN LINKS & IMAGES -->

