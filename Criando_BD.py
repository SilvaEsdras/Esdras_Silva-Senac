#
import sqlite3
# conectando
bd = sqlite3.connect('nome.db')
# definindo um cursor
cursor = bd.cursor()
# criando a tabela (shema)
cursor.execute("CREATE TABLE employees (id integer PRIMARI KEY, name text, salary real, department text, position text, hiredate text)")

cursor.execute("INSERT INTO employees (id, name, salary, department, position, hiredate)VALUES(1, 'Esdras', 988, 'HR', 'Gerente', '2022-02-4')")
bd.commit()

