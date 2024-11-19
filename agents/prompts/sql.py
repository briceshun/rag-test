sql_prompt = """
Write a SQL query using the information provided.
Use as few tables as possible if you can use mathematical operations to achieve the same result.
Only return the query
Do not explain it
"""

checker_prompt = """
Check the SQL query using the information provided. 
Make changes if necessary.
Only return the query
Do not explain it
"""