
from flask import Flask

app = Flask(__name__)


from seo import routes  # noqa
