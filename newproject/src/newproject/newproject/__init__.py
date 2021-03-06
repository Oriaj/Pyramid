# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from resources import Root
import views
import pyramid_jinja2
import os
here = os.path.dirname(os.path.abspath(__file__))
settings = {}
settings['mako.directories'] = os.path.join(here, 'templates')

__here__ = os.path.dirname(os.path.abspath(__file__))

	
def make_app():
    """ This function returns a Pyramid WSGI application.
    """
   # config = Configurator(root_factory=Root)
    settings = {}
    settings['mako.directories'] = os.path.join(__here__, 'templates')
    config = Configurator( root_factory=Root, settings=settings )
    config.add_renderer('.jinja2', pyramid_jinja2.Jinja2Renderer)
    #config.add_view(views.my_view,
                   # context=Root,
                    #renderer='mytemplate.jinja2')
    config.add_route( "home", "/home" )
    config.add_view( views.home_view, route_name="home", renderer="zodiac.mako" )
    config.add_route( "resultat", "/resultat" )
    config.add_view( views.home_view, route_name="resultat", renderer="resultat.mako" )
    
    config.add_static_view(name='static',
                           path=os.path.join(__here__, 'static'))
    return config.make_wsgi_app()

application = make_app()
