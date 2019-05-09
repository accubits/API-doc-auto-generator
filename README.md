# API doc auto generator
Simple app to generate API documentation using Postman collection


Step 1:
Copy the **docker-compose.yaml** file to a folder
```yml
version: '3.2'

services:
  web:
    image: accubits/api-doc-auto-generator:latest
    ports:
      - ${PORT:-4567}:4567
    volumes:
      - ./output/output.md:/usr/src/app/source/index.html.md
    depends_on:
      - json2md
  json2md:
    image: accubits/json2md:latest
    volumes:
      - ${INPUT_FILE}:/code/postman.json
      - ./output:/code/output
```

Step 2:
Copy the **.env** file and change the Postman collection json file location.
```
INPUT_FILE=./apipost.json
PORT=4567
```

Step 3:
Run the docker-compose

```yaml
docker-compose up -d
```

To update the API doc with new data,
- Copy new collection
- Run ***docker-compose up json2md***