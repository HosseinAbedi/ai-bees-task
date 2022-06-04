import sys
import connexion
sys.path.insert(1, 'src')

app = connexion.App(__name__, specification_dir='conf')
app.testing = False
app.add_api('comment_gen.yml')


