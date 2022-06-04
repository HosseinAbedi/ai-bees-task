

 - [Social Media Comment Generator Interface API](#social-media-comment-generator-interface-api)
 - [Environment Variables](#environment-variables)
  - [Launch](#launch)
  - [Usage](#usage)
  - [Running Tests](#running-tests)
  - [Dependencies](#dependencies)
  - [Possible Improvements in the Future](#possible-improvements-in-the-future)
  - [API](#api)

## Social Media Comment Generator Interface API

Creating comments for social media posts.
The service is comprised of different parts:

* In the first part, a user puts in a text (a post) as an input. Then, user's input is fed to a [zero-shot classifier](https://huggingface.co/facebook/bart-large-mnli) to predict the association (relatedness) of the text to a set of predefined class labels (For example, `['Sports', 'Technology', 'Medicine', "Politics", "Arts"]`, we can extend this list easily). We use a multi-label classification problem given the labels and the text and assign most probable class label to the text.
 * In the second part using a [state of the art named entity recognition model](https://huggingface.co/dslim/bert-base-NER) we extract the name Companies, Persons and Locations. Along with this model we use a Python library to parse the text for date values.
 * The third part is about generating comment about the post given the information extracted. To do this properly we can use a language model but since publicly available model need relatively powerful  hardware to host we switch to and alternative method and that is using a  [text summarization model](https://huggingface.co/philschmid/distilbart-cnn-12-6-samsum) to generate the comments.
 After going through these components, result is store in a MongoDB instance. The whole system is served using Flask framework as a Restful API. The architecture of the system is shown in the following picture: 
 ![Arch](https://lh3.googleusercontent.com/tdClz7dna1i7KT4OlRJLR-ZvXWqthk6b73WHGdMKc7Zp66VqCxHJ9IbPdUOCp4NuhqSsOO5vRtVkdwTn45iVxpmsgjs_RBOJXag9QyJt7ZJW3bxr8k7IgtswmxrZjTLfTmWZtle52VMBdGiKxJFHURwcW_5-NWJaOa92ICyeGVnR7AiccCSxUTNAM5U6UD2_EpRtF0mtRKNbS1IDYNGz5npET5g9OG8AijWnbj6FSWbx9kBUhDpVCL03BEBfnPEUvoeb5OKnIdWhM6Xqa2S-vZhB4u--AafAPKKn2bMZvXD6-cNDxEqavxEXZk0bhGp81gZ_jSKuX1lTm1y8lq8JNd_7E6pV1LGb6Gzaw0ErKbgv0_uHbr1OAbf06gsfWYX-ts0h-sPdjUbGzEdCgdqJ6ZZS5JqiedHgEzYk-TMGK59fMzcJyC7EcUt9R7cOW4TS1gvn0Be9e1tYlD1il7ESmjWiZQqRLb0piqaRNF7As-xFFy7gSa8jhkfCR2vqjay00NYeBjSfscKYwYvUgG_fiHyuHCs817XoS4GoTffDjwlXHgeRkeiQRXuU4P6t3aQuOB44bO7WC_I3xmfQr0y7I740awydozED0FD_at4Rr7QPBUchvqjZS6oJpBKWOgC71Je0L-Jtk3vcArWyA4hobrFfUawBaiA2N588DKE5XxwRchY5L0dCZYWhlr3QE7fVjZFziNz6Nb53VK6ybDChwNY_COMIyd0WTKgk698xaB1qOiR3g7GHDUc7wQKjqg=w502-h601-no?authuser=0)


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
```text
My name is Sarah and I live in London and I worked at Google Left on March 6th 2020. My job there mostly involved in leading a team of sotware developers in two projects about self driving cars.
I had a very nice time at Google.
```
The output would be
```json
{
  "category": "Technology",
  "comment": "Sarah worked at Google left on March 6th 2020. Her job was to lead a team of sotware developers in two projects about self driving cars. Sarah had a very nice time at Google. Sarah lives in London and she had a nice time there.",
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
}
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
It runs the tests and create a report in the `coverage.xml`, this file is used by tools like [SonarQube](https://www.sonarqube.org/) for generating the final report.


### Dependencies

* a MongoDB instance (on your local machine or in MongoDB cloud). To set up the minimum requirement for this project you can use the docker compose file in `MongoDB-Scripts`. Run the following commands:
```bash
pip install docker-compose
docker-compose up -d
```
In here, I used a [MongoDB Atlas Shared Instance](https://www.mongodb.com/pricing?utm_content=controlpricingterms&utm_source=google&utm_campaign=gs_footprint_row_search_core_brand_atlas_desktop&utm_term=mongodb%20pricing&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624584&adgroup=115749713463&gclid=Cj0KCQjwheyUBhD-ARIsAHJNM-My4GSyXS5EJe1NbPPLBel6jLmIfCKLs5KULtx8Elb06wxq7_VJtAoaAm12EALw_wcB) that is free to use. You can get your own instance up and running in less than a ten minutes.


### Possible Improvements in the Future

* There are a couple of ways to improve the performance of the service
	* Apart from replacing the model with a better one, NER models can be improved by integrating gazetteer based models with the current model, especially enhance the quality of the model in the case PERSON and COMPANY entities.
	* To generate comments, the best practice would be  to use a language models like [GPT-J-6B](https://huggingface.co/EleutherAI/gpt-j-6B?text=My+name+is+Merve+and+my+favorite) (given that we have a very powerful hardware) or [GPT-3](https://openai.com/api/) (given than we have an account). For example, with GPT3 we can create a training data set of topics, named entities and comments. Then we finetune a model based on this data to build a state of the art model for comment generation.
	* To run the current models efficiently and with low latency we need to either host the models on a hardware with decent GPU or use available services like [NLPCloud](https://nlpcloud.io/) (the paid plans) to have a very good performance in the case of response time.


### API 
---
title: Social Media Comment Generator Interface API v0.1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
---

> Code samples

```shell
# You can also use wget
curl -X GET /v1/getComment?post=string

```

```http
GET /v1/getComment?post=string HTTP/1.1

```

```javascript

fetch('/v1/getComment?post=string',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

result = RestClient.get '/v1/getComment',
  params: {
  'post' => 'string'
}

p JSON.parse(result)

```

```python
import requests

r = requests.get('/v1/getComment', params={
  'post': 'string'
})

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/v1/getComment', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/v1/getComment?post=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/v1/getComment", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /getComment`

*Generate text from a social media post and extract it's topic and entities in the post.*

<h3 id="src.methods.generate_comment_endpoint-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|post|query|string|true|none|

<h3 id="src.methods.generate_comment_endpoint-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|ok|None|

<aside class="success">
This operation does not require authentication
</aside>


