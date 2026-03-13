from . import default, start, greet, give_prophecy, close_menu

all_handlers_routes = [
    start.router,
    greet.router,
    give_prophecy.router,
    close_menu.router,
    default.router
]
