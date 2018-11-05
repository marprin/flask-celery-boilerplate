from app import create_app
from utils import celery


app = create_app()
app.app_context().push()
