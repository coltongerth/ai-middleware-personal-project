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
        <textarea id="text" placeholder="Enter text here..." oninput="updateCount()"></textarea>
        <div id="counter"></div>
        <br />
        <button onclick="analyze()">Analyze</button>

        <h3>Result</h3>
        <pre id="result">Waiting...</pre>

        <script>
            const apiKey = localStorage.getItem("apiKey");
            


            if (!apiKey) {
                window.location.href = "/";
            }


            const tier = localStorage.getItem("userTier");

            const MAX_CHARS = tier === "premium" ? 100 : 20;

            function updateCount() {
                const textarea = document.getElementById("text");
                const counter = document.getElementById("counter");

                if (textarea.value.length > MAX_CHARS) {
                    textarea.value = textarea.value.slice(0, MAX_CHARS);
                }

                counter.textContent =
                    `${textarea.value.length} / ${MAX_CHARS} characters (${tier})`;
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