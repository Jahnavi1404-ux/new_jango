pip install dj-database-url
import dj-database-url
import os
DATABASES = {
 "default": dj_database_url.parse(os.environ.get("postgresql://test_db_u5jn_user:Fd6sgz5JvdJn7jIlCcZYPFN9PHj3k73j@dpg-d0epehc9c44c738a742g-a.oregon-postgres.render.com/test_db_u5jn"))
}
