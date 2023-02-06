# Projet Data & IoT

## L'équipe
- [@Lawberryy](https://github.com/Lawberryy)
- [@Sarayeo](https://github.com/Sarayeo)

## Description
Dans ce projet, on utilise [l'API Météo](https://api.meteo-concept.com/documentation) de Météo Concept afin de récupérer la température maximale de la journée dans une ville spécifique (dans notre cas, nous avons choisi Nanterre). Cette valeur nous allons la stocker et la comparer à une autre température prédéfinie. Les 2 LEDs présentent dans notre schéma réagiront differemment au clic sur le bouton (l'une s'allumera, l'autre pas), en fonction de si la température maximale de la journée dépasse ou non l'autre température prédéfinie dans le code.

Nous avons 2 versions de ce projet :
- Une première qui utilise un serveur local sur lequel on stock en brut les données météo de la journée récupérées avec l'API, elles n'évoluent donc plus d'une journée à l'autre.
- Une seconde un peu plus intéressante qui utilise directement l'API (et donc son serveur) afin que la température maximale se renouvelle chaque jour, et donc le projet aussi.

Une vidéo de chaque version est disponible.

## Démarrer avec le projet

Avant toute chose, vous devez installer ce qui suit sur votre machine :
- Node.js (v19.4)

### Les Dépendances
- Express.js
- bodyParser
- ip
- path

## Comment installer le projet

- Pour commencer, clonez le repository sur votre machine locale avec cette commande :
```shell
$ git clone git@github.com:Lawberryy/data-iot-project.git
```
ou tout autre manière que vous préférez.
- Une fois cela fait, allez dans le dossier "API_server" et installez toutes les dépendances listées juste au dessus avec cette commande npm :
```shell
$ npm install
```
- Ensuite, pour démarrer le serveur (afin d'utiliser la première version du projet), entrez la commande suivante :
```shell
$ npm run start
```
