import newspaper
from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import nltk
import os

# Set the NLTK data path to the included nltk_data directory
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')
nltk.data.path.append(nltk_data_dir)

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize_article():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        article.nlp()

        img_url = article.top_image
        title = article.title
        full_text = article.text.replace('Advertisement', '')
        summary = article.summary.replace('Advertisement', '')

        return jsonify({
            'img_url': img_url,
            'title': title,
            'full_text': full_text,
            'summary': summary
        })

    except newspaper.ArticleException as e:
        return jsonify({'error': 'Failed to process article', 'details': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e), 'traceback': traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(debug=True)
