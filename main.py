from langcorn import create_service
import uvicorn
app = create_service(
    "summarize_chain:chain"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)