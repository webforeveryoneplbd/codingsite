from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '529568532924bcf0434e429f8bd2483648880216e40edb3'  # Clé secrète pour la gestion des sessions


# Route vers la page d'accueil
@app.route('/')
def index():
    return render_template('page1_coding.html')


# Route pour le traitement de la connexion
@app.route('page2_coding.html', methods=['POST'])
def login():
    # Récupérer les informations du formulaire de connexion
    Id = request.form['id']
    password = request.form['password']

    # Vérifier les informations d'identification
    if verify_credentials(Id, password):
        # Si les informations d'identification sont valides, définir une session
        session['Id'] = Id
        return redirect('page2_coding.html')
    else:
        # Sinon, rediriger vers la page de connexion avec un message d'erreur
        return render_template('page1_coding.html', error='Identifiants incorrects')


# Route pour afficher le profil de l'utilisateur
@app.route('page2_coding.html')
def profile():
    # Vérifier si l'utilisateur est connecté
    if 'Id' in session:
        # Charger les données du profil depuis le fichier texte ou autre source
        Id = session['Id']
        return render_template('page2_coding.html', Id=Id)
    else:
        # Si l'utilisateur n'est pas connecté, rediriger vers la page de connexion
        return redirect('page2_coding.html')


# Fonction pour vérifier les informations d'identification dans un fichier texte
def verify_credentials(Id, password):
    # Ouvrir le fichier texte contenant les informations d'identification
    with open('data_base.txt', 'r') as file:
        # Lire chaque ligne du fichier
        for line in file:
            # Séparer le nom d'utilisateur et le mot de passe de chaque ligne
            stored_Id, stored_password = line.strip().split(',')
            # Vérifier si les informations d'identification correspondent
            if Id == stored_Id and password == stored_password:
                return True
    # Si les informations d'identification ne correspondent pas, retourner False
    return False


if __name__ == '__main__':
    app.run(debug=True)

