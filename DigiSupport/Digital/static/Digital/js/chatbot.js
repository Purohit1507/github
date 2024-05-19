document.addEventListener('DOMContentLoaded', function () {
    const openChatbotBtn = document.getElementById('open-chatbot');
    const closeChatbotBtn = document.getElementById('close-chatbot');
    const chatbotContainer = document.getElementById('chatbot');
    const chatbotInput = document.getElementById('chatbot-input');
    const sendChatbotBtn = document.getElementById('send-chatbot');
    const chatbotMessages = document.getElementById('chatbot-messages');

    openChatbotBtn.addEventListener('click', function () {
        chatbotContainer.style.display = 'flex';
        openChatbotBtn.style.display = 'none';
    });

    closeChatbotBtn.addEventListener('click', function () {
        chatbotContainer.style.display = 'none';
        openChatbotBtn.style.display = 'block';
    });

    function sendMessage() {
        const userMessage = chatbotInput.value;
        if (userMessage.trim() === '') return;

        const userMessageElement = document.createElement('div');
        userMessageElement.textContent = userMessage;
        userMessageElement.classList.add('user-message');
        chatbotMessages.appendChild(userMessageElement);

        // Placeholder for chatbot response logic
        const botResponseElement = document.createElement('div');
        botResponseElement.textContent = 'You Will get all answer Soon, We are Updating.';
        botResponseElement.classList.add('bot-message');
        chatbotMessages.appendChild(botResponseElement);

        // AJAX call to save chat log
        fetch('/save-chat-log/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Helper function to get CSRF token
            },
            body: JSON.stringify({
                'message': userMessage,
                'response': 'You Will get all answer Soon, We are Updating.'
            })
        });

        chatbotInput.value = '';
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }

    sendChatbotBtn.addEventListener('click', sendMessage);

    // Listen for Enter key press to send message
    chatbotInput.addEventListener('keypress', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage();
        }
    });
});

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
