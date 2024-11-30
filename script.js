document.getElementById("data-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = {
        region: document.getElementById("region").value,
        district: document.getElementById("district").value,
        species: document.getElementById("species").value,
        disease: document.getElementById("disease").value,
        vaccination: document.getElementById("vaccination").value,
    };

    const response = await fetch("/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
    });

    const result = await response.json();
    const messageDiv = document.getElementById("message");

    if (result.success) {
        messageDiv.textContent = "Data submitted successfully!";
        messageDiv.style.color = "green";
    } else {
        messageDiv.textContent = "Error submitting data.";
        messageDiv.style.color = "red";
    }
});
