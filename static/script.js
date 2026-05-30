document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');
    const topicInput = document.getElementById('topic-input');
    const chatContainer = document.getElementById('chat-container');
    const loadingOverlay = document.getElementById('loading-overlay');
    
    startBtn.addEventListener('click', async () => {
        const topic = topicInput.value.trim();
        
        if (!topic) {
            alert('Please enter a business topic to discuss.');
            return;
        }

        // Reset UI
        chatContainer.innerHTML = '';
        chatContainer.classList.add('hidden');
        loadingOverlay.classList.remove('hidden');
        startBtn.disabled = true;

        try {
            const response = await fetch('/simulate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topic }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Meeting simulation failed');
            }

            const data = await response.json();
            chatContainer.classList.remove('hidden');
            displayChat(data.chat_history);
        } catch (error) {
            console.error('Error:', error);
            chatContainer.innerHTML = `
                <div class="error-message">
                    <i class="fas fa-exclamation-triangle"></i>
                    <p>Executive Error: ${error.message}</p>
                </div>
            `;
        } finally {
            loadingOverlay.classList.add('hidden');
            startBtn.disabled = false;
        }
    });

    function displayChat(history) {
        if (!history || history.length === 0) {
            chatContainer.innerHTML = '<p class="text-muted">No discussion recorded.</p>';
            return;
        }

        history.forEach((msg, index) => {
            setTimeout(() => {
                appendMessage(msg);
                // Scroll to bottom
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }, index * 400); // Staggered appearance for meeting feel
        });
    }

    function appendMessage(msg) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message';
        messageDiv.setAttribute('data-role', msg.role);
        
        messageDiv.innerHTML = `
            <div class="message-header">
                <i class="fas fa-user-tie"></i>
                <span>${msg.role}</span>
            </div>
            <div class="message-content">
                ${marked.parse(msg.message)}
            </div>
        `;
        
        chatContainer.appendChild(messageDiv);
    }
});
