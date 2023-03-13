from db.db import get_connection

def delete_teacher(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.callproc('delete_teacher', args=(id,))
            connection.commit()
        connection.close()
        print('Teacher deleted successfully')
    except Exception as ex:
        print('Error deleting teacher:', ex)

def insert_teacher(name, surname, email, created_date):
    success=''
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.callproc('insert_teacher', args=(name, surname, email, created_date))
            connection.commit()
        connection.close()
        print('Teacher adding successfully')
        success= 'Teacher added successfully'
    except Exception as ex:
        print('Error adding teacher:', ex)
        success = 'Error adding teacher:', ex
    return success


def search_all_teachers():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.callproc('search_all_teachers')
            resultset = cursor.fetchall()
            teachers = []
            for row in resultset:
                teacher = {
                    'id': row[0],
                    'name': row[1],
                    'surname': row[2],
                    'email': row[3],
                    'created_date': row[4].strftime('%Y-%m-%d %H:%M:%S')
                }
                teachers.append(teacher)
        connection.close()
        return teachers
    except Exception as ex:
        print('Error searching teachers:', ex)

def search_teachers(id=None):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            if id:
                # Si se proporciona un valor para el parámetro id, buscar solo el profesor con ese id
                cursor.execute('search_teacher', args=(id))
            else:
                # Si no se proporciona un valor para el parámetro id, buscar todos los profesores
                cursor.execute("search_all_teachers")
            resultset = cursor.fetchall()
            teachers = []
            for row in resultset:
                teacher = {
                    'id': row[0],
                    'name': row[1],
                    'surname': row[2],
                    'email': row[3],
                    'created_date': row[4].strftime('%Y-%m-%d %H:%M:%S')
                }
                teachers.append(teacher)
        connection.close()
        return teachers
    except Exception as ex:
        print('Error searching teachers:', ex)

def search_teachers_(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.callproc('search_teacher', args=(id,))
            resultset = cursor.fetchall()
            teachers = []
            for row in resultset:
                teacher = {
                    'id': row[0],
                    'name': row[1],
                    'surname': row[2],
                    'email': row[3],
                    'created_date': row[4].strftime('%Y-%m-%d %H:%M:%S')
                }
                teachers.append(teacher)
        connection.close()
        return teachers
    except Exception as ex:
        print('Error searching teachers:', ex)
        return None


def update_teacher(id, name, surname, email):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.callproc('update_teacher', args=(id, name, surname, email))
            connection.commit()
        connection.close()
        print('Teacher updated successfully')
    except Exception as ex:
        print('Error updating teacher:', ex)



def search_all_teachers_test():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.callproc('search_all_teachers')
            resultset = cursor.fetchall()
            for row in resultset:
                print(row)
        connection.close()
    except Exception as ex:
        print('Error searching teachers:', ex)
        
def search_teacher_test(id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.callproc('search_teacher', args=(id,))
            resultset = cursor.fetchall()
            for row in resultset:
                print(row)
        connection.close()
    except Exception as ex:
        print('Error searching teacher:', ex)