from contextlib import asynccontextmanager
import subprocess

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager for FastAPI app. It will run all code before `yield`
    on app startup, and will run code after `yeld` on app shutdown.
    """

    try:
        subprocess.run(["tailwindcss", "-i", "app/static/src/input.css", "-o", "app/static/css/output.css", "--minify"])
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield
