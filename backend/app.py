from flask import Flask
from routes.dataset_routes import bp as dataset_bp
from routes.quality_log_routes import quality_bp
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

app.register_blueprint(dataset_bp)
app.register_blueprint(quality_bp)

@app.route("/sample", methods=["GET"])
def sample_route():
    return {"message": "API Health Check Successful!"}, 200
if __name__ == "__main__":
    app.run(debug=True)
