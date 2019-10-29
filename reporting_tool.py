import psycopg2

connect = psycopg2.connect('dbname=news')
cursor = connect.cursor()

def get_top_articles():
    sql = '''select articles.title, count(log.id) as views
        from articles join log
        on log.path = ('/article/' || articles.slug)
        group by(articles.title)
        order by views desc limit 3;'''
    cursor.execute(sql)
    return cursor.fetchall()

def print_result(action):
    if action == get_top_articles:
        type = ' views'
        print('Top 3 Articles:')
    elif action == get_top_authors:
        type = ' views'
        print('Top Authors:')
    else:
        type = '% errors'
        print('Days With More Than 1% Errors:')
    rows = action()
    for row in rows:
        print("%s - %s%s" % (str(row[0]), str(row[1]), type))
    print('---------------------------------------------------')

def get_top_authors():
    sql = '''select authors.name, count(log.id) as views
        from authors join articles on authors.id = articles.author join log
        on log.path = ('/article/' || articles.slug)
        group by(authors.name)
        order by views desc;'''
    cursor.execute(sql)
    return cursor.fetchall()

def get_requests_fail_days():
    sql = '''select requests.date, count*100::float/requests.requests as errors
    from requests join errors on requests.date = errors.date
    where count*100::float/requests.requests > 1;'''
    cursor.execute(sql)
    return cursor.fetchall()

def close_conn():
    """ Function to close the connection to the database """
    if cursor:
        cursor.close()
    if connect:
        connect.close()

if __name__ == '__main__':
    print_result(get_top_articles)
    print_result(get_top_authors)
    print_result(get_requests_fail_days)
    close_conn()
