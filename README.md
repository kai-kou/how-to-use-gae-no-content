# how-to-use-gae-no-content
Google App EngineでFlaskを利用する際のNo Content(204)ステータスコードの返し方

## Install

```sh
> git clone https://github.com/kai-kou/how-to-use-gae-no-content.git
> cd how-to-use-gae-no-content
> python -m venv venv
> . venv/bin/activate
> pip install -r requirements.txt
```

## Usage

### use flask

```sh
> flask run
```

### use gunicorn

```sh
> gunicorn -b 127.0.0.1:5000 app:app --log-level DEBUG
```

## Depoloy to Cloud App Engine

```sh
> vi app.yaml
> gcloud app deploy
```

## Access

### local

```sh
> curl 127.0.0.1:5000/good_no_content -o /dev/null -w '%{content_type}\n%{http_code}\n' -s

> curl 127.0.0.1:5000/bad_no_content -o /dev/null -w '%{content_type}\n%{http_code}\n' -s
```

### Cloud App Engine

```sh
> curl https://[GAE-ServiceName]-dot-[GCP-ProjectID].appspot.com/good_no_content -o /dev/null -w '%{content_type}\n%{http_code}\n' -s

curl https://[GAE-ServiceName]-dot-[GCP-ProjectID].appspot.com/bad_no_content -o /dev/null -w '%{content_type}\n%{http_code}\n' -s
```
