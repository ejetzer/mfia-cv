
# Mesures de courbes C-V avec le ZI MFIA

Prise de mesures automatisées dans le cadre du cours PHS8302 à Polytechnique
Montréal.

## Caractéristiques

- Connexion au MFIA
- Prise de mesure paramétrable
- Multi-plateforme

## Pré-requis

L'utilisation de ce programme requiert soit:

- L'installation préalable du serveur de données LabOne
	- via le centre de téléchargements de Zurich Instruments
	- via les programmes d'installation inclus sur le MFIA et accessibles via connexion USB sur Windows
	- ou via l'image disque incluse sous `lib/LabOne`
- Ou la vérification que le serveur embarqué sur le MFIA est à la version 26.1.2, ou plus
	généralement, à la même version que `zhinst-core`

## Usage/Examples

### Via LabOne

Si vous avez une installation locale du serveur LabOne, lancez le et naviguez au [localhost:8006](http://localhost:8006)
pour l'utiliser. Si votre MFIA est connecté à votre réseau local, vous devriez le voir dans la liste des appareils disponibles.
Double-cliquez pour ouvrir l'interface.

### Via 

```sh
pipenv run start
```

## Installation

Les pré-requis du programme sont décrits dans le `Pipfile`. Avant la première
exécution, installez les en créant l'environnement virtuel approprié:

```sh
git clone https://github.com/ejetzer/mfia-cv
cd mfia-cv
pipenv install
```

Si vous souhaitez travailler au développement du module, utilisez plutôt

```sh
pipenv install --dev
````

## Authors

- Émile Jetzer <emile.jetzer@polymtl.ca>
- Jacques Massicotte <jacques-2.massicotte@polymtl.ca>

Sous la supervision de Stéphane Kéna-Cohen et Camila Rizzi, dans le cadre du cours PHS8302.

## License

[AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)

## Related

Pour plus d'informations et de détails, je vous invite à consulter:

- Le [manuel du MFIA](https://docs.zhinst.com/mfia_user_manual/index.html) publié par Zurich Instruments
- La page Moodle du cours PHS8302
    - [En français](https://moodle.polymtl.ca/enrol/index.php?id=321)
    - [En anglais](https://moodle.polymtl.ca/enrol/index.php?id=4732)


