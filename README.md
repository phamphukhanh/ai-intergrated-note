# Note-taking Application (with OpenAI API integrated for summarizing)

## Introduction

Notaki is a note-taking web-application using Django framework. Including basic functionalities, CRUD operations for notes and OpenAi API integrated within these features to summarize your note content, giving an explicit view for user to catch up their information whenever the content is not well-organized.
Notice: The openaikey.py will not be included, you must create one and add your key (or create a environment variable named OPENAI_API_KEY) into it in order to use the "Summarizing the note content" feature. The file is placed in the main directory.

## Installation

### Prerequisites

Before installing the application, make sure you have the following dependencies installed using ```pip install <package_name>``` :

- **libmysqlclient-dev**: for installing mysqlclient.
- **mysqlclient**: for connecting to local MySQL.
- **langchain**: for utilities of langchain library.
- **langchain-openai**: for supporting langchain in using OpenAI API.

### XAMPP Setup

1. Download and install XAMPP from [here](https://www.apachefriends.org/index.html).
2. Once installed, you can start XAMPP with the following command:

    ```bash
    sudo /opt/lampp/lampp start
    ```

3. Import the ```note_management.sql``` included in the repository.
### Running the Server

To run the server, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/phamphukhanh/ai-intergrated-note
    cd <repository_directory>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the server:
    ```bash
    python manage.py runserver
    ```
    or
    ```bash
    python3 manage.py runserver
    ``` 
The server should now be running locally on your machine.

## Usage

Explore some basic functionalities such as:
  - Adding a new note
  - Deleting a note
  - Modifying an existed note
  - Searching for a note
  - Summarizing the note content
