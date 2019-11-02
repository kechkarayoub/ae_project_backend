
try:
    with open("app/server_settings.json") as server_conf_file:
        import pymysql
        pymysql.install_as_MySQLdb()
except:
    pass