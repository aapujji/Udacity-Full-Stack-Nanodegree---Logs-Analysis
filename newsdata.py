#!/usr/bin/env python2.7
import psycopg2

DBNAME = "news"

query_one = "What are the most popular three articles of all time?\n"
query_two = "Who are the most popular article authors of all time?\n"
query_three = "On which days did more than 1% of requests lead to errors?\n"

query_one_ans = ("select title, count(*) from articles join log "
                 "on log.path like concat('%',articles.slug,'%') "
                 "group by title, path order by count(*) desc limit 3;")
query_two_ans = ("select name, count(*) from authors join articles on "
                 "articles.author = authors.id join log on log.path "
                 "like concat('%', articles.slug, '%') group by name,"
                 "log.path order by count(*) desc limit 3;")
query_three_ans = ("select date, perc from err_perc group by date,"
                   "perc having perc >= 1 order by perc;")


def get_query(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        q = c.fetchall()
        db.close()
        for row in q:
            print row
        print "\n"
    except:
        print "Cannot connect to database."

if __name__ == '__main__':
    print query_one
    get_query(query_one_ans)

    print query_two
    get_query(query_two_ans)

    print query_three
    get_query(query_three_ans)
