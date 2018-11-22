from app import create_app
from utils import FlaskCelery
import settings


app = create_app()
celery = FlaskCelery('tasks', broker=settings.CELERY_BROKER_URL)
celery.conf.update(app.config)
app.app_context().push()
