from db import get_connection 

try:
    connection = get_connection()
    with connection.cursor() as curso:
        curso.execute('call select_alumnos()')
        resultset=curso.fetchall()
        for row in resultset:
            print(row)
    connection.close()
    
except Exception as ex:
    print('error', ex)