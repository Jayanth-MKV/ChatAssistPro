# FAQ Customer Support Chatbot API

## Setup

### Prerequisites

Ensure you have the following installed:

- Python (>=3.10)
- pip (package installer for Python)
- [Poetry](https://python-poetry.org/)

### Installation

1. Clone the repository:

   ```bash
   git clone <url>
   cd customer-support-chatbot
   ```

2. Install the required Python packages using Poetry:

   ```bash
   poetry install
   or
   pip install fastapi uvicorn spacy

   ```


4. Run the app:

   ```bash
    uvicorn main:app --reload
   ```

### Using Docker

If you prefer using Docker, you can pull the Docker image and run the application in a container:

1. Pull the Docker image:

   ```bash
    docker build -t chatbotapi .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 chatbotapi
   ```

This FastAPI app provides two endpoints:

/chat (POST): Accepts a JSON payload with a "message" field and returns the chatbot's response.
/faqs (GET): Returns the first 5 FAQs from the loaded FAQ list.

You can test the API using tools like curl, Postman, or by creating a simple frontend application that makes requests to these endpoints.


## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](MIT) file for details.