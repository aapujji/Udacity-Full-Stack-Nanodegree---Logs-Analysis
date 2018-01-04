#!/usr/bin/env python2.7
import psycopg2

DBNAME = "news"

query_one = "What are the most popular three articles of all time?\n"
query_two = "Who are the most popular article authors of all time?\n"
query_three = "On which days did more than 1% of requests lead to errors?\n"

query_one_ans = ("SELECT title, count(*) FROM articles JOIN log "
                 "ON log.path LIKE concat('%',articles.slug,'%') "
                 "GROUP BY title, path ORDER BY count(*) DESC limit 3;")
query_two_ans = ("SELECT name, count(*) FROM authors JOIN articles ON "
                 "articles.author = authors.id JOIN log ON log.path "
                 "LIKE concat('%', articles.slug, '%') GROUP BY name,"
                 "log.path ORDER BY count(*) DESC limit 3;")
query_three_ans = ("SELECT date, perc FROM err_perc GROUP BY date,"
                   "perc HAVING perc >= 1 ORDER BY perc;")


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
