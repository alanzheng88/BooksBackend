# Books
Webservice to search a database of books with implementation organized using a functional structure (organize files of project by what they do)

```
.
├── app
│   ├── __init__.py
│   ├── main
|   |   |-- __init__.py
│   │   ├── controller (app endpoints)
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── model (database models)
│   │   │   └── __init__.py
│   │   └── service (business logic of app)
│   │   |    └── __init__.py
|   |   |-- config.py (application settings - dev/test/prod configs)
│   └── test
└── requirements.txt
|-- manage.py (application entry point)

```

## Environments
To set the environment, use either: dev, test or prod when setting environment variable <APP_ENV>. dev is the default option when running app if no environment variable is set
```
// linux environment
export APP_ENV=test
```

## Prerequisites
```
database: mysql@5.7
tools: python3, pip3

// For MacOS Sierra
brew install mysql@5.7

```

## Setup

1. Run the following
```
pip3 install -r requirements.txt
./scripts/configure
python3 manage.py run
```

## Issues
```
Fixing mysql set-up (complete removal and reinstall)
  - https://gist.github.com/vitorbritto/0555879fe4414d18569d
  - https://stackoverflow.com/questions/50874931/the-post-install-step-did-not-complete-successfully-mysql-mac-os-sierra
```

## TODO

