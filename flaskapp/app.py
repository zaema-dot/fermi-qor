from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from createDB import Job, MainStats, RuntimeAnalysis, GeometricAnalysis, StatisticalAnalysis, setup_database  # import your models

app = Flask(__name__)

# Setup the database connection
engine = create_engine('mysql+pymysql://d2s:d2s_1234@db/emumbaqor')
Session = sessionmaker(bind=engine)

@app.route("/", methods=["GET", "POST"])
def index():
    session = Session()
    results = None
    stats_type = None

    if request.method == "POST":
        query_type = request.form["query_type"]
        query_value = request.form["query_value"]
        stats_type = request.form["stats_type"]

        query = None
        if query_type == "job_id":
            query = session.query(Job).filter(Job.fermi_job_id == query_value).first()
        elif query_type == "job_name":
            query = session.query(Job).filter(Job.job_name == query_value).first()
        elif query_type == "user_id":
            query = session.query(Job).filter(Job.user_id == query_value).first()

        if query:
            results = {
                "main_stats": session.query(MainStats).filter(MainStats.job_id == query.id).all() if stats_type in ["all", "main"] else None,
                "runtime_analysis": session.query(RuntimeAnalysis).filter(RuntimeAnalysis.job_id == query.id).all() if stats_type in ["all", "runtime"] else None,
                "geometric_analysis": session.query(GeometricAnalysis).filter(GeometricAnalysis.job_id == query.id).all() if stats_type in ["all", "geometric"] else None,
                "statistical_analysis": session.query(StatisticalAnalysis).filter(StatisticalAnalysis.job_id == query.id).all() if stats_type in ["all", "statistical"] else None
            }

    return render_template("index.html", results=results, stats_type=stats_type)


if __name__ == "__main__":
    app.run(debug=True)
