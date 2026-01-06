from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sentiment Tester</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 700px;
                margin: 40px auto;
            }
            textarea {
                width: 100%;
                height: 120px;
            }
            button {
                margin-top: 10px;
                padding: 8px 16px;
            }
            pre {
                background: #f4f4f4;
                padding: 10px;
            }
        </style>
    </head>
    <body>
        <h2>Sentiment Analysis Tester</h2>
        <textarea id="text" placeholder="Enter text here..."></textarea>
        <br />
        <button onclick="analyze()">Analyze</button>

        <h3>Result</h3>
        <pre id="result">Waiting...</pre>

        <script>
            const apiKey = localStorage.getItem("apiKey");
            console.log("api key", apiKey)

            if (!apiKey) {
                window.location.href = "/";
            }
            async function analyze() {
                const text = document.getElementById("text").value;

                const response = await fetch("/sentiment/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-API-Key": apiKey
                    },
                    body: JSON.stringify({ text })
                });

                const data = await response.json();
                document.getElementById("result").textContent =
                    JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """