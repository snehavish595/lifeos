from fastapi import FastAPI

app = FastAPI(
    title="LifeOS API",
    description="Backend for LifeOS, your personal life operating system.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to LifeOS API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}