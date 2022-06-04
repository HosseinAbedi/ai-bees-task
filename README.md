

 - [Social Media Comment Generator Interface API](#social-media-comment-generator-interface-api)
 - [Environment Variables](#environment-variables)
  - [Launch](#launch)
  - [Usage](#usage)
  - [Test](#test)
  - [Dependencies](#dependencies)

## Social Media Comment Generator Interface API

Creating comments for social media posts.


## Environment Variables

Here's the list of the environment variables needed to run the service:
| Variable                | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| SERVER_PORT              | Server port number                                           |
| MONGODB_USERNAME              | MongoDB username |
| MONGODB_PASSWORD                 | MongoDB password |
| MONGODB_HOST           | MongoDB host address     |
| MONGODB_DATABASE | MongoDB database name  |
| MONGODB_COLLECTION | MongoDB collection name  |


### Launch

Just build the docker image and run the image. For example
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

	* Python3.7 virtual environment (for running tests), can be set up with
	```bas
	python3.7 -m venv venv
	source venv/bin/activate
	pip install -U pip
	pip install -r requirements.txt
	```
* `.env` file containing all the ENVs required 
- Running Tests

For running unit tests, please run the script `run_tests.sh` with 
```bash 
bash run_tests.sh
```
It runs the tests and create a report in the `coverage.xml`, this file is used by tools like SonarQube for generating the final report.


### Dependencies

* a MongoDB instance (on your local machine or in MongoDB cloud). To set up the minimum requirement for this project you can use the docker compose file in `MongoDB-Scripts`. Run the following commands:
```bash
pip install docker-compose
docker-compose up -d
```


### Possible Improvements in the Future

* There are a couple of ways to improve the performance of the service
	* NER models can be improved by integrating gazetteer based models with the current model, especially enhance the quality of the model in the case PERSON and COMPANY entities.
	* To generate comments, the best practice would be  to use a language models like [GPT-J-6B](https://huggingface.co/EleutherAI/gpt-j-6B?text=My+name+is+Merve+and+my+favorite) (given that we have a very powerful hardware) or [GPT-3](https://openai.com/api/) (given than we have an account). For example, with GPT3 we can create a training data set of topics, named entities and comments. Then we finetune a model based on this data to build a state of the art model for comment generation.
	* To run the current models efficiently and with low latency we need to either host the models on a hardware with decent GPU or use available services like [NLPCloud](https://nlpcloud.io/) (the paid plans) to have a very good performance in the case of response time.
