

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

Just build the docker image and run the it. For example
```bash
docker build -t image:latest .
docker run -p $SERVER_PORT:$SERVER_PORT image:latest
```

### Usage

After deployment, to see the Swagger UI, go to
```bash
{service_public_address}/v1/ui
where {service_public_address}
is of the format `ip:port`
```

For example I had my service up and running on my personal server, given the following input
```json
My name is Sarah and I live in London and I work at Google Left on March 6th 2020. My job there mostly involved in leading a team of sotware developers in two projects about self driving cars.
I had a very nice time at Google.
```
The output would be
```json
{
  "category": "Technology",
  "comment": "Sarah lives in London and she works at Google. Her job at Google left on March 6th 2020. She was involved in leading a team of sotware developers in two projects about self driving cars. Sarah had a nice time at Google and she had a very nice time there.",
  "named_entities": [
    {
      "Person": "Sarah"
    },
    {
      "Location": "London"
    },
    {
      "Company": "Google"
    },
    {
      "Company": "Google"
    },
    {
      "Date": "2020-03-06"
    }
  ]
```
![Swagger UI example](https://lh3.googleusercontent.com/_2Xh6Txg1qznAaAD3q_FFrl1PJG6rJS4q-jmEB5f9CjwjfyZxBN5dt0g-EhtLbdzymIu5lbCRL_C01zzPLnnMvfYz7kJp91ZPUxWtMh-vliOaKBfSLSC6n24yz9H1UFpEkwASkFWxlnbL3LrEYrTq-LOeSkVexPejsG3ZPCx0MJ3Q1hybp0JH5pJuHe9E2WEJl5D_OoDSZyjNC0uuKZW4U08D0QT1Dd7lFMsD3QdwZkFGXmzajtjsehxv2GyDUFl5DmJsX99EXQbzNz2y7h2kJmq6fJGOob1doNjjX-Qu3RJSmTbXxgFodQLuYo0FYeH14CjtMriLiToDiJkWJjTWM-iLUvoE0e8_OqE8SLuvgeBHm56Po55QuR0Yl6NCq6DDKXNGPX1uOSraeYUrQHPcGQSu7eEwWcdix2VV_u04NhFOjSwfrJbgPHa7rn5py_5viWJDe9iDZAzW_UgqmAVlZm_XmCtaTHPadbA-ANzQoD9Db2nlhRuCnJfqw9_sYG8vVjag3tAAAifXCbouGJNyAO1JKdxJBlLaNB_wLpuJIz-Z1iFhd7GAUvoKdtk8_XeLR1sHWW2XFreiODqndEUm3vXHg5sEqI6lSXmr7QHtZbOTN45beM3FeKtn8BCuS6Cp6bFdjgy4KyIPELfPYaa7O2kOyy1xqQwOMPY49fBLoupu1QQAiSwhqB9Sr1sDxg3rifSl-3Z9HSXSjxFPnopWIvSSCy54vJWb_hbY46KKMJeydN7TNnLaYxkUvZSPQ=w1027-h607-no?authuser=0)
![Swagger UI example 2](https://lh3.googleusercontent.com/t9hduPrI8XH8iWBHuDpyzX2UxCGhZgvOw9peUaIoNU-RJjvUuinZADcuIucxPs_-X2_3_SYrgVCdSz9BSdCjim8_iWM7YOaFXzuQSX7hTjH0zbn53f558KX5Vp2k3YwC-2ekW9NqXukP2SQTHtCfh7iD0dJaoHUewQJ56lLQycVX3iRrQ5OvFYwjCfCWelZqN-CM8wiRk1bJiTFQIDjmyYFdIFfHLXr2ksXLPJEmWM_wnQvhPjCyS4ureARbbNtAOhCheXc18VM6jzPke7bnsiFFNb4giLWkkXdA2UPE5U5bEuU4lmh5qUy8_SOVtJ8dpq2gfYQqIAkmlclhcdkM9djcgelolnO0f3lKT1PTt5VrRvU-7P4KKdrAajmgV8ZcJjtywb5s_gx2ByA3EUzopU7i-OJeob_OiwV4F0Ryq6JYfE-8YXrndCW4iUS-UHOzvMAS64IUXPb_IOVHwjJGH6wGU6ltWxKSXDqelVhH_wZ9E5g-vmTadbRKN5OisyatalcJfnX583KbJvA6eKZhg7SqAf9F34cEJnNe1lARcw0Vg_lhslsiRlynmJ7h0-5rLDFMwJKdpxVrw2jYJBKvzECZNV999uOM1pKuFC5cCYXrdinAMQYvZW4ktQATdgI-IdoUveR728toz33KUqXGvE4YwdBnJAET2Qxrz1ZqUMNtIp2RWrl53PGxFByWz5I_qNH8zmi9UPqpY975fp4_lDYicuw4ZgwDvzVG-ZFOd1ct_c38KP6awXhfkJe6nQ=w1051-h627-no?authuser=0)
### Running Tests
  
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
