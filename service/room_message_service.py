import json
from exceptions.unauthorized import Unauthorized


def verify_room(request, conn):
    try:
        obj = request.get_json()

        code = obj.get('code')

        sql = f"SELECT exists(select * from room inner join room_code on room.id = room_code.id_room where isactivate is true and room_code.code = ?)"
        values = (code,)

        cursor = conn.cursor()
        cursor.execute(sql, values)
        rs = cursor.fetchone()
        objR = {}
        if (len(rs) > 0):
            objR["contain"] = rs[0]

        if (objR["contain"] is 1):
            return 'ok'
        else:
            raise Unauthorized('not authorized')

    except Exception as err:
        raise err


def send_message(request, conn):
    try:
        obj = request.get_json()

        code = obj.get('code')

        sql = f"select room.id from room inner join room_code on room.id = room_code.id_room where isactivate is true and room_code.code = ?"
        values = (code,)

        cursor = conn.cursor()
        cursor.execute(sql, values)
        rs = cursor.fetchone()
        objR = {}
        if (len(rs) > 0):
            objR["id"] = rs[0]

        if (objR["id"] != None):
            text = obj.get('text')
            name = obj.get('name')

            sql = f"INSERT INTO room_messages(text, alias_name) values(?,?)"
            values = (text, name)
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            return 'ok'
        else:
            raise Unauthorized('not authorized')

    except Exception as err:
        raise err

def get_message(request, conn):
    try:
        obj = request.get_json()

        code = obj.get('code')

        sql = f"select room.id from room inner join room_code on room.id = room_code.id_room where isactivate is true and room_code.code = ?"
        values = (code,)

        cursor = conn.cursor()
        cursor.execute(sql, values)
        rs = cursor.fetchone()
        objR = {}
        if (len(rs) > 0):
            objR["id"] = rs[0]

        if (objR["id"] != None):
            lastid = obj.get('lastid')


            sql = f"select id, text, alias_name from room_messages where id > ?"
            values = (lastid,)
            cursor = conn.cursor()
            cursor.execute(sql, values)
            rs = cursor.fetchall()

            all_obj = []
            for r in rs:
                obj = {}
                obj["id"] = r[0]
                obj["text"] = r[1]
                obj["alias_name"] = r[2]
                all_obj.append(obj)

            return json.dumps(all_obj)
        else:
            raise Unauthorized('not authorized')

    except Exception as err:
        raise err