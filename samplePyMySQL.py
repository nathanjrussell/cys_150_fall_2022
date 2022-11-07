import pymysql


with conn.cursor() as cursor:
    sql = "select id_number, first_name, last_name, city, state from accounts"
    cursor.execute(sql)
    #conn.commit()
    results = cursor.fetchall()
    for result in results:
        testStr = "Good Morning {0!s} {1!s}! I Hope you have a great day in {2!s}, {3!s}".format(result['first_name'],result['last_name'],result['city'],result['state'])
        print(testStr)
    conn.close()
