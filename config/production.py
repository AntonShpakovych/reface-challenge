import dj_database_url

from .shared import *


DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("ELEPHANT_POSTGRESQL_URL"),
        conn_max_age=600
    )
}

MIDDLEWARE.insert(
    MIDDLEWARE.index(
        "django.middleware.security.SecurityMiddleware"
    ) + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware"
)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
