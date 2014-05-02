from flask import Flask

app = Flask(__name__)

db.posts.ensure_index([
      ('body', 'text'),
      ('title', 'text'),
  ],
  name="search_index",
  weights={
      'title':100,
      'body':25
  }
)

@app.route('/search')
def search():
    query = request.form['q']
    text_results = db.command('text', 'posts', search=query, limit=SEARCH_LIMIT)
    doc_matches = (res['obj'] for res in text_results['results'])
    return render_template("search.html", results=results)