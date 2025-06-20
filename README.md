# Common Number Pairs API (with IaaC)

This project deploys a RESTful API using the FastAPI framework, leveraging AWS SAM (Serverless Application Model) to define the infrastructure as code.

## Infrastructure: AWS SAM

AWS SAM is a framework for building serverless applications. It provides a way to define your application's resources and dependencies using YAML or JSON templates. The template.yaml file in this project defines the necessary AWS resources, such as API Gateway, Lambda functions, and IAM roles.

## Project Structure

- **app/**: Contains the FastAPI application code.
- **layers/fastapi/**: Directory containing dependencies for the FastAPI layer.
- **tests/**: Unit tests for the application.
- **poetry.lock**: Poetry lock file to manage Python dependencies.
- **pyproject.toml**: Poetry configuration file.
- **template.yaml**: AWS SAM template defining the infrastructure.

## Local Development

### Prerequisites
- Install AWS SAM CLI: [AWS SAM CLI Installation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- Install Python 3.13
- Install Poetry: [Poetry Installation](https://python-poetry.org/docs/#installation)

### Using Makefile

The `Makefile` provides targets to help with local development:

```sh
make all       # Runs format, lint, and test
make test      # Runs all tests
make format    # Formats code using ruff
make typecheck # Checks for type errors using mypy
```

### Running the API Locally

# Create a virtual environment
```sh
python -m venv .venv  #Make sure that you are creating the virtual environment with Python 3.13.
```

# Activate the virtual environment
```sh
source .venv/bin/activate
```

# Install dependencies using Poetry
```sh
poetry install --no-root
```

There are two ways to run the API locally:

1. **Using AWS SAM:**
   ```sh
   sam build && sam local start-api
   ```

2. **Using Uvicorn:**
   ```sh
   uvicorn app.main:app --reload
   ```

## Deployment

To deploy the API using AWS SAM, follow these steps:

1. Ensure you have the necessary permissions to create and manage AWS resources.
2. Configure your AWS credentials.
3. Deploy the stack:
   ```sh
   sam build
   sam deploy --guided
   ```

Follow the prompts to provide required parameters such as the environment, API domain, certificate ARN, and hosted zone ID.

## Public API

- **API Endpoint:** `https://nordhealth-api.ownspace.cloud`
- **Interactive OpenAPI Documentation:**
  - Swagger UI: `https://nordhealth-api.ownspace.cloud/docs`
  - ReDoc: `https://nordhealth-api.ownspace.cloud/redoc`

## API Endpoints

- **Get Info:** `/v1/nordhealth/get_info/`
- **Extract Numbers Pairs:** `/v1/nordhealth/extract_numbers_pairs/`

## Contributions

Contributions to this project are welcome. Please ensure that your code adheres to the formatting and type-checking standards defined in the Makefile.

## License

This project is licensed under the MIT License.
