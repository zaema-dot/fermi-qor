from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createDB import Job, MainStats, RuntimeAnalysis, GeometricAnalysis, StatisticalAnalysis  # Assuming createDB.py has models

app = Flask(__name__)

# Configure the database connection
DATABASE_URI = 'mysql+pymysql://d2s:d2s_1234@localhost/emumbaqor'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        job_id = request.form.get('job_id')
        job_name = request.form.get('job_name')

        session = Session()

        if not user_name and not job_id and not job_name:
            return render_template('index.html', error="Please enter at least one search criterion.")

        query = session.query(Job).outerjoin(MainStats).outerjoin(RuntimeAnalysis).outerjoin(GeometricAnalysis).outerjoin(StatisticalAnalysis)

        if job_id:
            query = query.filter(Job.fermi_job_id == job_id)
        if job_name:
            query = query.filter(Job.job_name == job_name)
        if user_name:
            query = query.filter(Job.user_id == user_name)

        job = query.first()

        if not job:
            return render_template('index.html', error="No job found for the provided parameters.")

        response = {
            "job_name": job.job_name,
            "fermi_job_id": job.fermi_job_id,
            "user_id": job.user_id,
            "main_stats": [{stat.property: stat.value} for stat in job.main_stats],
            "runtime_analysis": [{stat.property: stat.value} for stat in job.runtime_analysis],
            "geometric_analysis": [{stat.property: stat.value} for stat in job.geometric_analysis],
            "statistical_analysis": [{
                "set_id": stat.set_id,
                "properties": {stat.property: stat.value}
            } for stat in job.statistical_analysis]
        }

        return render_template('index.html', result=response)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
