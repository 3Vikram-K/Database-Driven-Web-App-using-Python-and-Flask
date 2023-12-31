from sqlalchemy import create_engine, text, insert


engine = create_engine("mysql+pymysql://root:Aug$2023$$$@localhost:3306/vykramCareers?charset=utf8mb4")

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        jobs = []
        for row in result:
            jobs.append(row._asdict())
        return jobs
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))

        jobs = []
        for row in result:
            jobs.append(row._asdict())
        
        if len(jobs) == 0:
            return None
        else:
            return jobs[0]
        
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

        conn.execute(query,dict( 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url']))
        conn.commit()


    