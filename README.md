# Description des classes

## Utilisation Simple
Lancer le script simulation_gui.py et cliquer sur 1gen:
1. Un generation de NN est generee.
2. Chaque NN element (individu) de la generation est activé avec en input la position en y de la voiture,
	générant ainsi la commande a donner a la voiture en boucle
3. La voiture se déplace jusqu'a la collision ou apres 10s de simulation
4. Le score est calcule en fonction de la distance en Y a la fin de la simulation (et imprime dans le terminal)
5. Puis on passe a l'element suivant de la generation ou a la generation suivante (voir log dans le terminal)
6. La simulation continue sans s'arreter. Pour l'arreter appuyer sur Stop.

## Comprehension des classes

Liste des classes utiles:

### Dubins Car:
Cette classe simule une voiture de Dubins (vitesse constante) simplement à l'aide d'une simulation d'euler.
La voiture de Dubins prend uniquement la commande angulaire en entrée.

### Environment
L'environnement ou va se déplacer la voiture de Dubins.
Elle permet de la simuler:
- la voiture de Dubins
- les collisions avec les murs
- calculer (comme un capeur laser) la distance jusqu'a l'obstacle en face
Ici les obstacles sont uniquements les limites du rectangle definissant l'environnement

L'environnement prends en parametres les dimensions de l'environnement, le pas de temps et le regulateur

### Regulateur
Un régulateur est un objet qui génére des commandes pour la voiture de Dubins (par exemple)
Par défaut un environnement possede un regulateur aléatoire

### AI_regulator
Une classe derivee de Regulateur. C'est celle qui va generer les commandes en activant le NN
Elle est plutot bien commentee


[NN]: 'Neural_Network'
