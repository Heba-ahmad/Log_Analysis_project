#!/usr/bin/env python

# a reporting tool that prints out reports, using the psycopg2 module

import psycopg2

DBName = "news"


def main():
    # create a connection to the given database news
    conn = psycopg2.connect(database=DBName)
    # create a cursor....
    c = conn.cursor()
    # Q1 Answer: the most popular three articles of all time as sql code
    top_three_arti = """ SELECT * FROM top_articles_views
     LIMIT 3;
     """
    c.execute(top_three_arti)
    result = c.fetchall()
    print("\n1. The most popular three articles of all time:\n")
    for (title, views) in result:
        print("      {} - {} Views".format(title, views))

    # Q2 Answer: the popular article authors of all time as sql code
    top_arti_auth = """
        SELECT authors.name,
        COUNT(*) AS top_authors
        FROM articles JOIN authors ON authors.id =
        articles.author JOIN log ON path LIKE concat(
        '/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY top_authors DESC;"""
    c.execute(top_arti_auth)
    result = c.fetchall()
    print("\n2. The most popular article authors of all time:\n")
    for (name, top_authors) in result:
        print("      {} - {} Views".format(name, top_authors))

    # Q3 the days that have more than 1% of requests lead to errors
    errors_pescent = """
    SELECT * FROM percentage_errors WHERE percentage > 1
    ORDER BY percentage_errors.percentage DESC;
    """
    c.execute(errors_pescent)
    result = c.fetchall()
    print("\n3. Days that have more than 1% of requests lead to errors:\n")
    for (date, percentage) in result:
        print("      {} - {}% Errors".format(date, percentage))
    # exit connection with the database
    c.close()
    conn.close()


if __name__ == "__main__":
    main()
