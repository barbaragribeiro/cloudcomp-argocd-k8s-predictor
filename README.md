## From within the cluster

### Making a request

A request can be made using `curl` through the endpoint `10.244.0.74:5005/api/american`. which takes only POST requests. The tweets are passed through the `data` in the request, such as follows:


```bash
curl -X POST 10.244.0.74:5005/api/american --data '{"text" : "#covid"}'
```


### Evaluating multiple tweets in one request

Alternatively, one can send a single request to evaluate a list of tweets. In this case, it is returned a list of values accordingly.

```bash
foo@bar:~$  curl -X POST 10.244.0.74:5005/api/american --data '{"text":["#covid", "This is english covid and maybe symptoms treat home idk what else to write scared shit", "Big trip 5 mi to north...checked out Yountville (another ghost town, sadly) but found the one open spot w take away drinks and a cozy outdoor firepit. #covid19 #margaritamonday #yountville #socialdistancing"]}'
{
  "predicted": [
    0, 
    0, 
    1
  ]
}

```

## From outside the cluster

Alternatively, the api can be accessed from outside the cluster by first piping as follows:

```bash
ssh -fNT -L <local-port>:10.244.0.74:5005 <username>@69.195.152.146 -p 4422
```

Then proceed as above, but using the endpoint `localhost:<local-port>/api/american`
