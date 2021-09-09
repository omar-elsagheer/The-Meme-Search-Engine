

from flask import Flask, render_template, request, jsonify
import sqlite3
from image_search.feature_extractor import FeatureExtractor
from image_search.retrieve_images import get_images
from inverted_index.documents_and_text import save_file
from ranking.scoring_corpus import tf_idf_query
from autocomplete.auto_complete import auto_complete
from relevance_feedback.rochio import rochio_algorithm
from spelling_correction.spell_check import check_spelling

app = Flask(__name__)
conn = sqlite3.connect('RF.db')


def add_to_db(params):
    try:
        with sqlite3.connect("RF.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO queries (query, image)VALUES(?, ?)", params)
            con.commit()
            msg = "Record successfully added"
            print(msg)
    except:
        con.rollback()
        msg = "error in insert operation"
        print(msg)


def get_from_db(params):
    try:
        with sqlite3.connect("RF.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * from queries where query = \"" + params + "\"")
            rows = cur.fetchall()
            images_names = [params]
            for row in rows:
                images_names.append(row[1])
            return images_names
    except:
        return []


@app.route('/', methods=['POST', 'GET'])
def index():
    # Ihab's reservation

    ajax = request.get_json()
    if ajax is not None:
        if 'query' in ajax:
            query = ajax.get('query')
            autos = auto_complete(words, query)
            return jsonify({
                "a": autos,
            })
        else:
            image_name = ajax.get('imgName')[:-4]
            txt_query = ajax.get('txtQuery')
            print(txt_query, image_name)
            params = (txt_query, image_name)
            add_to_db(params)
    if request.method == 'POST' and 'query' in request.form:
        text_query = request.form['query'].strip(' ')
        alt_query = check_spelling(all_terms, text_query)
        if alt_query == text_query:
            alt_query = ''
        images_names = get_from_db(text_query)
        if len(images_names) > 1:
            qm = rochio_algorithm(images_names)
            images = tf_idf_query(qm, tf_idf, image_names)
        else:
            images = tf_idf_query(text_query, tf_idf, image_names)
        return render_template('index.html', text_query=text_query, images=images, alt_query=alt_query)
    elif request.method == 'POST' and 'image' in request.form:
        image_query = request.form['image']
        images = get_images(fe, image_query)
        return render_template('index.html', image_query=image_query, images=images)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # for ranking
    tf_idf = save_file('l', 'sorted_tf_idf')
    image_names = save_file('l', 'image_names')
    # for spell checking
    all_terms = save_file('l', 'all_terms')
    # Image Search
    fe = FeatureExtractor()
    # Auto complete
    words = save_file('l', 'words')
    app.run(debug=True)
