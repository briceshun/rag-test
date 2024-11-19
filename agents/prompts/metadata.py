metadata_prompt = """
You are an AI model trained to analyze database schemas and provide detailed descriptions. 
Given the following table sample and information schema, please:

1. Write a short description the table, including its columns and data types. BE SIMPLE AND CONCISE.
2. Suggest the main use case for this table in a database.

I will provide you with the following information:
{   "sample": "...",
    "schema": "...",
}

Please provide a detailed and structured response with no code formatting using the following format:
{   "description": '...",
    "use case": '...",
}
"""