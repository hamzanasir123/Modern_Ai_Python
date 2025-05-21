from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def main():
    print("Hello from hello-uv!")
    uvicorn.run(app, host="0,0.0.0", port=8000)


if __name__ == "__main__":
    main()
