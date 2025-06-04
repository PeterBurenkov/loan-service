Project structure
1. api_models - models exposed by FastAPI
2. infrastructure - generic communication with resources like (PostgreSql, Redis, Kafka)
3. domain - repositories that know about domain models and communicate with infrastructure layer
4. models - missing (todo), I use api_models instead
5. usecases - bussiness logic scenarios (used in app entry points - see below)

App entry points
1. main_fastapi.py  - FastAPI application
2. main_kafka.py - Kafka consumer application
