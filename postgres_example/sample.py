from contextlib import contextmanager

import psycopg2 as pg2


PG_SETTINGS = {
    "database": "dev",
    "user": "postgres",
    "password": "password",
    "host": "postgres",
    "port": "5432",
}


@contextmanager
def pg_cur(auto_commit=False):
    with pg2.connect(**PG_SETTINGS) as conn:
        with conn.cursor() as cur:
            yield cur

        if auto_commit:
            conn.commit()


def init():
    '''
    create extension cube;
    '''
    with pg_cur(auto_commit=True) as cur:
        print("create table")
        try:
            cur.execute("""
            DROP TABLE sample
            """)
            cur.execute("""
            CREATE TABLE sample (
                obj_id char(24) not null,
                question text not null,
                vector cube not null
            )
            """)
            print("create table done")
        except Exception as e:
            print(f"pg message: {e}")

def get_object_id(num):
    default = 100000000000000000000000
    return str(default+num)

def make_dataset():
    with pg_cur(auto_commit=True) as cur:
        try:
            for i in range(10):
                v = f"({i}, 0.0)"
                text = f"text_{i}"
                cur.execute("""
                    insert into sample (obj_id, question, vector)
                    values (%s, %s, %s::cube)
                """, (get_object_id(i), text, v))
            print("update done")
        except Exception as e:
            print(f"pg message: {e}")

if __name__ == "__main__":
    init()
    make_dataset()
    with pg_cur(auto_commit=True) as cur:
        obj_ids = tuple(get_object_id(i) for i in range(5))
        sql = """
            select obj_id, question, vector, vector <-> %(vs)s::cube
            from sample
            where obj_id in %(obj_ids)s
        """
        params = {'vs': '(0, 3)', 'obj_ids': obj_ids}
        cur.execute(sql, params)
        rows = cur.fetchall()
        breakpoint()
        print("end")
