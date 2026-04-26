
from langchain_core.messages import HumanMessage, SystemMessage

SQL_SYSTEM_PROMPT = """
  You are a helpful assistant that can answer questions about the database.

  Shema:
  {schema}

  Students:
  {students}
"""


schema = """
  CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT
  )
"""

students = """
  INSERT INTO students (id, name, age) VALUES (1, 'John', 20), (2, 'Jane', 21), (3, 'Jim', 22)
"""

system_message = SystemMessage(content=SQL_SYSTEM_PROMPT.format(schema=schema, students=students))