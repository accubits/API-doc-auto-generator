# API doc generator from Postman collection
Simple app to generate API documentation from Postman collection

#### Initial setup
Step 1:
Clone the repo. https://github.com/accubits/API-doc-auto-generator.git

Step 2:
Replace the JSON in `apipost.json` with Postman collection JSON

Step 3:
Run the docker-compose file

```yaml
docker-compose up -d
```

#### Udate the API doc with new data
Step 1:
Copy new collection

Step 2:
Run `docker-compose up json2md`


Core repo's:
- [Slate](https://github.com/accubits/slate)
- [json2md](https://github.com/accubits/json2md)