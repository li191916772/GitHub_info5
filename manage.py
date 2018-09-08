from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

app = create_app("development")

# 管理启动
manager = Manager(app)
# 数据库迁移
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route("/")
def index():

    return "index"

if __name__ == "__main__":
    manager.run()