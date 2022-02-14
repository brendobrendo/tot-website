from flask_app import app
from flask_app.controllers import routes, routes_meetings, routes_role_assignments, routes_poasts, routes_members, routes_officers, routes_role_confirmations, routes_emails

if __name__ == "__main__":
    app.run(debug=True)

