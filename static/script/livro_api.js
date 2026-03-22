async function buscarDadosLivro() {
    const query = document.getElementById('input_busca').value.trim();
    if (!query) return alert("Digite o título!");

    const url = `https://openlibrary.org/search.json?title=${encodeURIComponent(query)}`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.docs && data.docs.length > 0) {
            const livro = data.docs[0];

            document.getElementById('titulo').value = livro.title || "";
            document.getElementById('autor').value = livro.author_name 
                ? livro.author_name.join(', ') 
                : "Desconhecido";

            document.getElementById('descricao').value =
                `Publicado em: ${livro.first_publish_year || 'N/A'}`;

            if (livro.cover_i) {
                const capaUrl = `https://covers.openlibrary.org/b/id/${livro.cover_i}-L.jpg`;
                document.getElementById('capa_url').value = capaUrl;
                document.getElementById('preview_capa').src = capaUrl;
                document.getElementById('preview_capa').style.display = 'block';
            }

            alert("Livro encontrado!");
        } else {
            alert("Nenhum resultado encontrado.");
        }

    } catch (error) {
        console.error("Erro:", error);
        alert("Erro de conexão com a API.");
    }
}