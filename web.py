from flask import Flask, render_template_string, request, redirect, url_for
from main import add_note, read_notes, get_latest_note, note_summary_prompt

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>AI Sticky Notes</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        :root {
            color-scheme: dark light;
            --bg: #181a1b;
            --fg: #f1f1f1;
            --accent: #2d8cf0;
            --note-bg: #23272a;
            --note-border: #2d8cf0;
        }
        @media (prefers-color-scheme: dark) {
            body { background: var(--bg); color: var(--fg); }
            .notes { background: var(--note-bg); color: var(--fg); border-left: 4px solid var(--note-border);}
            textarea, input, button { background: #222; color: #eee; border: 1px solid #444; }
        }
        @media (prefers-color-scheme: light) {
            body { background: #f9f9f9; color: #222; }
            .notes { background: #fff; color: #222; border-left: 4px solid var(--accent);}
            textarea, input, button { background: #fff; color: #222; border: 1px solid #bbb; }
        }
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 40px; }
        h1 { color: var(--accent); }
        textarea { width: 100%; height: 60px; margin-bottom: 10px; resize: vertical; }
        .notes { padding: 10px; margin-bottom: 20px; border-radius: 6px; }
        button {
            background: var(--accent);
            color: #fff;
            border: none;
            padding: 8px 18px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
            transition: background 0.2s;
        }
        button:hover { background: #1a73e8; }
        .container { max-width: 600px; margin: auto; }
        .footer { text-align: center; margin-top: 40px; font-size: 0.9em; color: #888; }
        @media (max-width: 700px) {
            body, .container { margin: 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI Sticky Notes</h1>
        <form method="post" action="/add">
            <textarea name="note" placeholder="Digite sua nota aqui..." required></textarea><br>
            <button type="submit">Adicionar Nota</button>
        </form>
        <h2>Nota mais recente</h2>
        <div class="notes">{{ latest|safe }}</div>
        <h2>Todas as notas</h2>
        <div class="notes" style="white-space: pre-line;">{{ notes|safe }}</div>
        <h2>Resumo das notas</h2>
        <div class="notes">{{ summary|safe }}</div>
        <div class="footer">Desenvolvido com Flask & MCP &mdash; <a href="https://github.com/" style="color:var(--accent);text-decoration:none;">GitHub</a></div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    notes = read_notes()
    latest = get_latest_note()
    summary = note_summary_prompt()
    return render_template_string(
        HTML,
        notes=notes.replace('\n', '<br>'),
        latest=latest,
        summary=summary
    )

@app.route("/add", methods=["POST"])
def add():
    note = request.form.get("note", "")
    if note.strip():
        add_note(note)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)