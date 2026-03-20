const searchInput = document.getElementById("search");
const notesDiv = document.getElementById("notes");

searchInput.addEventListener("keyup", async () => {
    const query = searchInput.value;

    const res = await fetch(`/search?q=${query}`);
    const notes = await res.json();

    notesDiv.innerHTML = "";

    notes.forEach(note => {
        const highlighted = note.content.replace(
            new RegExp(query, "gi"),
            match => `<mark>${match}</mark>`
        );

        notesDiv.innerHTML += `
            <div class="note">
                <h3>${note.title}</h3>
                <p>${highlighted}</p>
                <span class="tag">${note.tag}</span>
                <small>${note.created_at}</small><br>
                <a href="/edit/${note.id}">✏️ Edit</a>
                <a href="/delete/${note.id}">❌ Delete</a>
            </div>
        `;
    });
});

function filterTag(tag) {
    const notes = document.querySelectorAll(".note");

    notes.forEach(note => {
        const noteTag = note.querySelector(".tag").innerText;

        if (tag === "All" || noteTag === tag) {
            note.style.display = "block";
        } else {
            note.style.display = "none";
        }
    });
}