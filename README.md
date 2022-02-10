## FASTAPI TODO REST
Sample fastAPI todo app using SQLModel, Sqlite

## INSTALLATION
```bash
$ pip install fastapi pydantic sqlmodel "uvicorn [standard]"
```

## RUNNING
```bash
$ uvicorn app.main:app --reload
```

## RUNNING USING DOCKER
You need install docker first

```bash
$ docker build --tag yourimagename .
```
```bash
$ docker run -d --name yourcontainername -p 8080:80 yourimagename
```