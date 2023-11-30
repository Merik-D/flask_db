from flask import Flask

from mydb.auth.route.error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from mydb.auth.route.all.user_route import user_bp
    from mydb.auth.route.all.airline_route import airline_bp
    from mydb.auth.route.all.airport_route import airport_bp
    from mydb.auth.route.all.ticket_purchase_history_route import ticket_purchase_history_bp
    from mydb.auth.route.all.ticket_route import ticket_bp
    from mydb.auth.route.all.flight_route import flight_bp
    from mydb.auth.route.all.baggage_allowance_route import baggage_bp
    from mydb.auth.route.all.connected_flight_route import connected_flight_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(airline_bp)
    app.register_blueprint(airport_bp)
    app.register_blueprint(ticket_purchase_history_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(flight_bp)
    app.register_blueprint(baggage_bp)
    app.register_blueprint(connected_flight_bp)
    # app.register_blueprint(airport)
    # app.register_blueprint(airline_airport)