from flask import (
	render_template
)
import connexion

## app instance
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def home():
	return render_template('./templates/home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)