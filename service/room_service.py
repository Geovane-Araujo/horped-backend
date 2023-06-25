from config.database import new_connections_sqlite
from exceptions.internal import InternalServer
from util.util import gerar_sequencia_aleatoria


def create_room(request,conn):

    try:
        obj = request.get_json()
        #conn = new_connections_sqlite()

        name = obj.get('name')

        sql = f"INSERT INTO room(name) values(?)"
        values = (name,)


        cursor = conn.cursor()
        cursor.execute(sql, values)
        id_room = cursor.lastrowid

        room_code = gerar_sequencia_aleatoria(10)
        conn.commit()

        sql = f"insert into room_code(code, id_room, isactivate) values(?, ?, ?)"
        values = (room_code, id_room, True)
        cursor.execute(sql, values)
        conn.commit()

        return room_code
    except Exception as err:
        if(err.args != None):
            raise InternalServer(err.args[0])
        else:
            raise InternalServer(err.msg)
