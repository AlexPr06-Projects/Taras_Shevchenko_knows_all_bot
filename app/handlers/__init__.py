from . import start, greet, give_prophecy, close_menu, echo

all_handlers_routes = [
    start.router,
    greet.router,
    give_prophecy.router,
    close_menu.router,
    echo.router
]
