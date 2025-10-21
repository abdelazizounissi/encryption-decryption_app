async function processText() {
    const text = document.getElementById("inputText").value;
    const cipher = document.getElementById("cipherType").value;
    const action = document.getElementById("actionType").value;
    const key = document.getElementById("keyInput").value || 3;

    const response = await fetch("/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cipher, action, text, key })
    });

    const data = await response.json();
    document.getElementById("outputText").textContent = data.result;
}
