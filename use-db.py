import toolforge

conn = toolforge.connect('mediawikiwiki_p')

with conn.cursor() as cur:
    cur.execute("SELECT * from user_groups LIMIT 2;")
    for x in cur:
        print(x)
