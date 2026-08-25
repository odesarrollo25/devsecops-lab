from fastapi import FastAPI


app = FastAPI(title="DevSecOps Task API")


@app.get("/")
def root():
    return {
        "name": "DevSecOps Task API",
        "version": "0.2.0",
        "status": "running",
    }
