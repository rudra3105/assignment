document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData();
    const file = document.getElementById('file').files[0];
    formData.append('file', file);

    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    if (response.ok) {
        document.getElementById('filepath').value = result.filepath;
        alert('File uploaded successfully');
    } else {
        alert(`Error: ${result.error}`);
    }
});

document.getElementById('processForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData();
    const data = document.getElementById('data').value;
    const filepath = document.getElementById('filepath').value;

    formData.append('data', data);
    formData.append('filepath', filepath);

    const response = await fetch('/process_image', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    if (response.ok) {
        const link = document.createElement('a');
        link.href = `/download/${result.output_path.split('/').pop()}`;
        link.textContent = 'Download Processed File';
        document.getElementById('result').appendChild(link);
    } else {
        alert(`Error: ${result.error}`);
    }
});
