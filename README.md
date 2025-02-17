Requirements

Build a Retrieval Augmented Generation (RAG) system that leverages Weaviate as its vector database.
Design a performant system that efficiently retrieves answers from uploaded documents in various formats.
Develop a robust backend system focused on data ingestion, embedding generation, indexing, and retrieval.

1. Document Ingestion & Embedding Generation
* Supported Formats:
    * PDF
    * DOCX
    * JSON
    * TXT
* Ingestion Pipeline:
    * Document Upload: Implement functionality to upload documents in any of the above formats.
    * Embedding Creation: For each uploaded document, generate embeddings using an appropriate model (e.g., OpenAI’s text-embedding, Hugging Face models, etc.).
    * Storage: Store the generated embeddings within Weaviate.
    * Automation: Develop an automated pipeline that:
        1. Monitors for new document uploads.
        2. Processes and generates embeddings.
        3. Indexes the embeddings in Weaviate.
2. Question-Answer API Endpoint
* Functionality:
    * APIs to ingest documents and update a document. Note: Update is equivalent to re-uploading the entire doc with the changes.
    * Create an API endpoint that accepts queries against individual documents.
    * The system should retrieve the most relevant text snippet(s) from the queried document stored in Weaviate.
* Response Requirements:
    * Return the answer with associated metadata such as:
        * Snippet of the retrieved text.
        * Document ID or other relevant identifiers.
3. Performance Optimization
* Efficient Retrieval:
    * Ensure that the RAG system is optimized for quick and accurate retrieval.
    * Implement best practices such as:
        * Document chunking for handling large documents.
        * Precomputed embeddings to reduce latency during query time.
4. Deployment
* Platform:
    * Deploy the application on a cloud platform of your choice (e.g., AWS, GCP, Azure, Render, Railway, etc.).
* Accessibility:
    * Provide publicly accessible endpoints for testing.
    * Include clear deployment instructions in your documentation.
5. JSON Data RAG Extension (Bonus)
* Enhanced Functionality (Optional):
    * Extend the system to support structured queries for JSON data.
    * Capabilities may include:
        * Retrieving the maximum or minimum value of a specified field.
        * Performing aggregations (e.g., sum, average) on numerical fields.

Deliverables
1. Code Repository:
    * The repository should contain:
        * The document ingestion pipeline.
        * API endpoint implementation.
        * Deployment scripts.
    * Include a README.md file with comprehensive setup and usage instructions.
    * You’re free to use GenAI tools like GPT/Claude.
2. Live Deployment:
    * Provide a publicly accessible URL for testing the system.
3. Documentation:
    * A detailed explanation of the system architecture and workflow.
    * API documentation that explains the endpoints and their usage.
4. Design Write-Up (Optional):
    * Summarize your design choices, including any trade-offs.
    * Highlight potential improvements and challenges encountered along with their solutions.

Functional Requirements
* Correctness & Completeness:
    * Does the system correctly ingest documents and answer queries?
* Code Quality & API Design:
    * Is the code well-organized, maintainable, and documented?
* Deployment:
    * Is the application successfully deployed and easily testable via public endpoints?
* Bonus Features:
    * Are the extended JSON data aggregation capabilities implemented effectively?
* Clarity & Documentation:
    * Are the provided instructions clear, comprehensive, and easy to follow?

Solution
