import json
from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


app = Flask(__name__, static_folder=Path.cwd() / 'static', static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/clustering', methods=['POST'])
def clustering():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    target = data['target']
    head = data['record']['head']
    body = data['record']['body']
    df = pd.DataFrame(body, columns=head)
    result = append_kmeans_pca(df, target)
    return jsonify({
        'type': 'success',
        'payload': {
            'head': result.columns.tolist(),
            'body': result.values.tolist()
        }
    })


def append_kmeans_pca(df, target_column, num_clusters=5):
    # num_seeds = 5
    max_iterations = 300
    pca_num_components = 2
    vectorizer = TfidfVectorizer()
    vecs = vectorizer.fit_transform(df[target_column])
    model = KMeans(
        n_clusters=num_clusters,
        max_iter=max_iterations,
        precompute_distances='auto',
        n_jobs=-1
    )

    clusters = model.fit_predict(vecs)
    X = vecs.todense()
    reduced = PCA(n_components=pca_num_components).fit_transform(X)
    reduced_df = pd.DataFrame(reduced)
    reduced_df['cluster'] = clusters
    concat = pd.concat([df, reduced_df], axis=1)

    return concat


def main():
    app.debug = True
    app.use_reloader = True
    app.run(host='0.0.0.0', port=5000, threaded=True)


if __name__ == '__main__':
    main()
