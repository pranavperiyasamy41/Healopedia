async function getMedInfo() {
    // 1. Correct IDs to match your professional HTML structure
    const medInput = document.getElementById('medSearch'); 
    const med = medInput.value.trim();
    const btn = document.getElementById('btn'); 
    const resultArea = document.getElementById('resultBox'); 
    const answerText = document.getElementById('answerText');

    if (!med) {
        alert("Please enter a medicine name.");
        return;
    }

    // 2. UI Feedback: Clinical Loading State
    btn.innerText = "Consulting AI...";
    btn.disabled = true;
    resultArea.classList.add('hidden'); 

    try {
        // 3. API Call: Updated to match the backend route "/med-info"
        // Using encodeURIComponent is best practice for search terms with spaces
        const response = await fetch(`http://127.0.0.1:8000/med-info?medicine=${encodeURIComponent(med)}`);
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Medicine not found in FDA database.");
        }

        const data = await response.json();
        
        // 4. Update UI with AI Answer and the Source Snippet for credibility
        answerText.innerHTML = `
            <div style="color: #2dd4bf; margin-bottom: 10px; font-weight: bold;">AI Summary:</div>
            ${data.answer}
            <div style="margin-top: 20px; border-top: 1px solid #334155; padding-top: 10px;">
                <small style="color: #94a3b8;"><strong>FDA Label Context:</strong> ${data.source_snippet}</small>
            </div>
        `;
        
        resultArea.classList.remove('hidden');

    } catch (err) {
        console.error("Search Error:", err);
        alert(err.message || "Make sure the Python backend is running on port 8000!");
    } finally {
        btn.innerText = "Search";
        btn.disabled = false;
    }
}