from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def login():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Login</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 500px;
                margin: 60px auto;
            }
            input {
                width: 100%;
                padding: 8px;
                font-size: 16px;
            }
            button {
                margin-top: 10px;
                padding: 8px 16px;
            }
            .error {
                color: red;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <h2>Enter API Key</h2>
        <input id="apiKey" placeholder="X-API-Key" />
        <button onclick="login()">Login</button>

        <div class="error" id="error"></div>

        <script>
            async function login() {
                const key = document.getElementById("apiKey").value;
                const errorDiv = document.getElementById("error");
                errorDiv.textContent = "";

                const response = await fetch("/auth/validate", {
                    headers: {
                        "X-API-Key": key
                    }
                });

                if (!response.ok) {
                    errorDiv.textContent = "Invalid API key";
                    return;
                }

                const data = await response.json();

                // Store key locally
                localStorage.setItem("apiKey", key);
                localStorage.setItem("userTier", data.tier);

                // Redirect to app
                window.location.href = "/ui";
            }
        </script>
    </body>
    </html>
    """