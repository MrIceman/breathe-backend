from flask import Blueprint

from extensions import database_manager, crypto
from profile.controller import ProfileController

profile_blueprint = Blueprint('profile', __name__, url_prefix='/profile')
controller = ProfileController(database_manager=database_manager, crypto=crypto, array_parser=array_parser)
from .view import *
