
- [Parser Service](#parser-service)
- [Environment Variables](#environment-variables)
  - [Launch](#launch)
  - [Usage](#usage)
  - [Test](#test)
  - [Dependencies](#dependencies)

## Parser Service

Parsing service for resumes in various languages.


## Environment Variables

| Variable                 | Default Value | Description                                                  |
|--------------------------|---------------|--------------------------------------------------------------|
| SERVER_PORT              | None          | Server port number                                           |
| VNUMBER                  | None          | Version number                                               |
| SENTRY_DSN               | None          | Sentry DSN string key                                        |
| APP_ENV                  | None          | Sentry environment identifier (staging, test and production) |
| DAXTRA_ACCOUNT          | None          | Daxtra accound id key                                            |
| DAXTRA_JWT_TOKEN | None          | Daxtra JWT token for their parsing service                                     |
|DAXTRA_PARSER_URL            | None          | Daxtra parsing service url
|GOOGLE_APPLICATION_CREDENTIALS           | None          | Path to serviece account json file (google cloud service account for document ai service)
|DOCUMENT_AI_PROJECT_ID            | None          | Google document ai project id                       |                        |
|DOCUMENT_AI_RESOURCE_LOCATION           | None          | Google document ai project's location                      |                        |
|DOCUMENT_AI_PROCESSOR_ID            | None          | Google document ai project's processor id                       |
|NUMBER_OF_PERMISSIBLE_PAGES_TO_PARSE            | None          | Maximum permissible number of pages in a resume file                        |
|AUTH_TOKEN            | None          | Authentication token (a uuid4 string)                        |

### Launch

Just build the docker image and run the image. Example
```bash
docker build -t image:latest .
docker run $SERVER_PORT:$SERVER_PORT image:latest
```

### Usage

After deployment, to see the Swagger UI, go to
```bash
{service_public_address}/v1/ui
```

You can also find the documentation in [postman](https://qpageapi.postman.co/workspace/QPage~0fa24148-4a10-474b-9860-452941cbc985/folder/15375452-f7886196-feab-43d6-a671-6f8655925f2c?ctx=documentation).

### Test

  
- Dependencies

*  `Sonar-scanner` for running the tests (path to Sonar-scanner should be specified in the last line of `run_tests.sh`)

* A configuration file called `sonar-project.properties` (required by sonar-scanner for sending the report to sonarqube website)

* Python3.7 virtual environment (for running tests), can be set up with
```bas
python3.7 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```
* .env file containing all the ENVs required
- Running Tests

For running unit tests, please run the script `run_tests.sh`. It run the tests and create a report in the `coverage.xml`, this file is used by SonarQube for generating the final report.


### Dependencies

None
