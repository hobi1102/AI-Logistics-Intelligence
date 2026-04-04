document.addEventListener('DOMContentLoaded', () => {

    // Freight Form Handler
    document.getElementById('freight-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const btn = e.target.querySelector('button');
        const originalText = btn.innerHTML;
        btn.innerHTML = 'Predicting...';
        btn.disabled = true;

        const dollars = document.getElementById('dollars').value;
        const modelType = document.getElementById('freight-algo').value;

        try {
            const response = await fetch('/api/predict/freight', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    Dollars: dollars,
                    model_type: modelType
                })
            });
            const data = await response.json();

            if (data.success) {
                const resultDiv = document.getElementById('freight-result');
                const resultValue = document.getElementById('freight-value');
                
                resultValue.textContent = data.message;
                
                // Reset animation
                resultDiv.style.animation = 'none';
                resultDiv.offsetHeight; /* trigger reflow */
                resultDiv.style.animation = null;
                
                resultDiv.style.display = 'flex';
            } else {
                alert('Error: ' + data.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred during prediction.');
        } finally {
            btn.innerHTML = originalText;
            btn.disabled = false;
        }
    });

    // Invoice Form Handler
    document.getElementById('invoice-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const btn = e.target.querySelector('button');
        const originalText = btn.innerHTML;
        btn.innerHTML = 'Analyzing...';
        btn.disabled = true;

        const payload = {
            invoice_quantity: document.getElementById('inv-qty').value,
            invoice_dollars: document.getElementById('inv-dollars').value,
            Freight: document.getElementById('freight').value,
            total_item_quantity: document.getElementById('total-qty').value,
            total_item_dollars: document.getElementById('total-dollars').value
        };

        try {
            const response = await fetch('/api/predict/invoice', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await response.json();

            if (data.success) {
                const resultDiv = document.getElementById('invoice-result');
                const resultValue = document.getElementById('invoice-value');
                const indicator = document.getElementById('risk-indicator');
                
                resultValue.textContent = data.message;
                
                indicator.className = 'status-indicator ' + (data.risk_flag === 1 ? 'risk' : 'safe');
                resultValue.className = 'value ' + (data.risk_flag === 1 ? 'risk-text' : 'safe-text');
                
                // Reset animation
                resultDiv.style.animation = 'none';
                resultDiv.offsetHeight;
                resultDiv.style.animation = null;
                
                resultDiv.style.display = 'flex';
            } else {
                alert('Error: ' + data.error);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred during analysis.');
        } finally {
            btn.innerHTML = originalText;
            btn.disabled = false;
        }
    });

});
