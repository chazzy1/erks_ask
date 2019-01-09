# -*- encoding:utf-8 -*-
from flask import Blueprint

bpapp = Blueprint('projectuser', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/static_projectuser')

# from ercc import db
# from ercc import logger
from . import models  # noqa
from . import views  # noqa
from . import signals  # noqa
