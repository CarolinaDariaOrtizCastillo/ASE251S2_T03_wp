const sendBtn = document.getElementById("sendBtn");
const userInput = document.getElementById("userInput");
const chatMessages = document.getElementById("chatMessages");

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") sendMessage();
});

function sendMessage() {
  const text = userInput.value.trim();
  if (text === "") return;

  appendMessage("user", text);
  userInput.value = "";

  // Simulación de respuesta
  setTimeout(() => {
    let response = "No entendí muy bien eso 😅, ¿podrías explicarme mejor?";
    const msg = text.toLowerCase();

    if (msg.includes("hola")) {
      response = "¡Hola! 😊 ¿Qué te gustaría saber hoy?";
    } else if (msg.includes("precio")) {
      response = "¿Podrías especificarme el producto del que quieres saber el precio?";
    } else if (msg.includes("producto")) {
      response = "Claro, dime qué producto te interesa y te cuento más.";
    }

    appendMessage("bot", response);
  }, 600);
}

function appendMessage(sender, text) {
  const msgDiv = document.createElement("div");
  msgDiv.textContent = text;
  msgDiv.className =
    sender === "user"
      ? "bg-blue-900 text-white rounded-lg px-3 py-2 ml-auto max-w-[75%]"
      : "bg-gray-200 text-gray-800 rounded-lg px-3 py-2 max-w-[75%]";
  chatMessages.appendChild(msgDiv);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
