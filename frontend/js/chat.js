const API_URL = 'http://localhost:8000';

const email = document.getElementById('email');
const password = document.getElementById('password');
const loginBtn = document.getElementById('login-btn');
const registerBtn = document.getElementById('register-btn');
const authSection = document.getElementById('auth-section');
const chatSection = document.getElementById('chat-section');
const chatBox = document.getElementById('chat-box');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const clearBtn = document.getElementById('clear-btn');
const typing = document.getElementById('typing');

let accessToken = localStorage.getItem('token');
let sessionId = localStorage.getItem('session');

if (accessToken && sessionId) {
    showChat();
}

function showChat() {
    authSection.style.display = 'none';
    chatSection.style.display = 'block';
}

loginBtn.onclick = async () => {
    const res = await fetch(`${API_URL}/chat/session`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email: email.value, password: password.value})
    });
    if (res.ok) {
        const data = await res.json();
        accessToken = data.access_token;
        localStorage.setItem('token', accessToken);
        await createSession();
    } else {
         const err = await res.json();
        alert('Ошибка входа: ' + (err.detail || 'Неверные данные'));
    }
};

registerBtn.onclick = async () => {
    const res = await fetch(`${API_URL}/auth/register`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email: email.value, password: password.value})
    });
    if (res.ok) {
        alert('Регистрация успешна! Теперь войдите.');
    } else {
        alert('Ошибка регистрации');
    }
};

async function createSession() {
    const res = await fetch(`${API_URL}/chat/session`, {
        method: 'POST',
        headers: {'Authorization': `Bearer ${accessToken}`}
    });
    if (res.ok) {
        const data = await res.json();
        sessionId = data.id;
        localStorage.setItem('session', sessionId);
        showChat();
    }
}

function appendMessage(sender, text) {
    const el = document.createElement('div');
    el.className = `message ${sender}`;
    el.textContent = text;
    chatBox.appendChild(el);
    chatBox.scrollTop = chatBox.scrollHeight;
}

sendBtn.onclick = sendMessage;
messageInput.onkeypress = (e) => { if (e.key === 'Enter') sendMessage(); };

async function sendMessage() {
    const text = messageInput.value.trim();
    if (!text) return;
    messageInput.value = '';
    messageInput.disabled = true;
    sendBtn.disabled = true;
    typing.style.display = 'block';
    appendMessage('user', text);
    const res = await fetch(`${API_URL}/chat/message?session_id=${sessionId}`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${accessToken}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text})
    });
    const data = await res.json();
    appendMessage('bot', res.ok ? data.bot_response : 'Ошибка');
    messageInput.disabled = false;
    sendBtn.disabled = false;
    typing.style.display = 'none';
}

clearBtn.onclick = () => { chatBox.innerHTML = ''; };