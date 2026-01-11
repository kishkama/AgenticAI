import uvicorn
import os
from google.adk.cli.fast_api import get_fast_api_app

DEBUG_MODE = os.environ.get("DEBUG", "false").lower() == "true"

if __name__ == "__main__":
    agents_dir = os.path.dirname(os.path.abspath(__file__))
    app = get_fast_api_app(
        agents_dir=agents_dir,
        web=True,
        host="0.0.0.0",
        port=8000,
        reload_agents=not DEBUG_MODE,  # Disable reload when debugging
    )
    print(f"server is listening on port 8000 (debug={DEBUG_MODE})")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug" if DEBUG_MODE else "info")